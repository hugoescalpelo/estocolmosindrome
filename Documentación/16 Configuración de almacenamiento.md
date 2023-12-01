# Configuración de almacenamiento

En [AgentDVR](https://www.ispyconnect.com/) la configuración de almacenamiento incluye el guardado de fotos, grabaciones y audios,los cuales son parte esencial del proyecto [Síndrome de Estocolmo](https://estocolmosindrome.com/), pues son uno de los productos que se pueden comprar en el sitio del proyecto por dinero real o a cambio de información personal. En las notas anteriores no se contempla, por lo que aquí se muestra el proceso completo.

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
- Resolución 640x480 para todas las cámaras interiores
- Resolución 1280x720 para la cámara de la mirilla que apunta al exterior del departamento
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
    - Almacenamiento externo HDD Seagate Skyhawk dual 4TB RAID 0
- Agenet DVR v4.4.9.0
- CodeProject.AI 2.1.9-Beta
- Departamento de 56m2. Este dato es importante porque limita la cantidad de camaras que forman parte del proyecto. Para mas cámaras es necesario mas espacio de almacenamiento.
- Esta guía explica como configurar almacenamiento local, para almacenamiento remoto, es necesario adquirir una licencia de AgentDVR.

**Nota**: Estas configuraciones sólo comprenden la configuración de almacenamiento mas eficiente. Si deseas mejorar la calidad de grabación, como la resolución de las cámaras, deberás contar con una mejor red y medir constantemente el uso de espacio que consumes diaramente para establecer un ciclo de borrado.
    
## Instrucciones

Este instructivo explica las configuraciones de optimización en AgentDVR para realizar la grabación continua de 6 cámaras y un micrófono ambiental.

### Configuración de AgentDVR

1. Haz clic en el boton de configuración del servidor en la esquina superior derecha del dashboard de [AgentDVR](http://localhost:8090/#Live).
2. Haz clic en el boton **Settings** de la sección **Configuration**.
3. Haz clic en el boton **General** en la esquina superior derecha del cuadro de dialogo de configuración y selecciona la opción **Storage**.
4. Haz clic en el botón **...** de la sección _Configure_.
5. Si no tienes previamente configurado un sistema de almacenamiento local, haz clic en el botón **+**, si lo tienes, haz clic en el boton editar del almacenamiento local que ya tienes.
6. En la sección **Location** escribe la ruta de la carpeta de almacenamiento local donde deseas guardar las fotos, imágenes y grabaciones de AgentDVR.
    - Windows: Puedes obtener esta ruta abriendo un explorador de archivos y luego dirigiendote a la caperta donde deseas guardar todo; luego haz clic en la barra de direcciones y copia la ruta. Puedes seleccionar un disco externo o almacenamiento secundario. En mi caso, he creado una carpeta llamada iSpy en mi disco _F:_ el cual es mi arreglo RAID0 de 8TB. También puedes escribir manualmente la ruta, solo recuerda que en Windows debes usar diagonal invertida (\\). Si tienes problemas, copia el siguiente ejemplo: `F:\iSpy\` y ajusta la direccion de tu carpeta de almacenamiento. Consulta el enlace del video al final de este documento.
    - Linux: Si usas linux posiblemente sabes escribir rutas de archivos ;) Si no, misma situación, solo que usas diagonales normales (/). Por ejemplo `/home/user/iSpy/`
7. Activa el almacenamiento activando el boton inmediatamente debajo del cuadro de texto de la ruta de almacenamiento.

### Storage Management

La adminsitración de almacenamiento determina cuanto tiempo permanecen los archivos en la carpeta principal, para dar contexto, existe otra sección llamada Archivo, donde se guardará todo después de cierto tiempo. Asegurate de que esta opción esté activada con el switch al inicio de esta sección.

- **Max Size**: Es el tamaño máximo de almacenamiento en MegaBytes de la carpeta que guarda el contenido antes de archivarlo. Escribe un valor de 1000MB.
- **Max Age**: Es el tiempo máximo que fotos y videos pasarán en la carpeta principal. Pasado este tiempo, los archivos se moverán a la carpeta de Archivo. Se recomienda un máximo de 72h.
- **Delete to recicle bin**. Si activas esta opción, fotos y videos se borrarán en lugar de archivarse. Esta opción debe estar desactivada. Puedes activar esta opción en caso de que tengas poco espacio de almacenamiento, en cuyo caso, solo se almacenará un maximo de 1000MB y los archivos solo se guardarán en disco un máximo de 72h. Si usas la configuración de borrado, tal vez quieras cambiar las configuraciones de **Max Size** y **Max Age**.

### Archivado

La sección de archivado mueve los archivos a una carpeta para su almacenamiento. La idea es que en esta carpeta se guardan los archivos que no se van a consultar. Esto es conveniente para vincular a la tienda de información personal en el proyecto del sitio dado que las carpetas activas están separadas por cámara y por fecha.

- **Archived location**: Es la carpeta de videos archivados, por ejemplo `F:\iSpy\archive\`
- **Photos location**: Es la carpeta de fotos archivdas, por ejemplo: `F:\iSpy\photo`
- **Index archived files**: Permite ver los elementos archivados en la interfaz de _AgentDVR_. Esta opción debe dejarse desactivada.
- **Archive Expires**: La cantidad de días tras la cual se borran los elementos del archivo. Esta configuración se deja en 0 para no borrar nada.

### Network Storage
Esta sección permite configurar un FTP o un almacenamiento en la nube, pero para ello se requiere comprar la licencia de _AgentDVR_ por lo que no se cubre en este documento.

Finalmente, acepta todas las configuraciones.

### Storage Interval
Esta configuración indica cada cuantos minutos se realiza la administración de archivos. Se recomienda 1440 minutos (24h) para equipos encendidos continuamiente, 360 minutos (6h) para equipos encendidos diariamente y 60 minutos (1h) para equipos encendidos solo en horario laboral.

## Configuración de cámara
Adicionalmente, cada cámara debe ser configurada para el almacenamiento de fotos y video.

### Almacenamiento de fotos
1. Haz clic derecho en la cámara que deseas configurar y selecciona la opción **Edit**.
2. Seleccióna la opción **Photos** en el menu en la esquina superior derecha del cuado de dialogo.
3. **Enabled**. Apagado. Esta sección guarda fotos de las cámaras constantemente, no es necesario ya que las que nos interesan se toman al detectar movimiento o caras y estas se activa mas adelante en la sección _Mode_.
4. **AI Server**. Default. No es necesario configurar algo extra ya que esto permite aplicar funciones de AI con un servidor externo.
5. **JPG URL**. Esta configuración es para indicar a _AgentDVR_ una url diferente para cámaras IP en caso de que el fabricante tenga una ruta diferente para obtenerlas en lugar de tomarlas del stream. No hace falta configurar nada extra aquí.
6. **Mode**: Configurar a Motion Detected. Permite activar la opción de guardado ante la detección de eventos. Esto se activa automáticamente aunque la opción general este desactivada.
7. **Interval**: Configurar 60. Esto guarda una foto segun el tiempo indicado cuando se activa la directiva anterior. Si se actva la configuración general mencionada en el punto 3, las fotos se guardaran constantemente independientemente de la detección de movimiento o rostros.
8. **Delay**. Se configura en 0 para tomar la foto inmediatamente. Establece el tiempo de espera antes de tomar una nueva foto. 
9. **Quality**. Configurar en 80. Esta configuración determina la calidad de la foto. Configura a 100 para mejores resultados.
10. **Overlay Text**. Configura un texto para escribir en la imagen. Puedes poner el texto que quieras, en mi caso será `estocolmosindrome.com` Esta configuración es valida aunque la configuración general esté desactivada (paso 3).
11. **File Name**. Cambia el formato de nombrado de las fotos, no es necesario cambiar nada aquí.
12. **FTP**. Mantener Apagado. Esto guarda las fotos en un FTP previamente configurado, lo cual sólo está disponible en la versión pagada de _AgentDVR_.
13. **Counter Max**. Dejar en 20. Es un numero secundario para evitar sobre escribir imagenes con el mismo nombre, solo útil en caso de que cambies algo que garantice nombres diferentes, como quitar los modificadores de minuto o segundoen la configuración de nombrado.

Haz clic en OK para guardar estas configuraciones.

### Configuración general de almacenamiento
1. Haz clic derecho en la cámara que deseas configurar y selecciona la opción **Edit**.
2. Seleccióna la opción **Storage** en el menu en la esquina superior derecha del cuado de dialogo.
3. **Location**: Determina la carpeta en la que se guardan las fotos, de forma predeterminada pone la del servidor general.
4. **Folder**: Genera un nombre aleatorio para los videos guardados por esta cámara. Puedes cambiarlo pero no es necesario.
5. **Archive**: Mantener activado. Esto permitirá aplicar las directivas de archivado configuradas en la sección del servidor.
6. **Storage Management**: Mantener activado. Esta opción permite aplicar directivas extra de almacenamiento.
7. **Max Size**: Esta opción permite asignar una directiva personalizada para esta cámara. Dejar en 1024.
8. **Max Age**: Esta opción permite asignar una directiva personalziada para esta cámara. Dejar en 72.


## Referencias

Puedes consultar los siguientes video para mas detalles

- [Lista de reproducción del proyecto](https://www.youtube.com/watch?v=_F277YnKmog&list=PLm5nY_UPV5A7sAQCkPrWafyoOXLW3rvgx&pp=iAQB)
- [Tutorial: Desarrollo de Proyecto 009 - Instalando Agent DVR y Ejemplo con ESP32CAM](https://youtu.be/3nzBiaU9kvc)
- [Tutorial: Desarrollo de proyecto 012 - Camera Web Server con ESP32CAM](https://youtu.be/hWVYICauV34)
- [Tutorial: Desarrollo de proyecto 013 - Servidor de CodeProject.AI para reconocimiento facial](https://youtu.be/_mnCV-Gkf0c)
- [Desarrollo de proyeto 014 - Configuración de detección de rostros con AgentDVR y CodeProyect.AI](https://youtu.be/_YfmRRuaYoE)