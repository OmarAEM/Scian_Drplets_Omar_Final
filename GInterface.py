# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:29:01 2021

@author: phili
"""


#%% Abrir Interfaz Grafica
# que a su  vez llama la funcion de Guardar Los datos del Mouse
# ESTA ES LA SEGUNDA SCRIPT


import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
import MouseClick   
import numpy as np
import cv2
from tktooltip import ToolTip

from idlelib.tooltip import Hovertip
from tkinter import messagebox as mb

class GraphicInterface:
    
  def __init__(self, master):

      #Definicion de parametros iniciales para obtencion de tension superficial
      # Parametro                    Asociacion
      #   Drop            area donde se encuentra la gota
      #   Need            area donde se encuentra la aguja
      #   Image           imagen de la gota colgante que se utiliza
      #   Dens1           densidad de la gota [kg/m3]
      #   Dens2           densidad del medio [kg/m3]
      #   Thick           medida de la aguja (diametro en [G])
      #   folder          ubicacion del computador donde se encuentra la imagen

      frame =Frame(master)
      frame.pack()
      self.Drop = []
      self.Need = []
      self.Image=[]
      self.Dens1=[]
      self.Dens2=[]
      self.Thick=[]
      self.folder = []
      self.moment=0
      
      myLabel = Label(frame,text= "Insert Data")
      myLabel.pack(padx=10,pady=10)
      
      frame =LabelFrame(frame,text="Parameters",padx=20,pady=20)
             
      self.myLabel1 = Label(frame,text= "Drop Density [Kg/m3]:")
      self.myLabel1.pack(padx=10,pady=0)
      self.button1=Hovertip(self.myLabel1,"Densidad de la gota",hover_delay=0)
      
      self.Entry1 = Entry(frame,width=30, bd=1)
      self.Entry1.pack(pady=10)
      #self.Entry1.insert(0,float(997.0))

      
      self.myLabel2 = Label(frame,text= "Environment Density [Kg/m3]:")
      self.myLabel2.pack(padx=10,pady=0)
      self.button2=Hovertip(self.myLabel2,"Densidad del medio en el cual se encuentra colgando la gota. Ej: si usted coloca la gota y el medio en el que se encuentra es el aire debe ingresar 1.23 pues la densidad del aire es 1.23[Kg/m3]",hover_delay=0)
   
      self.Entry2 = Entry(frame,width=30, bd=1)
      self.Entry2.pack(pady=10)
      #self.Entry2.insert(0,float(1.23))

      
      
      self.myLabel3 = Label(frame,text= "Needle Thickness [G]:")
      self.myLabel3.pack(padx=10,pady=0)
      self.button3=Hovertip(self.myLabel3,"Diametro de la aguja",hover_delay=0)
      
      self.Entry3 = Entry(frame,width=30, bd=1)
      self.Entry3.pack(pady=10)
      #self.Entry3.insert(0,float(22))

      
      frame.pack(padx=100,pady=50)

            


      
      #Lectura de todos los parametros iniciales introducidos en la interface
      def CallBox():
    
          
          frame.filename = filedialog.askopenfilename(initialdir = "Desktop",title = "Select Image",filetypes = ( ("all files","*.*") ,("bmp files","*.bmp"), ("jpeg files","*.jpg"), ("png files","*.png")  ))
          print(frame.filename)
          img = cv2.imread(frame.filename)
          img_Temp = img.copy()
          img_Temp2 = img.copy()
          
          
          self.Drop  = np.array(MouseClick.CallMouseClick(img_Temp, "Select drop Region And Press Enter"))   # ESTAS COORDENADAS DEBO GUARDAR
          self.Need  = np.array(MouseClick.CallMouseClick(img_Temp2,"Select Needle Region And Press Enter")) 
          self.Image=img
          
          self.Dens1= float(self.Entry1.get())
          self.Dens2= float(self.Entry2.get())
          self.Thick= float(self.Entry3.get())
          self.folder=os.path.dirname(frame.filename)


          #print("Drop's Density:",self.Dens1)
          #print("Needle's Density:",self.Dens2)
          #print("Needle's Thickness:",self.Thick)              
          #print("Drop Coordinates:", self.Drop)
          #print("Needle Coordinates",self.Need)
          #self.moment = 1
          self.Entry1.config(state="disabled") 
          self.Entry2.config(state="disabled") 
          self.Entry3.config(state="disabled") 
          
          self.button["state"] = DISABLED

          return self.Drop,self.Need,self.Image,self.Dens1,self.Dens2,self.Thick,self.folder


      frame =LabelFrame(frame,text="Search for Image",padx=20,pady=20)
      frame.pack(padx=20,pady=20)
      
      
      self.button = Button(frame,text="Load Image", fg="black",command=CallBox)
      self.button.pack(padx=10,pady=20)

      
      #master.mainloop() 

      #root2=Tk()
      Button(master,text="Calculate",command=master.destroy).pack()
      master.mainloop()
      

#Funcion para guardado y posterior manipulacion de todos los parametros iniciales       
def mainWindow():
    
    root = tk.Tk()
    root.title("SCIAN-Lab's Drop Surface Tension Measurement Tool ")
    root.minsize(400, 100)
    app =GraphicInterface(root)

    #root.mainloop()

    

     
    
    DropCoords= np.array(app.Drop)
    NeedCoords=np.array(app.Need)
    imageT =app.Image
    
    Dens1 =app.Dens1
    Dens2 =app.Dens2
    Thick  =app.Thick
    folder =app.folder


    #print("cors",DropCoords)
    
    return DropCoords, NeedCoords, imageT,Dens1,Dens2,Thick,folder


#Si desea probar la visulizacion y obtencion de zonas donde esta la gota y la aguja, quite # de la siguiente linea
#Test_interface = mainWindow()

 

    