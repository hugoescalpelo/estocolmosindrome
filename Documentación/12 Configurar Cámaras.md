# Configuración del ESP32CAM como cámara de seguridad

## Requisitos

1. [Arduino IDE 1.8 o superior](https://www.arduino.cc/en/software)
2. [Bibliotecas Espressif para ESP32CAM y Arduino IDE](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html)
3. [Python3](https://www.python.org/downloads/)
4. [PIP](https://pypi.org/project/pip/)
5. ESP32CAM AI-Thinker
6. Cámara OV2640
7. FTDI level adapter

**Nota**: Para realizar esta configuración se usó una máquina virtual con Ubuntu 22.04LTS, pero puede realizarse en cualquier sistema operativo. Puedes consultar las instrucciones para otros sistemas operativos en la [documentación oficial de Espressif](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html).

## Prepara el entorno

1. Instala Arduino IDE 1.8 o superior
- Opción 1: Abre la tienda de aplicaciones de Ubuntu e instala Arduino.
- Opción 2: Ejecuta el comando `sudo apt install arduino`
- Opción 3: Descarga el archivo .zip de [arduino.cc](https://www.arduino.cc/en/software), extrae los archivos y ejecuta arduino.
- Opción 4. Descarga el archivo AppImage de [arduino.cc](https://www.arduino.cc/en/software),  [configuralo como ejecutable](https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing) y ejectua Arduino.
2. Agrega tarjetas adicionales al administrador de tarjetas
- Haz clic en archivo y preferencias.
- En la opción "Additional Boards" pega el siguiente enlace `https://espressif.github.io/arduino-esp32/package_esp32_index.json`
3. Agrega ES32 desde el administrador de tarjetas
- Haz clic en Herramientas > Tarjeta > Administrador de tarjetas.
- Busca `esp32`.
- En la busqueda aparecerán las tarjetas .ESP32, haz clic en el boton instalar
4. Reinicia Arduino
5. Selecciona la tarjeta AI-Thinker
- Haz clic en Herraimentas.
- Haz clic en el menú Tarjetas.
- Selecciona la opción esp32
- Busca la tarjeta AI-Thinker. **Nota**: Las tarjetas no se encuentran por orden alfabético. La tarjeta se encuentra cerca alrededor del 2/3 de la lista.
6. Configura los Drivers del ESP32CAM. Ejecuta los siguientes comandos. Estos comandos deben ejecutarse con Arduino IDE cerrado

```
sudo usermod -a -G dialout $USER
sudo apt-get install git
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip3 install pyserial
mkdir -p ~/Arduino/hardware/espressif
cd ~/Arduino/hardware/espressif
git clone https://github.com/espressif/arduino-esp32.git esp32
cd esp32/tools
python3 get.py
```

A continuación se muestra el circuito a realizar para programar el modulo ESP32CAM y posteriormente las configuraciones de la tarjeta AI-Thinker.

7. Realiza el circuito para programar el ESP32CAM.
- Realiza el siguiente circuito para programar el ESP32CAM.

![](https://github.com/hugoescalpelo/estocolmosindrome/blob/main/Circuitos/01%20Circuito%20para%20programar%20ESP32CAM.png?raw=true)
![](https://github.com/hugoescalpelo/estocolmosindrome/blob/main/Imagenes/001%20Circuito%20c%C3%A1mara.png?raw=true)


**Nota**: En esta imagen se muestra el circuito que configura el esp32CAM en modo programador. Se puede identificar porque el puerto GPIO0 está conectado con GND. Para probar el circuito, será necesario desconectar estos pines.
8. Conecta el circuito a tu computadora
- Conecta el cable USB mini al FTDI.
- Si configuraste Arduino en tu sistema operativo nativo, podras realizar la selección del puerto usb para programar el ESP32CAM en el siguiente paso sin problema
- Si usas una máquina virtual, reenvia el FTDI a de tu sistema operativo anfitrion a tu sistema operativo virtualizado en este momento. Para hacerlo en Virtual Box, haz clic en el boton Dispositivos > USB y selecciona el FTDI. Realiza este paso las veces que sea necesario para que el FTDI aparezca en tu sistema operativo virtualizado.
9. Selecciona el puerto USB para programar el ESP32CAM
- Haz clic en el boton Herramientas de la IDE de Arduino y selecciona el puerto USB de tu ESP32CAM. 
- Puede aparecer nombrado como FTDI, CH430, Quing Hong, Etc.
- En Windows puede ser nombrado como `COM3` u otro puerto COM.
- En Linux y Mac, puede ser nombrado como `dev/ttyUSB0`
10. Deja el resto de las configuraciones con su valor predeterminado

## Carga el programa a cada cámara que vayas a agregar al proyecto

Este proyecto usa 6 cámaras debido a las limitaciones del espacio en el que fue desarrollado originalmente, pero puedes agregar o quitar cámaras. 

Deberás agregar tu nombre de red y contraseña al programa para que cada ESP32CAM pueda conectarse a tu red local.

El programa está configurado para usar IP estática, por lo que será necesario que cambies la IP a cada cámara que programes.

A continuación se muestra la lista de IPs del proyecto original. Nota que la estructura de IP de tu ruter puede ser diferente a la mia.

- 192.168.15.110 Escritorio
- 192.168.15.111 Puerta
- 192.168.15.112 Mirilla
- 192.168.15.113 Cocina
- 192.168.15.114 Sala
- 192.168.15.115 Lavamanos

A continuación se muestran las instrucciones para cargar el programa. Nota: Debes haver configurado previamente la IDE de Arduino para trabajar con el ESP32CAM.

1. Abre el programa `ESP32CAM-videoserver-static-ip-autorestart-2023.ino`ubicado en la carpeta ESP32CAM del repositorio
2. Configura el Puerto USB
- Haz clic en el menu Herramientas
- En la sección puerto, selecciona el puerto donde está conectado el FTDI.
3. Escribe el nombre de red y contraseña en la linea 34 y 35. Verifica que espacios, simbolos, mayusculas y minusculas coincidan tanto en nombre como en contraseña.
4. Escribe una IP fija diferente para cada cámara que vayas a agregar.
- Selecciona una IP que no este usada previamente.
- Puedes seleccionar cualquier valor final de IP de 0 a 254.
- Puedes consultar las IPs previamente usadas en la configuración de tu router o con la herramienta wNetWatcher o similares.
5. Haz clic en el boton Upload de la IDE de Arduino para cargar el programa
- Nota: el ESP32CAM deberá estar conectado en modo programador para que sea posible cargar el prorgama. Puedes identificarlo comprobando que el pin GPIO0 esté conectado a GND.

## Comprueba el funcionamiento de cada cámara

Puedes comprobar el funcionamiento de cada cámara con los siguientes pasos.

- Para que el ESP32CAM deje de estar en modo pogramador y esté en modo funcionamiento, desconecta el pine GPIO0 de GND y reinicia el micro controlador.
- Si aun tienes conectado el micro controlador por USB, podrás abrir el monitor serial y comprobar que se ha realizado la conexión a WiFi y ver la IP a la que se ha conectado cada cámara luego de presionar el boton reset del micro controlador.
- Visita la IP de cada cámara, podrás ver la página de configuración de la cámara. Para ver el video, haz clic en el boton Start Streaming. No es encesario que realices ninguna configuración manual aqui. Las configuraciones necesarias se realizaran via API en NodeRed.

![](https://github.com/hugoescalpelo/estocolmosindrome/blob/main/Imagenes/002%20Base.png?raw=true)
![](https://github.com/hugoescalpelo/estocolmosindrome/blob/main/Imagenes/003%20Base%202.png?raw=true)
![](https://github.com/hugoescalpelo/estocolmosindrome/blob/main/Imagenes/004%20Base%203.png?raw=true)
![](https://github.com/hugoescalpelo/estocolmosindrome/blob/main/Imagenes/005%20Adaptador.png?raw=true)

## Uso recomendado

Para operar las cámaras, deben recibir 5V de forma constante. Para esto puedes usar una base para ESP32CAM, un banco de energía USB y un adaptador de corriente o cargador de celular de 5V a 1A. A continuación se muestran multiples opciones.

![](https://github.com/hugoescalpelo/estocolmosindrome/blob/main/Imagenes/006%20Camara%20funcionando.jpg?raw=true)