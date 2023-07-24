# -*- coding: utf-8 -*-
"""
Created on Mon May 10 13:39:59 2021

@author: phili
"""


from scipy.spatial.distance import directed_hausdorff

from matplotlib import animation
from scipy      import optimize
from mpl_toolkits.mplot3d import Axes3D 


import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour
import cv2

from scipy.spatial.distance import directed_hausdorff

from shapely.geometry import Point, LineString, Polygon ,MultiPolygon
from descartes import PolygonPatch
import shapely.ops as so
import os
import pandas as pd
import xlsxwriter
import GInterface
from datetime import datetime
from csv import writer

#Ejecucion de la interfaz para obtener parametros iniciales de la gota
#Coordenadas = GInterface.mainWindow()

class Method:
    
    def __init__(self,Data):
        
        self.Data=Data
        
        dropArea    = Data[0]
        needleArea  = Data[1]
        imag        = Data[2]
        
        Dens1       =Data[3]
        Dens2       =Data[4]
        Thick       =Data[5]

        folder = Data[6]
        
        #Diametro de la aguja
        #El diametro de las aguja a utilizar se lee a partir del calibre(Gauge[G]) de este, por lo que se debe hacer la conversion de [G] a [mm] y luego pasarlo a [m] para simplificar 
        # trabajar en las mismas unidades en todos los calculos
        options_needleDiameter = np.array([[18,1.2],[19,1.1],[20,0.9],[21,0.8],[22,0.7],[23,0.6],[25,0.5],[26,0.45],[27,0.4],[30,0.3]]) # inf obtenida de lectura_aguja.jpg en formato [unidad en G, unidad en mm]
        diameter_G = Thick 
        needleDiameter_mm = options_needleDiameter[np.where(options_needleDiameter[:,0] == diameter_G),1][0][0] # seleccionamos la medida en mm de diametro ingresa en G
        #needleDiameter_mm=Thick #en mm -usar esta linea si Thick se introduce en mm
        needleDiameter = needleDiameter_mm*1e-3  #conversion de needleDiameter_mm desde [mm] a [m]

        #Densidades
        density_drop = Dens1 #[kg/m^3]
        density_environment = Dens2 #[kg/m^3]
        diff_density = density_drop-density_environment #[kg/m^3]

        #Aceleracion de gravedad [m/s^2]
        g = 9.81          # Gravedad


        #Seleccion de las areas donde se encuentran tanto la gota como la aguja, los puntos a seleccionar para generar el area seran a partir de los vertices de un cuadrado/rectangulo
        # y estos tendran una estructura de lista [ix,iy,ex,ey] donde el punto inicial de seleccion sera (ix,iy) y el punto final de seleccion sera (ex,ey).
        # "i:initial", "e:end" y "x e y" las coordenadas; siendo _d los puntos asociados al area de la gota y _n los asociados a la aguja.

        #  (ix,iy)----------------|
        #     |                   |  
        #     |                   |
        #     |----------------(ex,ey)

        ix_d=dropArea[0,0]
        iy_d=dropArea[0,1]
        ex_d=dropArea[0,2]
        ey_d=dropArea[0,3]       
        ix_n=needleArea[0,0]
        iy_n=needleArea[0,1]
        ex_n=needleArea[0,2]
        ey_n=needleArea[0,3]

        dropArea=[ix_d,iy_d,ex_d,ey_d]
        needleArea=[ix_n,iy_n,ex_n,ey_n]

          
        #La imagen de la gota se debe trabajar en escala de grises 
        image = imag
        image_output2=image.copy()
        GrayImage=  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        image_output=GrayImage.copy()
        #print("-------------------------------------------------------------")
        #print("Image Properties:")
        #print("")
        #print("Image size")
        #print("Xsize:",GrayImage[0,:].size)
        #print("Ysize:",GrayImage[:,0].size)
        
        #print("--------------------------------------------------------------")
        
        #print("Density Drop",density_drop)
        #print("Density Medium",density_environment)
        #print("Needle Thickness:",Thick)
        #print("--------------------------------------------------------------")
        
        
        #Deteccion de borde de la gota
        def filterImage(img):
            edges = cv2.Canny(img,20,200)
            return edges
                       
        edges =filterImage(GrayImage)


        #Dimensiones de la imagen 
        size_x=GrayImage.shape[1]
        size_y=GrayImage.shape[0]


        #Obtencion del contorno de la aguja
        def getNeedle(size,img,needleArea,image):
                    
            #print("getNeedle function")
            #print("This needle width")

            nix=needleArea[0]
            niy=needleArea[1]
            nex=needleArea[2]
            ney=needleArea[3]
                    
            needle2 = []          
            for y in range(niy,ney,1):
                for x in range(nix,nex,1):          
                    if img[y,x] == 255:        
                        np.array([needle2.append([x,y])])        
                        needleArray = np.array(needle2) 
            #print(needleArray)
                                
            #plt.figure()
            #plt.title("Needle sides' Segmented")
            #cv2.rectangle(img,(nix,niy),(nex,ney),(0,0,255),3)
            #plt.imshow(image, cmap="gray")
            #plt.scatter(needleArray[:,0],needleArray[:,1])
            #plt.show()   
                    
            return needleArray
                
        NeedleArray=getNeedle(size_x,edges,needleArea,GrayImage)

        #Obtencion del centro de la aguja
        def NeedleCenter(needleArray):
            #print("NeedleCenter Function")
                    
            minNeedle = np.min(needleArray[:,0])
            maxNeedle = np.max(needleArray[:,0])
                    
            centerNeedle = int((minNeedle+maxNeedle)/2)
                    
            #plt.figure()
            #plt.title("Center of needle")
            #plt.imshow(edges, cmap="gray")
            #plt.scatter(needleArray[:,0],needleArray[:,1])
            #plt.scatter(centerNeedle,needleArray[0,1],color="red")
            #plt.show()   
                    
            return centerNeedle
                
        Ncenter = NeedleCenter(NeedleArray)

        # Buscamos la posicion x,aproximada, de la aguja tanto por su lado derecho, como izquierdo
        NeedleArray_left = []
        NeedleArray_right = []
        for i in range(0,len(NeedleArray)):
            if NeedleArray[i][0] < Ncenter:
                NeedleArray_left.append(NeedleArray[i][0])
            else:
                NeedleArray_right.append(NeedleArray[i][0])
        needle_left = np.array(NeedleArray_left)
        needle_right = np.array(NeedleArray_right)

        needle_left= int(np.mean(needle_left))
        needle_right= int(np.mean(needle_right))

        #Generacion linea blanca para poder realizar snake, debido a que la forma en la que se utilizara snake (con un rectangulo inicial) generaba problemas 
        # si no se hacia un corte en la imagen
        for i in range(needle_left,needle_right):
            GrayImage[iy_d+10][i] = 255

        edges =filterImage(GrayImage)

        edges_output = filterImage(image_output)


        def showing(img,string):
            
                    plt.title(string)
                    plt.imshow(img,"gray")
                    plt.show()
            
#        showing(GrayImage,"Gray Image")
#        showing(edges,"Edge detection Image")



        #     (1)-----line_upper-----(2)
        #      |                      |  
        #      |                      |
        #  line_left              line_right
        #      |                      |
        #      |                      |
        #     (4)-----line_lower-----(3)

        #Se crean 2 arrays  por cada linea guardando, en un array, su coordenada x y ,en otro, su coordenada y
        # esto en relacion a las areas definida para determinar el contorno de la gota
        #             line                     direccion de guardado
        #  line_upper_x/line_upper_y                (1)----->(2)
        #  line_right_x/line_right_y                (2)----->(3)
        #  line_lower_x/line_lower_y                (3)----->(4)
        #   line_left_x/line_left_y                 (4)----->(1)


        def ShowInit(img,dropArea,needleArea):

            dix=dropArea[0]
            diy=dropArea[1]
            dex=dropArea[2]
            dey=dropArea[3]
                                
            nix=needleArea[0]
            niy=needleArea[1]
            nex=needleArea[2]
            ney=needleArea[3]

        # Generacion de lineas con respecto a eje x
            line_upper_x = np.linspace(dix,dex,dex-dix+1)   
            line_right_x = np.linspace(dex,dex,dey-diy+1)   
            line_lower_x = np.linspace(dex,dix,dex-dix+1)
            line_left_x = np.linspace(dix,dix,dey-diy+1)

        # Generacion de lineas con respecto a eje y
            line_upper_y = np.linspace(diy,diy,dex-dix+1)
            line_right_y=np.linspace(diy,dey,dey-diy+1)
            line_lower_y= np.linspace(dey,dey,dex-dix+1)
            line_left_y=np.linspace(dey,diy,dey-diy+1)
        
        #Generacion de rectangulo a partir de lineas, separando la coordenada x e y, el sentido de union corresponde a (1)-->(2)-->(3)-->(4)
            line_x=np.append(line_upper_x,line_right_x)
            line_x=np.append(line_x,line_lower_x)
            line_x=np.append(line_x,line_left_x)

            line_y=np.append(line_upper_y,line_right_y)
            line_y=np.append(line_y,line_lower_y)
            line_y=np.append(line_y,line_left_y)

            rect_init = np.array([line_y,line_x]).T
                    
                    
            #plt.figure()
            #plt.title(" Inicialización Para segmentar con Snakes")
            #cv2.rectangle(img,(dix,diy),(dex,dey),(153,0,73),3)
            #cv2.rectangle(img,(nix,niy),(nex,ney),(0,255,0),3)
            #plt.imshow(img,cmap="gray")
            #plt.plot(rect_init[:,1],rect_init[:,0],color="red")
            #plt.scatter(cx,cy,color="red")
            #plt.scatter(dix,diy,color="darkorange")
            #plt.scatter(dex,dey,color="darkorange")
            #plt.scatter(nix,niy,color="darkorange")
            #plt.scatter(nex,ney,color="darkorange")
            #plt.xlabel("Pixeles eje x")
            #plt.ylabel("Pixeles eje y")
            #plt.show()
                    
            return

        #Verificacion de creacion correcta de forma inicial para snake
        #ShowInit(image,dropArea,needleArea)




        #
        def useSnake(img,alphaValue,dropArea):
            #print("useSnake function")
                
            dix=dropArea[0]
            diy=dropArea[1]
            dex=dropArea[2]
            dey=dropArea[3]
                    
        # Generacion de lineas con respecto a eje x
            line_upper_x = np.linspace(dix,dex,dex-dix+1)   
            line_right_x = np.linspace(dex,dex,dey-diy+1)   
            line_lower_x = np.linspace(dex,dix,dex-dix+1)
            line_left_x = np.linspace(dix,dix,dey-diy+1)

        # Generacion de lineas con respecto a eje y
            line_upper_y = np.linspace(diy,diy,dex-dix+1)
            line_right_y=np.linspace(diy,dey,dey-diy+1)
            line_lower_y= np.linspace(dey,dey,dex-dix+1)
            line_left_y=np.linspace(dey,diy,dey-diy+1)
        
        #Generacion de rectangulo a partir de lineas, separando la coordenada x e y, el sentido de union corresponde a (1)-->(2)-->(3)-->(4)
            line_x=np.append(line_upper_x,line_right_x)
            line_x=np.append(line_x,line_lower_x)
            line_x=np.append(line_x,line_left_x)

            line_y=np.append(line_upper_y,line_right_y)
            line_y=np.append(line_y,line_lower_y)
            line_y=np.append(line_y,line_left_y)

            rect_init = np.array([line_y,line_x]).T
                    
        #   snake = active_contour(gaussian(img, 3),init, alpha=alphaValue, beta=10, gamma=0.001,coordinates='rc') 
            snake = active_contour(gaussian(img, 3),rect_init, alpha=alphaValue, beta=10, gamma=0.001) 
                    


            #Visualizacion de snake generado       
            #fig = plt.figure()
            #ax=plt.subplot()
            #plt.title("Borde segmentado con Snake")
            #plt.imshow(img,cmap="gray")
            #plt.plot(snake[:,1],snake[:,0],color ="red",label="Contorno Activo")
            #ax.legend(loc="best")
            #plt.grid()
            #plt.show()   
                    
            return snake
        

        print("")
        print("------------------------------------------------------------------------------")
        print("Calculando contorno de la gota")
        print("Proceso 0/2 completado")   
        GraySnake1 = useSnake(GrayImage,0.010,dropArea)
        print("Proceso 1/2 completado") 
        GraySnake2 = useSnake(edges,0.010,dropArea)
        print("Proceso 2/2 completado") 
        print("------------------------------------------------------------------------------")
        print("")


        print("A continuacion se indicaran los resultados obtenidos")

        print(GraySnake2)
       
        #--------------REVISAR--------------#
        def AreaShoeLace(Array):
                    
            xArray=Array[:,0]
            yArray=Array[:,1]
                    
            sumaSs1=0
            sumaSs2=0    
                    
            for i in range(0,xArray.size-1,1):
                        
                sumaSs1 = sumaSs1+ xArray[i]*yArray[i+1]
                sumaSs2 = sumaSs2+ xArray[i+1]*yArray[i]
                        
            smSs1 = sumaSs1+ xArray[xArray.size-1]*yArray[0]
            smSs2 = sumaSs2+ xArray[0]*yArray[xArray.size-1]
                    
            Area= (abs(smSs1-smSs2))/2
            return Area
 
        #GrayArea = AreaShoeLace(GraySnake1)
        edgeArea = AreaShoeLace(GraySnake2)
        #print("Areas de ambas segmentaciones : ",GrayArea,edgeArea)

        #--------------REVISAR--------------#
        def poly(snake1,snake2):
                    
            poly1 = Polygon(snake1)
            poly2 = Polygon(snake2)
                    
            poly1_area = poly1.area
            poly2_area = poly2.area
                    
            return poly1_area,poly2_area
                #
        #areas=poly(GraySnake1,GraySnake2)
                
                    
        #print("Valores Areas con Poly :",areas)
        #print("Valores Areas con shoe : ",GrayArea,edgeArea)



        #Diametro de la aguja en pixeles
        def NeedleWidth(needleArray):
            #print("NeedleWidth Function")
                    
            needleSize = needleArray[:,0].size
            diff = []
                    
            for i in range(0,needleSize-2,2):
                        
                np.array([diff.append([needleArray[i+1,0]-needleArray[i,0]])])
                        
                diffArray= np.array(diff)
                absDiff = abs(diffArray)
                        
                realDiff =[]
                        
                for i in range(0,len(absDiff),1):
                    if absDiff[i]>2:
                                
                        realDiff.append(absDiff[i])
                                
            realDiff = np.array(realDiff)
            needleWidth = int(np.mean(realDiff))
                    
            return needleWidth

        Nwidth = NeedleWidth(NeedleArray)
        #print("Needle width:",Nwidth,"Pixel Units")


        #Relacion [m] por pixel, para tranformar toda la informacion de pixeles a metros
        def Ratio(width):
            #print("Ratio Function")
                    
            ratio = needleDiameter/width
                    
            return ratio
                
        ratio = Ratio(Nwidth)
        #print("ratio",ratio)


        #Obtencion de porcion de superficie inferior de la gota
        def getApex(imYsize,centerNeedle,needleArray,img,needleArea,dropArea):
            #print("getApex Function:")
                    
                    
            dix=dropArea[0]  # drop inicial x
            diy=dropArea[1]  # drop inicial y
            dfx=dropArea[2]  # drop inicial x
            dfy=dropArea[3]  #
                    
                    
            nix=needleArea[0]
            niy=needleArea[1]
            nfx=needleArea[2]
            nfy=needleArea[3]
                    
                    
            apexPoint  = []

            for y in range(diy+100,dfy,1):    
                        
                while img[y,centerNeedle]!=0:
                            
                    np.array([apexPoint.append([centerNeedle,y])])
                            
                    break
                        
                        
            apex = np.array(apexPoint)
                
            #print("apex,",apex)
                    
                    
            apexRegion=[]
                    
            for x in range(needleArray[0,0],needleArray[1,0],1):
                        
                for y in range(apex[0,1]-3,apex[0,1]+3,1):        
                    if edges[y,x]==255:
                                
                        np.array([apexRegion.append([x,y])])
                        apexRegionArray= np.array(apexRegion)
                                
            #plt.figure()
            #plt.title("Apex region ")
            #plt.imshow(edges, cmap="gray")
            #plt.scatter(needleArray[:,0],needleArray[:,1])
            #plt.scatter(centerNeedle,needleArray[0,1],color ="red")
            #plt.scatter(apexRegionArray[:,0],apexRegionArray[:,1])
                #   
                    
                    
            apexApex = np.max(apexRegionArray[:,1])
            apexSize = apexRegionArray[:,1].size
                    
            apexPosition=[]
                    
            for x in range(0,apexSize,1):
                        
                        
                if apexRegionArray[x,1]==apexApex:
                            
                    np.array([apexPosition.append([x])])
                    apexPositionArray=np.array(apexPosition)
                            
            minPos=np.min(apexPositionArray)
            maxPos=np.max(apexPositionArray)
                    
            apexLine = int((apexRegionArray[minPos,0]+apexRegionArray[maxPos,0])/2)
            apexFin = np.array([apexLine,apexApex])
                    
            #plt.figure()
            #plt.title("Apex Position ")
            #plt.imshow(img, cmap="gray")
            #plt.scatter(apexFin[0] ,apexFin[1] )
                #    plt.plot(GraySnake1[:,1],GraySnake1[:,0])
            #plt.show()
                    
            #print("apex position",apexFin)
            return apexFin
                
        GrayImage_2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )        
        edges_2 =filterImage(GrayImage_2)        
        apex = getApex(size_y,Ncenter,NeedleArray,edges_2,needleArea,dropArea)

        print("apex position",apex[1])
        print("apex position",apex[0])


        def surface_drop(surface,DropArea):
            dix=dropArea[0]  # drop inicial x
            diy=dropArea[1]  # drop inicial y
            dfx=dropArea[2]  # drop final   x
            dfy=dropArea[3]

            points=[]

            for i in range(dix,dfx):
                for j in range(diy, dfy):

                    if surface[j,i] == 255:         # coordenadas pertenecientes a la superficie de la gota
                                        
                                np.array([points.append([i,j])])
            return points

        drop_points=surface_drop(edges_output,dropArea)



        #Obtencion de R_0 a partir del apex anterior, esto se utiliza para calcular el radio (R_0) asociado a una circunferencia producida por apex
        def getRadio2(snake,apex,DropArea,image,gray,snake2,snake3):
                    
            dropArea=DropArea
                    
            dix=dropArea[0]  # drop inicial x
            diy=dropArea[1]  # drop inicial y
            dfx=dropArea[2]  # drop final   x
            dfy=dropArea[3]  # drop final   y
                    
                    
            Distance = 68
                    
            imYsize = snake[:,0].size
                    
            Xinicio = apex[0]-Distance
            Xfin    = apex[0]+Distance
                    
            surface=[]
            for i in range(Xinicio,Xfin,1):
                        
                j =  dfy-2
                        
                while j > 0:
                            
                    if snake[j,i] == 255:         # coordenadas pertenecientes a la superficie de la gota
                                
                        np.array([surface.append([i,j])])
                                
                        break
                            
                    j -= 1
                            
            surface
            surfaceArray=np.array(surface)
                    
                    
                    
            #Visualizacion de la superficie del apex        
            #plt.figure()
            #plt.title("Apex surface")
            #plt.imshow(snake,cmap="gray")
            #plt.scatter(surfaceArray[:,0],surfaceArray[:,1])
            #plt.show()
                    

            #Obtencion del centro de la circunferencia de radio R_0, utilizando la superficie del apex seleccionado
            x =surfaceArray[:,0]
            y =surfaceArray[:,1]

            x_m = np.mean(x)
            y_m = np.mean(y)

            x_mArray = np.ones(x.size)*x_m
            y_mArray = np.ones(y.size)*x_m
                            
            u2 = x - x_m
            v2 = y - y_m
                    
            Suv2  = np.sum(u2*v2)
            Suu2  = np.sum(u2**2)
            Svv2  = np.sum(v2**2)
            Suuv2 = np.sum(u2**2 * v2)
            Suvv2 = np.sum(u2 * v2**2)
            Suuu2 = np.sum(u2**3)
            Svvv2 = np.sum(v2**3)
                    
            A2 = np.array([ [ Suu2, Suv2 ], [Suv2, Svv2]])
                    
            B2 = np.array([ Suuu2 + Suvv2, Svvv2 + Suuv2 ])/2.0
            uc2, vc2 = np.linalg.solve(A2, B2)

            #Coordenada x,y del centro de la circunferencia de radio R_0
            xc_2 = x_m + uc2
            yc_2 = y_m + vc2

                    
            Ri_2     = np.sqrt((x-xc_2)**2 + (y-yc_2)**2)
            R_0      = np.mean(Ri_2)
            
            residu_2 = np.sum((Ri_2-R_0)**2)
               
            return R_0,xc_2,yc_2

        GrayImage_3 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )
        edges_3 =filterImage(GrayImage_3)
        GrayImage_4 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )
        edges_4 =filterImage(GrayImage_4)
                
        Rvalues =getRadio2(edges,apex,dropArea,image,GraySnake2,edges_3,edges_4)
        #print(Rvalues)
        #print("R_0",Rvalues[0])




        #Obtencion de tension superficial
        def getGamma(Radio,yc_2,imXsize,imYsize,apexFin,IMG,DropArea,Density):
                    
                    dropArea=DropArea
                            
                    dix=dropArea[0]  # drop inicial x
                    diy=dropArea[1]  # drop inicial y
                    dfx=dropArea[2]  # drop final   x
                    dfy=dropArea[3]  # drop final   y
                    
                    
                    
                    #A partir del centro de la circunfrencia obtenido anteriormente, se busca De y Ds asociados al parametro de forma, para 
                    # posterior calculo del numero de Bond
                    Yinicio = int(yc_2)-100
                    Yfin    = int(yc_2)+100
                    
                    Lone   = np.linspace(1,imXsize,imXsize)
                
                    lin  = Yinicio *np.ones((1,len(Lone)))
                    lfin = Yfin*np.ones((1,len(Lone)))
                
                    dropSide1 = []
                    Xlimite = imXsize-30
                    
                    for i in range(Yinicio,Yfin,1):
                        
                        for j in range(150,Xlimite,1):
                            
                            if IMG[i,j] == 255:
                                
                                np.array([dropSide1.append([j,i])])
                                
                                break
                
                    
                    dropSide1
                    dropSideArray1 = np.array(dropSide1) 
                    
                    dropSide2 = []
                    Xlimite = imXsize-30
                    
                    for i in range(Yinicio,Yfin,1):
                        
                        for j in range(150,Xlimite,1):
                            
                            jj = Xlimite-j
                            
                            if IMG[i,Xlimite-j] == 255:
                                
                                np.array([dropSide2.append([jj,i])])
                                
                                break
                                
                    dropSide2
                    dropSideArray2 = np.array(dropSide2) 
                    
                    Left= np.min(dropSideArray1[:,0])
                    Right=np.max(dropSideArray2[:,0])
                    
                    resultLeft  = np.array(np.where(dropSideArray1 == Left))
                    resultRight = np.array(np.where(dropSideArray2 == Right))
                    
                    DeDistance  = Right-Left
                    
                    DeYlenght = dropSideArray2[resultRight[0,0],1]*(np.ones((1,DeDistance+1)))
                    DeXlenght =  np.linspace(Left,Right,DeDistance+1)
                    
                    #print("Dey",DeYlenght[0,0])
                    
                    ApexOnes = apexFin[0]*np.ones((1,DeDistance+1))
                    ApexLine = np.linspace(apexFin[1], apexFin[1]-(DeDistance),DeDistance+1)
                    
                    upSide1=[]
                    
                    for i in range(0,Xlimite,1):
                        
                        if edges[int(ApexLine[-1]),i]==255:
                            
                            np.array([upSide1.append([ApexLine[-1],i])])
                            
                            break
                        
                    upSide1Array = np.array(upSide1)
                    
                    upSide2=[]    
                    
                    for j in range(0,imXsize-10,1):
                        
                        if edges[int(ApexLine[-1]),Xlimite-j]==255:
                            
                            #print(edges[int(ApexLine[-1]),Xlimite-j])
                            
                            np.array([upSide2.append([[ApexLine[-1]],[Xlimite-j]])])
                            
                            break
                        
                    upSide2Array = np.array(upSide2)
                    
                    DsDistance = int((upSide2Array[0,1]-upSide1Array[0,1]))+1
                    dsOnes = int(ApexLine[-1])*np.ones((1,DsDistance))
                    dsLine = np.linspace(int(upSide2Array[0,1]),int(upSide1Array[0,1]),DsDistance)
                    
                    
                    DsReal=DsDistance*ratio
                    DeReal=DeDistance*ratio
                    DsDeReal = DsReal/DeReal
                    
                    #Obtencion de numero de Bond a partir de la relacion de forma Ds/De y posterior calculo de 
                    # tension superficial a partir de su formula
                    BondNumber = 0.12836-(0.7577*(DsDeReal))+(1.7713*np.power(DsDeReal,2))-(0.5426*np.power(DsDeReal,3))
                    GammaTension = ((Density*np.square(Radio*ratio)*g)/(BondNumber))*1000
                    
                    
                    #print("")
                    #print("------------------------------------------------------------------------------")
                    #print("An a aproximated surface Tension is" , GammaTension, "[mN/Meter] compared with")
                    #print("The literature value for water is: 72.75 [nN/M]" )
                    #print("------------------------------------------------------------------------------")
                    #print("")
                    
                    
                    #Expancion de apex, es decir, se utiliza una mayor superficie inferior de la gota para obtener los R_0 asociados a esos nuevos apex
                    # onteniendo asi una amplia cantidad de R_0
                    dl=[]
                    rangeValues = []
                    
                    for i in range(70,90,1):
                        
                        start =  apexFin[0]-i
                        end   =  apexFin[0]+i
                        
                        np.array([rangeValues.append([start,end])])
                        np.array([dl.append([i])])
                        
                    dlArray  = np.array(dl)    
                    rangeArray = np.array(rangeValues)
                    RangeSize =  rangeArray[:,0].size
                    surfacePoints = []
                    Rvalues = []
                    centers = []
                    Rvalues2 = []
                    Xc_values = []
                    Yc_values = []
                    
                    
                    for i in range(0,RangeSize,1):
                        start2 = rangeArray[i,0]
                        end2   = rangeArray[i,1]
                        
                        surfacePoints = []
                        
                        for ii in range(start2,end2,1):
                        
                            j = dfy-2
        #                    j =  imYsize-30
                            
                            while j > 0:
                                
                                if edges[j,ii] == 255:
                                    
                                    surfacePoints.append([ii,j])
                                    sf = np.array(surfacePoints)
                                    
                                    break
                                
                                j -= 1
                                
                        for iii in range(0,1,1):
                            
                            x2 =sf[:,0]
                            y2 =sf[:,1]
                            
                            
                            x2_m = np.mean(x2)
                            y2_m = np.mean(y2)
                        
                            x2_mArray = np.ones(x2.size)*x2_m
                            y2_mArray = np.ones(y2.size)*x2_m
                            
                            u2 = x2 - x2_m
                            v2 = y2 - y2_m
                            
                            
                            Suv2  = np.sum(u2*v2)
                            Suu2  = np.sum(u2**2)
                            Svv2  = np.sum(v2**2)
                            Suuv2 = np.sum(u2**2 * v2)
                            Suvv2 = np.sum(u2 * v2**2)
                            Suuu2 = np.sum(u2**3)
                            Svvv2 = np.sum(v2**3)
                        
                            A2 = np.array([ [ Suu2, Suv2 ], [Suv2, Svv2]])
                            B2 = np.array([ Suuu2 + Suvv2, Svvv2 + Suuv2 ])/2.0
                        
                            uc2, vc2 = np.linalg.solve(A2, B2)
                            xc_2 = x2_m + uc2
                            yc_2 = y2_m + vc2
                        
                            Ri_2     = np.sqrt((x2-xc_2)**2 + (y2-yc_2)**2)
                            R_2      = np.mean(Ri_2)
                        
                            residu_2 = np.sum((Ri_2-R_2)**2)
                            np.array(Rvalues.append([R_2]))
                            np.array(Xc_values.append([xc_2]))
                            np.array(Yc_values.append([yc_2]))
                            
                    RadioArray=np.array(Rvalues)    
                    MeanRadio= np.mean(RadioArray)
                    MeanXc=np.mean(Xc_values)
                    MeanYc=np.mean(Yc_values)
                            
                    
                    #Grafico comportamiento de R_0 a distintos apex
                    #plt.figure()
                    #plt.title("Radios de curvatura")
                    #plt.plot(dl,RadioArray,".")
                    #plt.ylim(182,193)
                    #plt.grid()
                    #plt.savefig('Radios de curvatura.png')
                    #plt.show()
                    


                    #Calculo del gamma promedio a partir de todos los radios R_0 obtenidos                     
                    Gamma = []
                    
                    for i in range(0,RangeSize,1):
                        
                        G = ((Density*np.square(RadioArray[i]*ratio)*g)/(BondNumber))*1000
                        np.array([Gamma.append([G])])
                            
                    GammaArray = np.array(Gamma)
                    meanGamma = np.mean(GammaArray)
                    stdGamma  = np.std(GammaArray)

                    #Grafico de tension superficial obtenidos      
                    #plt.figure()
                    #plt.title("Surface Tension Values")
                    #plt.plot(dl,GammaArray[:,0],".")
                    #plt.grid()
                    #plt.ylim(65,78)
                    #plt.savefig('GraficoTensión.png')
                    #plt.show()
                            
                    print("")
                    print("------------------------------------------------------------------------------")
                    print(" The Mean Surface Tension  Value is :",meanGamma,"+/-",stdGamma)
                    print("------------------------------------------------------------------------------")
                    print("")

                   

                    #Visualizacion de Ds, De y apex      
                    #plt.figure()
                    #plt.title("Segmented Droplet")
                    #plt.imshow(edges,cmap="gray")
                    #plt.scatter(sf[:,0],sf[:,1])
                    #plt.scatter(dsLine,dsOnes,color="red")
                    #plt.scatter(DeXlenght,DeYlenght,color = "orange")
                    #plt.scatter(xc_2,yc_2,color ="orange")
                    #plt.scatter(apexFin[0],apexFin[1],color="yellow")
                    #plt.savefig('segmentedDrop.png')
                    #plt.show()

                    return meanGamma,stdGamma,MeanRadio,BondNumber,MeanXc,MeanYc #,DeYlenght[0,0]
                
                        
                        
        GammaValues = getGamma(Rvalues[0],Rvalues[2],size_x,size_y,apex,edges,dropArea,diff_density)
        #print("GammaValues",GammaValues)
                
                
        print("")
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")



        

        Worthington_Number=edgeArea*np.pi*ratio
        Shape_parameter=(edgeArea-np.pi*GammaValues[2])/edgeArea

        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        gamma=round(GammaValues[0],3)
        stdgamma=round(GammaValues[1],3)
        bond=round(GammaValues[3],3)
        wort=round(Worthington_Number,3)
        shape_pam=round(Shape_parameter,3)
        R_0=round(GammaValues[2]*ratio,3)
        parameters=["Tension superficial: "+str(gamma)+" +/- "+str(stdgamma)+" [N/m]","Numero de Bond: "+str(bond),"Numero worht: "+str(wort),"Parametro de forma: "+str(shape_pam),"R_0: "+str(R_0)+" [m]"]
        

        def contorno(surface,image,R_0,Xc,Yc,apexX,apexY):

  
            # Radius of circle
            radius = 1
            
            # Blue color in BGR
            color = (255, 0, 0)
            
            # Line thickness of 2 px
            thickness = 1
            
            # Using cv2.circle() method
            # Draw a circle with blue line borders of thickness of 2 px
            for i in range(0,len(surface)):
                center_coordinates=(surface[i][0],surface[i][1])
                image = cv2.circle(image, center_coordinates, radius, color, thickness)

            radius2=int(R_0)
            color2=(0,255,0)
            center_coordinates2=(int(Xc),int(Yc))
            image=cv2.circle(image, center_coordinates2, radius2,color2, thickness)
            image=cv2.circle(image, center_coordinates2, 6 ,color2, -1)

            start_point=(int(Xc),int(Yc))
            end_point=(apexX,apexY)
            image = cv2.arrowedLine(image, start_point, end_point,color2, thickness) 
            cv2.putText(image_output2, "R_0", (int(Xc)+10,int((apexY+int(Yc))/2)), font, fontScale, color2, thickness, cv2.LINE_AA)

            
            return image

        image_output2=contorno(drop_points,image_output2,GammaValues[2],GammaValues[4],GammaValues[5],apex[0],apex[1])

        j=len(parameters)-1
        for i in range(20,141,30):
            org = (10, image.shape[0]-i)
            cv2.putText(image_output2, parameters[j], org, font, fontScale, color, thickness, cv2.LINE_AA)
            j-=1

        

        now=datetime.now()
        date="date_"+str(now.year)+"_"+str(now.month)+"_"+str(now.day)+"__hour_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)

        date2=str(now.year)+"_"+str(now.month)+"_"+str(now.day)
        hour=str(now.hour)+":"+str(now.minute)+":"+str(now.second)

        #Guardo informacion de la imagen junto a su tension superficial en la carpeta resultados
        total_folder = 0
        dir = folder+"/Resultados/"
        for path in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, path)):
                total_folder += 1

        if total_folder == 0:
            d = {"Fecha":[date2],"Hora":[hour],'Tension superficial': [gamma], 'error tension': [stdgamma],"Numero de Bond": [bond], "Numero worht: ":[wort],"Parametro de forma: ":[shape_pam],"R_0: ":[R_0]}
            df = pd.DataFrame(data=d)
            df.to_csv(folder+'/Resultados/Result.csv')
        if total_folder != 0:
                df2=pd.read_csv(folder+'/Resultados/Result.csv')
                index=df2.shape[0]
                list_data=[index,date2,hour,gamma,stdgamma,bond,wort,shape_pam,R_0]
                with open(folder+'/Resultados/Result.csv', 'a', newline='') as f_object:  
                    # Pass the CSV  file object to the writer() function
                    writer_object = writer(f_object)
                    writer_object.writerow(list_data)  
                    f_object.close()
        save_Gamma=folder+"/Resultados/"+date+".png"
                
        cv2.imwrite(save_Gamma,image_output2)



        #Grafico R_0 vs De      
        def plotRadio(img,apx,de):
                    
                    ap= apx
                    print(ap)
                    de =de
                    print(de)
                    
                    diff = ap[1]-de
                    print("difference",diff)
                    
                    
                    cx=ap[0]
                    cy=de
                    
                    print("radio de inicialización",diff)
                    s = np.linspace(0, 2*np.pi, 400)
                    r =[cy]  + (diff*np.sin(s)/1.0)#  500
                    c =[cx]  + (diff*np.cos(s)/1.0) #1
                    init = np.array([r, c]).T
                    
                    plt.figure()
                    plt.title("R0 from De")
                    plt.imshow(img)
                    plt.plot(init[:,1],init[:,0],color="red")
                    plt.scatter(cx,cy,color="red")
                    plt.show()
            
#        plotRadio(edges,apex,DS[2])

            

        
        


     
#Method(Coordenadas)


