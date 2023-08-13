# Optimización de cámaras

Las cámaras conectadas a [AgentDVR](https://www.ispyconnect.com/) son parte esencial del proyecto [Síndrome de Estocolmo](https://estocolmosindrome.com/), pues realizan el reconocimiento facial que detona el funcionamiento del departamento inteligente. En las notas anteriores se realizó la configuración básica, pero esta podría no ser optima para un funcionamiento fluido. En esta nota se explicará la configuración de optimización para las cámaras.

**Nota**: Antes de ejcutar cualquier configuración de este documento.

## Requisitos

- Windows
- Docker Desktop. La versión de Windows ya incluye docker-compose (opcional)
- WSL2
- Ubuntu (WSL2)
- Activar la integración de Ubuntu en Docker Desktop
- AgentDVR en [localhost:8090](http://localhost:8090/)
- CodeProject.AI with GPU en [localhost:32168](http://localhost:32168/)
- Cámaras ESP32CAM con el programa de **Camera Web Server** modificado y cargado.
- Sistema AgentDVR con cámaras agregadas.

## Aclances

Antes de explicar las configuraciones necesarias, es importante establecer las condiciones bajo las cuales los siguientes consejos funcionarán.

Estas configuraciones fueron probadas bajo las siguientes condiciones:

- Cámaras ESP32CAM con el [programa CameraWebServer](https://github.com/hugoescalpelo/estocolmosindrome/tree/main/ESP32CAM/ESP32CAM-videoserver-static-ip-autorestart-2023) de este repositorio
- Resolución 640x480 para todas las cámaras interiores
- Resolución 1280x720 para la cámara de la mirilla que apunta al exterior del departamento
- Conexión WiFi de 2.4GHz
- Cifrado AES-WPA2, el mas común en modems WiFi casa habitación y el predeterminado del ESP32CAM
- Canal WiFi atomático
- De 24 a 32 dispositivos WiFi conectados simultaneamente
- Equipo PC local con las siguientes características
    - Procesador Ryzen 5600x
    - 32GB de RAM
    - Tarjeta gráfica nVidia 1650 4GB VRAM, 16GB memoria compartida
    - Windows 10 Pro compilación 19045.3324
- Agenet DVR v4.4.9.0
- CodeProject.AI 2.1.9-Beta
    
## Instrucciones

Este instructivo explica las configuraciones de optimización en AgentDVR para mejorar la latencia del streaming de las cámaras ESP32CAM y el reconocimiento de imagen asociado a ellas.

### Configuración de AgentDVR

1. Accede al sitio local de configuración de [AgentDVR](http://localhost:8090/)
2. Accede a las configuraciones del servidor principal haciendo clic en botón de configuración de la esquina superior izquierda, luego haz clic en el botón Settings del menú Configuration
3. En la sección General, el valor MaxCPU = 60
4. En la sección AI Server, haz clic en el botón de configuración del servidor
    - En el menú Edit cofigura los siguientes valores: Timeout = 3, Retry Delay = 3.
    - En el menú Settings busca el módulo Face Recognition y en configuraicón configura lo siguiente: Enable = On, GPU = On, Process = 2, Start Delay = 0, Mode = Medium, Use CUDA = Yes. El resto de las configuraciones deberán dejarse con los valores predeterminados
5. En la sección Playback configura lo siguiente: Max Stream Size = 720p, Maximum MJPG Size = 1280x720, Default MJPG Size = 640x480, Codec = H264/MP4/MP3, Video FPS = 10, Center images = On, Use GPU = On. Dejar el resto de configuraciones con sus valores rpedeterminados

### Configuración de cámaras interiores

La siguientes configuraciones son para las cámaras interiores, es decir, todas excepto la cámara de la mirilla externa.

1. Haz clic derecho en la cámara y selecciona la opción Edit
2. En la sección General configura lo siguiente: Decoder = GPU, Max Framerate = 10.
3. En la sección General, en la sección Source Type haz clic en el boton de configuraicónes. Esto abre el menú Video Source.
4. En el menú Video Source seleccióna la sección Advanced. Configura lo siguiente: Decode GPU = 0 para configuraciones de PC con procesador sin video integrado y con tarjeta gráfica dedicada, el numero correspondiente a la tarjeta gráfica que se desea usar para equipos con multiples tarjetas gráficas ya sea integradas o dedicadas. Puedes conocer el índice de la tarjeta gráfica desde el administrador de tareas de Windows en la sección Rendimiento. GPU Decoder = cuda, Basic Authentication = On, Use HTTP1.0 = Off, Prevent JPEG Cache = On, User Agent = Mozilla/5.0, Width = 640, Height = 0, Connection Timeout = 8000, Recconect Interval = 0, Reconnect Strategy = Immediate, VLC Options = 
    
    :network-caching=128
    :live-caching=10
    :file-caching=10

## Agregar un rostro a CodeProject.AI

Para realizar esta configuración, requieres de AgentDVR funcionando, el servidor de CodeProject.AI funcionando, tener agregada al menos una cámara, haber realizado las configuraciones anteriores.

Para poder configurar esta sección, haz clic en el boton de configuración de la sección Edit Faces que contiene 3 puntos [...].

En esta sección podrás agregar nuevos rostros al servidor de CodeProject.AI para que los diferencíe y los detecte:

1. Para agregar un rostro, haz clic en el boton Add.
2. Escribe el nombre de la persona a agregar. **Nota** Es recomendable agregar multiples fotos de la misma persona, en distintos ángulos y situaciones de contraste. Si ya has agregado previamente a una persona, escribe el nombre exactamente igual que la vez anterior, para evitar confusiones en el sistema. 
3. Una vez que hallas escrito el nombre, puedes seleccionar la opción Upload o Use Cámera. A continuación se describen las diferencias.
    - Upload. Puede seleccionar cualquier foto de tu disco duro.
    - Use Cámera. Toma una foto actual con la cámara actual. Se recomienda estár frente a la cámara. La fotogrfía se tomará en el momento en el que hagas clic en el botón, así que preparate.

**Notas**: Se recomienda agregar fotografías bajo los siguientes criterios:

- Caso optimo: Fotografias de rostro completo, centrado, bien iluminado, con excelente contraste y de resoluciones que varíen entre 640x480 px a 2MPx.
- Caso real: Agregar fotografías reales de las cámaras, en buenas y malas condiciones de ilumincación, con distintos angulos de detección, fuera de lo ideal, pero conservando una vista clara del rostro.

**Otras observaciones**
- Este algoritmo empieza a dar resultados favorables a partir de 5 fotos.
- Estimo que este algoritmo se vuelve un 3% a 5% mas eficiente con cada mes de funcionamiento continuo.¨

## Uso

Si has configurado todo de forma correcta, podrás ver resaltado el nombre del rostro que has agregado junto a un porcentaje de certeza cada intervalo que hayas configurado.

![]()

## Importante

Este algormito es intensivo en consumo energético. Eso significa que el uso constante de esta función en multiples cámaras de manera continua puede multiplicar varais veces el consumo energético del servidor utilizado. Si bien, el nivel de uso de recursos sube un porcentaje muy pequeño en mi equipo, el costo del recibo de energía eléctrica se mutiplico por 2 cada mes durante 6 meses. **Usarse con precaución**.

## Optimización

En el siguiente documento se describirán una serie de guias básicas para mejorar el rendimiento del servidor de AgentDVR y CodeProject.AI. Las configuraciones de este documento deben contextualizarse a las capacidades del servidor que lo ejecuta y representan únicamente una guía para comprobar el funcionamiento. Estas configuraciones no se recomiendan para producción.

## Referencias

- [Lista de reproducción del proyecto](https://www.youtube.com/watch?v=_F277YnKmog&list=PLm5nY_UPV5A7sAQCkPrWafyoOXLW3rvgx&pp=iAQB)
- [Tutorial: Desarrollo de Proyecto 009 - Instalando Agent DVR y Ejemplo con ESP32CAM](https://youtu.be/3nzBiaU9kvc)
- [Tutorial: Desarrollo de proyecto 012 - Camera Web Server con ESP32CAM](https://youtu.be/hWVYICauV34)
- [Tutorial: Desarrollo de proyecto 013 - Servidor de CodeProject.AI para reconocimiento facial](https://youtu.be/_mnCV-Gkf0c)
