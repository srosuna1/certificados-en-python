[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


Programa para generar certificados adaptado a Venezuela

Requisitos para ejecutar la script

- python 2.7 con los minimos requierimientos instalados
- rst2pdf programa para convertir archivos de texto plano reestructurado a pdf 
	apt-get install rst2pdf en Debian, Ubuntu



------------------------
Descomprimir el archivo tar.gz en un carpeta del sistema cualquiera.

el archivo de imagen para el fondo del certificado debe estar en formato png.

modificar el archivo estilo.style en la linea 17 con el nombre del archivo.png 
que se usara para certificado.

ejecutar 

$ python generar_certificados.py

o bien 

$ sudo chmod a+x generar_certificados.py

y desde el terminal

$ ./generar_certificados.py

---------------

Mirar el proceso como sale en Pantalla_terminal.jpeg

El codigo fuente original pertenece a Ramiro Algozino aka ralgozino
twitter @ralgozino publicado en:
http://ralgozino.wordpress.com/2012/04/20/generando-certificados-diplomas-con-python-rst2pdf/

Modificado para Venezuela por:

Samuel Rojas
aka @srosuna1 
twitter @srosuna1

email: srosuna01@gmail.com samuelrojas01@gmail.com
http://samuelrosuna.net.ve
http://srosuna.wordpress.com


