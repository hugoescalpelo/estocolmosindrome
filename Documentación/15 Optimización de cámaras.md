# Optimización de cámaras

Las cámaras conectadas a [AgentDVR](https://www.ispyconnect.com/) son parte esencial del proyecto [Síndrome de Estocolmo](https://estocolmosindrome.com/), pues realizan el reconocimiento facial que detona el funcionamiento del departamento inteligente. En las notas anteriores se realizó la configuración básica, pero esta podría no ser optima para un funcionamiento fluido. En esta nota se explicará la configuración de optimización para las cámaras.

**Nota**: Antes de ejcutar cualquier configuración lee este documento completo.

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
- Resolución 640x480 para todas las cámaras.
- Conexión WiFi de 2.4GHz
- Cifrado AES-WPA2, el mas común en modems WiFi casa habitación y el predeterminado del ESP32CAM
- Canal WiFi atomático
- De 24 a 32 dispositivos WiFi conectados simultaneamente
- Equipo PC local con las siguientes características
    - Procesador Ryzen 5600x
    - 32GB de RAM DD4 3200MHz
    - Tarjeta gráfica nVidia 1650 4GB VRAM, 16GB memoria compartida
    - Windows 10 Pro compilación 19045.3324
    - Disco interno SSD Velocidad R/W 3500MBps/3000MBps
    - Almacenamiento externo HDD Seagate Skyhawk dual 8TB RAID 0
- Agenet DVR v4.4.9.0
- CodeProject.AI 2.1.9-Beta
- Departamento de 56m2. Este dato es importante porque garantiza una distancia no mayor a 5 metros entre cada cámara y el modem, lo que tiene influencia directa en la intesidad de la señal que recibe cada cámara.

**Nota**: Estas configuraciones sólo comprenden la optimización del streaming, es necesario que sigas leyendo la documentación para configurar la grabación y la optimización de detección de rostros.
    
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
    
    ```
    :network-caching=128
    :live-caching=10
    :file-caching=10
    ```
    Deja las demás configuraciones con el valor predeterminado.
5. En el menú Video Source, en la sección FFMPEG configura lo siguiente: Buffer = 128, RTSP Mode = Auto, Prefer TCP = On, Scale Mode = Fast Bilinear. Deja las demás configuraciones con el valor predeterminado.

Estas configuraciones deben realziarse para cada cámara interior.

### Configuración de cámara exterior

Las siguientes configuraciones son únicamente para la cámara que apunta a la mirilla de la puerta. Todas las configuraciones son las mismas excepto de las correspondientes al número 4 y 5. Los cambios se muestran a continuación.

4. En el menú Video Source seleccióna la sección Advanced. Configura lo siguiente: Decode GPU = 0 para configuraciones de PC con procesador sin video integrado y con tarjeta gráfica dedicada, el numero correspondiente a la tarjeta gráfica que se desea usar para equipos con multiples tarjetas gráficas ya sea integradas o dedicadas. Puedes conocer el índice de la tarjeta gráfica desde el administrador de tareas de Windows en la sección Rendimiento. GPU Decoder = cuda, Basic Authentication = On, Use HTTP1.0 = Off, Prevent JPEG Cache = On, User Agent = Mozilla/5.0, Width = 1280, Height = 720, Connection Timeout = 8000, Recconect Interval = 0, Reconnect Strategy = Immediate, VLC Options = 
    
    ```
    :network-caching=256
    :live-caching=10
    :file-caching=10
    ```
    Deja las demás configuraciones con el valor predeterminado.
5. En el menú Video Source, en la sección FFMPEG configura lo siguiente: Buffer = 256, RTSP Mode = Auto, Prefer TCP = On, Scale Mode = Fast Bilinear. Deja las demás configuraciones con el valor predeterminado.

### Configuraciones de Detector - Cámara principal

Las siguientes configuraciones son para la cámara principal, la que se encuentra en el escritorio y tiene como propósito realizar el conteo de horas trabajadas.

1. Haz clic derecho en la cámara y selecciona la opción Edit
2. Dirígete a la sección Detector y configura lo siguiente: Enabled = On, Detector = Objects, Overlay = On, Timeout = 2.
3. Haz clic en el boton de configuraciones del menú Detector y configura lo siguiente: Frame Size = Medium, Detect Inteval = 300, Widht limits = 1, 80, Height limits = 1, 80, Use GPU = On, File = Face, Alert Condition = More Than, Alert Number = 0.

**Nota**: Estas configuraciones deben ser ajustadas de acuerdo a las capacidades de tu eqipo PC.

## Configuraciones de Detector - Cámaras interiores

Esta congiguración es para el resto de las cámaras interiores y tiene como propósito detectar el movimiento para iniciar reconocimiento facial y grabaciones.

1. Haz clic derecho en la cámara y selecciona la opción Edit
2. Dirígete a la sección Detector y configura lo siguiente: Enabled = On, Detector = Simple, Overlay = On, Timeout = 3.
3. Haz clic en el boton de configuraciones del menú Detector y configura lo siguiente: Sensitivity = 200, 100, Gain = 10.
4. Haz clic en el menú Advanced: Analyzer = CNT (Fast), Frame Size = Medium, Tracker = CSRT, Max Objects = 3, Detect Interval = 300, Track Interval = 200, Pixel Stability = 1, 40, Use History = Off, Paralel Process = On, Tracking TimeOut = 3, Movement Timeout = 3.

**Nota**: Estas configuraciones deben ser ajustadas de acuerdo a las capacidades de tu eqipo PC.

## Configuraciones Extra

Esta nota sólo comprende la configuración de optimización del streaming y uso de recursos del sistema. Adicionalmente se requiere una serie de configuraciones extra, las cuales serán detalladas en las notas siguientes

## Recomendaciones de uso de recursos.

El sistema configurado es intensivo en recursos de hardware para el equipo PC que sostiene todos los sistemas. Es importante que consideres los siguientes consejos para evitar daños a tu equipo PC o un incremento exagerado en el consumo eléctrico.

**Nota**: Las configuraciones actuales son recomendados para un equipo de capacidades medias bajas como se menciona al inicio de este documento.

**Equipo de capacidades bajas**

Se considera como equipo de capacidades bajas configuraciones similares a las siguientes:

- Procesador Core i3 modelo 2020 o equivalente
- 16 GB de RAM DDR3
- Tarjeta gráfica nVidia 1060 o similar
- Almacenamiento HDD no especializado

**Equipo de capacidades altas**

Se considera como equipo de capacidades altas configuraciones similares o superiores a las siguientes:

- Procesador Core i7 2020 o superior
- 32 GB de RAM DDR4 3200MHz o superior
- Tarjeta gráfica nVidia 2070 o superior
- Almacenamiento SSD mayor a 3500MBps/3000MBps R/W
- Almacenamiento HDD grado servidor surveillance

**Configuraciones recomendadas**

Para equipos de capacidades bajas se recomienda cambiar los Frame Size a Small, para equipos de capacidades altas se recomienda Frame Size a Large.

Otra elemento que influye en la fluidez del sistema, es la resolución de Max Stream Size en la categoría Playback de las configuraciones del servidor. Puede ser configurado en 1080p para equipos de capacidades altas y medias.

**Consideraciones de diseño**

Para evitar el daño al equipo que contiene todos los servidores del proeycto se recomienda refrigeración liquida de al menos doble ventilador para equipos de capacidades altas y de ventilador simple para equipos de capacidades medias y bajas.

Para una correcta refrigeración de la tarjeta gráfica se recomienda al menos un disipador de doble ventilador.

Para reducir el consumo se recomienda una fuente de alimentación de capacidad Bronze 80 con una capacidad al menos 40% mayor al consumo general de potencia de todos los dispositivos del equipo PC.

## Referencias

Puedes consultar los siguientes video para mas detalles

- [Lista de reproducción del proyecto](https://www.youtube.com/watch?v=_F277YnKmog&list=PLm5nY_UPV5A7sAQCkPrWafyoOXLW3rvgx&pp=iAQB)
- [Tutorial: Desarrollo de Proyecto 009 - Instalando Agent DVR y Ejemplo con ESP32CAM](https://youtu.be/3nzBiaU9kvc)
- [Tutorial: Desarrollo de proyecto 012 - Camera Web Server con ESP32CAM](https://youtu.be/hWVYICauV34)
- [Tutorial: Desarrollo de proyecto 013 - Servidor de CodeProject.AI para reconocimiento facial](https://youtu.be/_mnCV-Gkf0c)
- [Desarrollo de proyeto 014 - Configuración de detección de rostros con AgentDVR y CodeProyect.AI](https://youtu.be/_YfmRRuaYoE)