# Temperature Sensor Emulator

Aplicación para emular un sensor de temperatura y realizar puruebas en  
etapa de desarrollo.

## Prerrequisitos

≧◠‿◠≦

1. Manejo de terminal y línea de comandos.
2. Instala Eclipse Mosquitto.
3. Crea un archivo mosquitto.conf en la ruta C:\ con la siguiente configuración.
   ```
   listener 1883
   protocol  mqtt

   listener 8080
   protocol websockets

   allow_anonymous true
   ```
4. Abre una terminal en la carpeta de istalación.
5. Ejecuta el comando `./mosquitto.exe -c C:\mosquitto.conf -v` para  
   iniciar el broker.
6. Instala Python 3.11 y PIP como herramienta de línea de comandos.
7. Conocimientos en entornos virtuales para Python.
8. Requieres del siguiente repositorio
   [sensor-monitoring](https://github.com/miniscandal/sensor-monitoring) como aplicación web para  
   monitoreo en tiempo real.

## Instalación

≧◠‿◠≦

1. Clona el repositorio en tu computadora.  
   `git clone https://github.com/miniscandal/temperature-sensor-emulator`  
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el comando `pip install -r requirements.txt` para instalar  
   los paquetes requeridos.
4. Ejecuta el comando `.\venv\Scripts\activate` para activar el entorno virtual.
5. Ejecuta el comando python .\src\sensor.py -i 1 -s 1 para inicar un emulador.

## Uso

≧◠‿◠≦

<img src="./docs/pictures/terminal-capture-01-min.png" width="540">

## Tecnologías
![Terminal](https://img.shields.io/badge/Terminal-%23474745.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Mosquitto](https://img.shields.io/badge/Mosquitto-%233C5280.svg?style=for-the-badge)
![MQTT](https://img.shields.io/badge/MQTT-%23007ACC.svg?style=for-the-badge&logo=MQTT&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-%2348494a.svg?style=for-the-badge)

## Aprendizajes

≧◠‿◠≦

Implementación de un entorno virtual aislado para evitar conflictos  
de dependencias y prevenir la contaminación del sistema.

Integración de Python para realizar pruebas en aplicaciones web en tiempo real.

## Documentación

≧◠‿◠≦

* [Python](https://www.python.org/)
* [Mosquitto](https://mosquitto.org/)

## Licencia

≧◠‿◠≦

Este proyecto está bajo la Licencia MIT - mira el archivo LICENSE para detalles.