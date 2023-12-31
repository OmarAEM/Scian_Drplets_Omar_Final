# Scian_Droplets_Omar_Final
## Instalacion de Droplets tool
Para poder instalar Droplets tool debe dirigirse a la carpeta Instalacion de este repositorio (https://github.com/OmarAEM/Scian_Drplets_Omar_Final/tree/main/Instalacion).

En la carpeta Instalacion encontrara dos carpetas:

Programas necesarios: en esta carpeta se encontrara el paso a paso de instalacion de Python, Visual Studio Code y Git, debido a que estos programas son los necesarios para ejecutar Droplets tool. Si ya posee instalado estos programas, omita esta instalaciones.

Droplets tool: en esta carpeta se encontrara como descargar Droplets tool, que carpetas va a necesitar para guardado de imagenes de gotas y la instalacion de librerias necesarias para poder ejecutar Droplets tool (si en este ultimo apartado se generan errores, se recomienda desinstalar e instalar nuevamente Python, Visual Studio Code y Git como encuentra en el paso a paso disponible en Programas necesarios). Ademas una subcarpeta de como realizar las actualizaciones.

## Actualizaciones de Droplets tool
En caso que se le notifique que se encuentra una nueva version de Droplets tool, dirijase a https://github.com/OmarAEM/Scian_Drplets_Omar_Final/tree/main/Instalacion/Droplets%20tool/Actualizaciones para saber como instalar la nueva version de Droplets tool.

## Ejecucion programa Droplets tool
Paso 1: Abrir programa Visual Studio Code, seleccione el boton "File" en la parte superior izquierda y luego seleccione "Open Folder..."
![Captura de pantalla 2023-07-19 030624](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/94a6fc4d-ce74-4a26-98d8-88a06c5b41c3)

Paso 2: Busque y seleccione la carpeta que se descargo con anterioridad (Recordar que el nombre de la carpeta descarga es "Scian_Drplets_Omar_Final"), una vez ya seleccionada la carpeta, aprete el boton "Selecionar carpeta".

<img width="565" alt="Captura de pantalla 2023-07-23 204403" src="https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/f16387ba-47c3-4d0a-8a65-0f6b67099326">



Paso 3: Al lado izquierdo podra visualizar todos los archivos que contiene la carpeta seleccionada anteriormente y una vez identificado, realice doble click sobre el archivo "Droplets.py"
![Captura de pantalla 2023-07-20 141231](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/efe15f89-416b-4abb-ac35-cce83b5d425f)


Paso 4: Ya con el archivo abierto, seleccione el icono en el cuadrado rojo de la imagen que se encuentra en la columna a la izquierda  y luego aprete "Run and Debug"

![Captura de pantalla 2023-07-19 030938](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/9fa36604-9052-4386-bdf6-8a5807b7a2a0)




Paso 4.1: La primera vez que realice el paso 5, aparecera la siguiente captura en la cual usted debe seleccionar "Python File"
![Captura de pantalla 2023-07-19 031000](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/15563407-ba37-40d5-a831-fcb15600d0c2)


Paso 5: Luego del paso 4 o 4.1 segun el caso, aparecera la interfaz donde debe ingresar la densidad de la gota en  "Drop Density [Kg/m3]", la densidad del medio en "Environment Density [Kg/m3]" y el diametro de la aguja en [G] en "Needle Thickness [G]". Una vez introducido estos 3 valores, debe apretar el boton "Load Image".

A modo de ejemplo si se tiene una gota de agua colgando, su entorno es el aire y se usa una aguja con diametro de 0.7 [mm], los parametros a introducir serian:

"Drop Density [Kg/m3]" ---> 997

"Environment Density [Kg/m3]" ---> 1.23

"Needle Thickness [G]" ---> 22

Esto debido a que la densidad del aguja es 997 [Kg/m3], la densidad del aire es 1.23 [Kg/m3] y el diametro de la aguja en [G] es de 22 [G].

![Drop_tool_1](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/a55e6fac-6bf5-4093-8e83-0ae3d429597b)


Paso 6: Una vez apretado el boton mencionado en el paso anterior, dirijase a la carpeta donde esten guardados sus imagenes de gotas colgantes, seleccione la imagen con la que desee trabajar y aprete el boton "Abrir"
![Captura de pantalla 2023-07-19 031313](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/ac2af28e-97cd-4f5d-acb3-7cddb668ba19)


Paso 7: Una vez abierta la imagen, primero debera seleccionar el area donde este la gota, para esto debera generar un rectangulo/cuadrado el cual contenga toda la gota; por lo que primero dirija su mouse al extremo superior izquierdo (imaginando que creara un rectangulo) haga click y mantenga apretado el boton del mouse en ese punto y luego mueva su mouse hasta la esquina inferior derecha para concretar el rectangulo, una vez llegado a ese punto debe de apretar el boton del mouse. Cuando ya finalice la accion antes mencionada, aprete el boton "Enter" de su teclado.
![Captura de pantalla 2023-07-19 031339](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/e572cdbe-25b0-4fd4-91bf-5edc64a98fbf)


Paso 8: Ahora aparecera nuevamente la imagen de la gota, repita el paso 8, pero en esta ocasion seleccione el area de la aguja.
![Captura de pantalla 2023-07-19 031402](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/bc1c3b5b-3561-4e6f-8704-cd30b86fd493)


Paso 9: Una vez finalizado el paso 9, aparecera nuevamente la interfaz del paso 6, esta vez con los parametros "Drop Density [Kg/m3]", "Environment Density [Kg/m3]" y "Needle Thickness [G]" bloqueadas como tambien "Load Image" (con la finalidad de no introducir nuevamente estos valores). Para finalizar esta parte, presione "Quit", generando el cierre de la interfaz.

![Drop_tool_2](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/e00e7485-9d3b-4d8d-81fc-71cfe7452adb)



Paso 10: Ahora podra ver en la terminal (seccion de abajo de la captura de imagen) que se esta indicando que se esta realizando la deteccion de borde de la gota indicando en que proceso esta, una vez finalizado ese proceso, se indica los parametros finales asociados a la tension superficial
![Captura de pantalla 2023-07-19 034058](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/e6c8c5fa-c532-422e-b97e-ea91c55ab93f)


Paso 11: Para ver informacion mas en detalle dirijase a la carpeta "Resultados", si es la primera vez que utiliza Droplets tool se creara un archivo llamado "Result.csv". En el archivo "Result.csv" se guardara toda la informacion relacionada a los datos obtenidos en el procesamiento de la imagen de la gota. Ademas cada vez que utilice Droplets tool se guardara una imagen asociada a los calculos realizados, y este tendra un formato en su nombre de "date_YEAR_MONTH_DAY__hour_HOUR_MINUTE_SECOND" esta nomenclatura indica la fecha y hora que se realizo la obtencion de la tension superficial.

![Drop_tool_3](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/524603b9-b281-4e90-b537-9f24094011c7)

Como "Result.csv" es un archivo .csv, para visualizarlo debera abrir este archivo de la manera que este acostumbrado. A continuacion se muestra como se ve la informacion en texto plano y tambien una visualizacion utilizando el programa excel y configurando internamente este.

![Drop_tool_7](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/9e8fa373-e80a-4d0b-9c42-150bb60fd26a)
![Drop_tool_6](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/bef234ee-cede-4840-be45-01765169ca9e)




Si usted abre la imagen en esta se encontrara informacion de la gota las cuales corresponden a su tension superficial, numero de Bond, numero de Worthington, Parametro de forma y R_O (circunferencia asociada al gota). El numero de Worthington y el parametro de forma corresponden a valores entre 0 y 1 que nos permiten identificar que tan buena es la gota, esto quiere decir que tan acorde es la gota utilizada para determinar su tension superficial.
Ademas se podra visualizar cual fue el contorno de gota utilizado, junto a la circunferencia generada a partir de R_0 utilizado en el calculo de la tension superficial.

![Drop_tool_4](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/adb176d6-2b03-442f-8e5a-c7d46edc92ed)




PROXIMAMENTE
Aun hay que hacer algunos cambiamos de nomenclatura en el nombre de guardado de imagen, como la de incluir nombre de imagen original.
Visualizacion del contorno de la gota detectado y circunferencia+R_0 para realizar procesamiento interno.}
Mejor explicacion de los todos los valores indicados en la imagen final.
Me di cuenta que debo arreglar el numero de Worthington debido a que no esta entregando valores acordes.


