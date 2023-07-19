# Scian_Droplets_Omar_Final
## 1. Descarga e instalacion de programas (si es que no los tiene)
Instalar Python desde https://www.python.org/downloads/
![Python](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/c98f0065-2bd2-4fa8-9da6-79e1b781836a)

Instalar Visual Studio Code desde https://code.visualstudio.com/download
![Vscode](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/54594746-a6f4-448a-b3e1-08244c00b94e)

Instalar librerias necesarias
Para poder instalar las librerias necesarias, dirijase al buscador de windows y escriba "cmd", luego abra el programa "Simbolos del sistema" y buscar ruta donde se encuentra instalado python
![Captura de pantalla 2023-07-19 082558](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/0fa25398-823b-44ca-853a-62d4e9661b35)

Ahora se debe buscar la ruta donde se encuentra instalado python
![instalar_librerias](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/d867520c-2e19-48be-949b-3f945e93fd0a)
Para las librerias se debe escribir y apretar enter cada vez que se escriba un pip install
pip install opencv-python

pip install scikit-image

pip install shapely

pip install pandas

pip install xlsxwriter

pip install descartes

## 2. Creacion de carpetas a utilizar
Primero hay que descargar el programa Droplets desde https://github.com/OmarAEM/Scian-Droplets-Omar, una vez en la pagina, apretar el boton "Code" y posteriormente "Download ZIP", abrir archivo zip y extraer la carpeta "Scian-Droplets-Omar-main" en su computador (puede ser en el escritorio o en una carpeta que tenga destinada para trabajar con droplets
![Captura de pantalla 2023-07-19 083959](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/0386a760-6c28-4248-9035-fd2a10b13363)

Lo segundo es crear una carpeta donde guardara las imagenes de las gotas (si ya posee una omita esta parte), en el lugar que mas le acomode en su computador.
Luego cree una carpeta "Resultados" dentro de la carpeta donde guarda la imagenes, esta carpeta se utilizara para registrar los resultados obtenidos al calcular la tensio interfacial.


## 3. Ejecutar programa Droplets
PASO 1: Abrir programa Visual Studio Code, seleccione el boton "File" en la parte superior izquierda y luego seleccione "Open Folder..."
![Captura de pantalla 2023-07-19 030624](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/06716bbe-9910-48c5-8b87-84418970192d)

Paso 2: Busque y seleccione la carpeta que se extrajo del archivo zip descargado del repositorio en Github, una vez ya seleccionada la carpeta, aprete el boton "Seleecionar carpeta"
![Captura de pantalla 2023-07-19 030741](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/ab5123bc-4a5e-481b-bfc6-51ab478faa5f)

Paso 3: Aprete "Yes, I trust the authors"

![Captura de pantalla 2023-07-19 030806](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/8aa5dbc3-1e89-4356-aa61-350b9bbf93b2)

Paso 4: Al lado izquierdo podra visualizar todos los archivos que contiene la carpeta seleccionada anteriormente y una vez identificado, realice doble click sobre el archivo "Droplets.py"
![Captura de pantalla 2023-07-19 034004](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/51952393-ec0b-42f0-b7bf-66b1b02aa51b)

Paso 5: Ya con el archivo abierto, seleccione el cuarto icono de la columna a la izquierda (aquel que posee una linea azul a su costado) y luego aprete "Run and Debug"

![Captura de pantalla 2023-07-19 030938](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/df0085af-9292-4137-81dd-a8190c4e6ad6)

Paso 5.1: La primera vez que realice el paso 5, aparecera la siguiente captura en la cual usted debe seleccionar "Python File"
![Captura de pantalla 2023-07-19 031000](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/ed028550-0c72-49a6-9df8-cb34591e8f2a)

Paso 6: Luego del paso 5 o 5.1 segun el caso, aparecera la interfaz donde debe ingresar la densidad de la gota, la densidad del medio y el diametro de la aguja en [G]. Una vez introducido estos 3 valores, debe apretar el boton "Open Image"
![Captura de pantalla 2023-07-19 031252](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/06964daa-3753-40c5-b3a0-82690a5c485d)

Paso 7: Una vez apretado el boton mencionado en el paso anterior, dirijase a la carpeta donde esten guardados sus imagenes de gotas colgantes, seleccione la imagen con la que desee trabajar y aprete el boton "Abrir"
![Captura de pantalla 2023-07-19 031313](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/9b917770-2438-4b2b-92b0-e026cfee7220)

Paso 8: Una vez abierta la imagen, primero debera seleccionar el area donde este la gota, para esto debera generar un rectangulo/cuadrado el cual contenga toda la gota; por lo que primero dirija su mouse al extremo superior izquierdo (imaginando que creara un rectangulo) haga click y mantenga apretado el boton del mouse en ese punto y luego mueva su mouse hasta la esquina inferior derecha para concretar el rectangulo, una vez llegado a ese punto debe de apretar el boton del mouse. Cuando ya finalice la accion antes mencionada, aprete el boton "Enter" de su teclado.
![Captura de pantalla 2023-07-19 031339](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/076c6a6f-5eab-4b4e-9402-51fae62a85c8)

Paso 9: Ahora aparecera nuevamente la imagen de la gota, repita el paso 8, pero en esta ocasion seleccione el area de la aguja.
![Captura de pantalla 2023-07-19 031402](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/9d95e7be-12ee-452e-b2c3-a49c87c42b91)

Paso 10: Una vez finalizado el paso 9, aparecera nuevamente la interfaz del paso 6, en esta ocasion cierre la ventana con la cruz de la esquina superior derecha

![Captura de pantalla 2023-07-19 031252](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/06964daa-3753-40c5-b3a0-82690a5c485d)

Paso 11: Ahora podra ver en la terminal (seccion de abajo de la captura de imagen) que se esta indicando que se esta realizando la deteccion de borde de la gota indicando en que proceso esta, una vez finalizado ese proceso, se indica los parametros finales asociados a la tension superficial
![Captura de pantalla 2023-07-19 034058](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/72cd7015-513f-42d0-bf22-27695193b46c)

Paso 12: Si lo desea puede dirijirse a la carpeta "Resultados" que se creo en un comienzo en su carpeta donde guardara la imagenes de la gota; y dentro de esta carpeta podra encontrar todas las imagenes de gotas analizadas y tendran como nombre su tension superficial calculada.
![Captura de pantalla 2023-07-19 041508](https://github.com/OmarAEM/Scian_Drplets_Omar_Final/assets/115668053/b11840b5-58ce-48de-bad8-9188e1c39bcb)
