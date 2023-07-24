# Scian_Droplets_Omar_Final
## Instalacion de Droplets tool
Para poder instalar Droplets tool debe dirigirse a la carpeta Instalacion de este repositorio (https://github.com/OmarAEM/Scian_Drplets_Omar_Final/tree/main/Instalacion).

En la carpeta Instalacion encontrara dos carpetas:

Programas necesarios: en esta carpeta se encontrara el paso a paso de instalacion de Python y Visual Studio Code, debido a que estos programas son los necesarios para ejecutar Droplets tool. Si ya posee instalado estos programas, omita esta instalaciones.

Droplets tool: en esta carpeta se encontrara como descargar Droplets tool, que carpetas va a necesitar para guardado de imagenes de gotas y la instalacion de librerias necesarias para poder ejecutar Droplets tool (si en este ultimo apartado se generan errores, se recomienda desinstalar e instalar nuevamente Python y Visual Studio Code como encuentra en el paso a paso disponible en Programas necesarios).

## Ejecucion programa Droplets tool
Paso 1: Abrir programa Visual Studio Code, seleccione el boton "File" en la parte superior izquierda y luego seleccione "Open Folder..."
![Captura de pantalla 2023-07-19 030624](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/94a6fc4d-ce74-4a26-98d8-88a06c5b41c3)

Paso 2: Busque y seleccione la carpeta que se extrajo del archivo zip descargado del repositorio en Github, una vez ya seleccionada la carpeta, aprete el boton "Seleecionar carpeta"
![Captura de pantalla 2023-07-19 030741](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/4f383511-9144-43cd-a6f0-a9835ca954a0)


Paso 3: Al lado izquierdo podra visualizar todos los archivos que contiene la carpeta seleccionada anteriormente y una vez identificado, realice doble click sobre el archivo "Droplets.py"
![Captura de pantalla 2023-07-20 141231](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/efe15f89-416b-4abb-ac35-cce83b5d425f)


Paso 4: Ya con el archivo abierto, seleccione el icono en el cuadrado rojo de la imagen que se encuentra en la columna a la izquierda  y luego aprete "Run and Debug"

![Captura de pantalla 2023-07-19 030938](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/9fa36604-9052-4386-bdf6-8a5807b7a2a0)




Paso 4.1: La primera vez que realice el paso 5, aparecera la siguiente captura en la cual usted debe seleccionar "Python File"
![Captura de pantalla 2023-07-19 031000](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/15563407-ba37-40d5-a831-fcb15600d0c2)


Paso 5: Luego del paso 5 o 5.1 segun el caso, aparecera la interfaz donde debe ingresar la densidad de la gota, la densidad del medio y el diametro de la aguja en [G]. Una vez introducido estos 3 valores, debe apretar el boton "Load Image"
![Captura de pantalla 2023-07-20 142858](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/b0ee977c-f010-46a5-81ff-5391d1f3fb5a)

Paso 6: Una vez apretado el boton mencionado en el paso anterior, dirijase a la carpeta donde esten guardados sus imagenes de gotas colgantes, seleccione la imagen con la que desee trabajar y aprete el boton "Abrir"
![Captura de pantalla 2023-07-19 031313](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/ac2af28e-97cd-4f5d-acb3-7cddb668ba19)


Paso 7: Una vez abierta la imagen, primero debera seleccionar el area donde este la gota, para esto debera generar un rectangulo/cuadrado el cual contenga toda la gota; por lo que primero dirija su mouse al extremo superior izquierdo (imaginando que creara un rectangulo) haga click y mantenga apretado el boton del mouse en ese punto y luego mueva su mouse hasta la esquina inferior derecha para concretar el rectangulo, una vez llegado a ese punto debe de apretar el boton del mouse. Cuando ya finalice la accion antes mencionada, aprete el boton "Enter" de su teclado.
![Captura de pantalla 2023-07-19 031339](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/e572cdbe-25b0-4fd4-91bf-5edc64a98fbf)


Paso 8: Ahora aparecera nuevamente la imagen de la gota, repita el paso 8, pero en esta ocasion seleccione el area de la aguja.
![Captura de pantalla 2023-07-19 031402](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/bc1c3b5b-3561-4e6f-8704-cd30b86fd493)


Paso 9: Una vez finalizado el paso 9, aparecera nuevamente la interfaz del paso 6, en esta ocasion cierre la ventana con la cruz de la esquina superior derecha

![Captura de pantalla 2023-07-20 142858](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/097810a0-5ae5-4754-aa0d-c2d9a82c7371)


Paso 10: Ahora podra ver en la terminal (seccion de abajo de la captura de imagen) que se esta indicando que se esta realizando la deteccion de borde de la gota indicando en que proceso esta, una vez finalizado ese proceso, se indica los parametros finales asociados a la tension superficial
![Captura de pantalla 2023-07-19 034058](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/e6c8c5fa-c532-422e-b97e-ea91c55ab93f)


Paso 11: Si lo desea puede dirigirse a la carpeta "Resultados" que se creo en un comienzo en su carpeta donde guardara la imagenes de la gota; y dentro de esta carpeta podra encontrar todas las imagenes de gotas analizadas y nombre de archivo tiene como formato date_AÑO_MES_DIA__hour_HORA_MINUTO_SEGUNDO.
![Captura de pantalla 2023-07-20 141913](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/c9d77ce1-a927-4502-96c1-3e7fb87befca)

Si usted abre la imagen en esta se encontrara informacion de la gota las cuales corresponden a su tension superficial, numero de Bond, numero de Worthington, Parametro de forma y R_O (circunferencia asociada al gota). El numero de Worthington y el parametro de forma corresponden a valores entre 0 y 1 que nos permiten identificar que tan buena es la gota, esto quiere decir que tan acorde es la gota utilizada para determinar su tension superficial.
![Captura de pantalla 2023-07-20 142237](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/f160398b-dbbe-4014-aa2e-426aa1916027)

PROXIMAMENTE
Aun hay que hacer algunos cambiamos de nomenclatura en el nombre de guardado de imagen, como la de incluir nombre de imagen original.
Visualizacion del contorno de la gota detectado y circunferencia+R_0 para realizar procesamiento interno.}
Mejor explicacion de los todos los valores indicados en la imagen final.
Me di cuenta que debo arreglar el numero de Worthington debido a que no esta entregando valores acordes.


