# Configuración de AI de AgentDVR

[AgentDVR](https://www.ispyconnect.com/) es un software para cámaras de vigilancia que es compatible con reconocimiento facial y reconocimiento de objetos con ayuda de [codeproject.ai](https://www.codeproject.com/). En este documento se muestran las configuraciones de AgentDVR para hacer uso de reconocimiento facial por Inteligencia Artificial

**Nota**: Antes de ejcutar cualquier configuración de este documento, lee la sección final sobre optimización.

## Requisitos

- Windows
- Docker Desktop. La versión de Windows ya incluye docker-compose (opcional)
- WSL2
- Ubuntu (WSL2)
- Activar la integración de Ubuntu en Docker Desktop
- AgentDVR en [localhost:8090](http://localhost:8090/)
- CodeProject.AI with GPU en [localhost:32168](http://localhost:32168/)


## Instrucciones

Este instructivo asume que ya tienes instalado AgentDVR,  CodeProject.AI y tienes algunas cámaras funcionando. Para este caso, el primero se instala de forma nativa y el segundo por Docker Compose.

### Configuración server de CodeProject.AI en AgentDVR

1. Haz clic en el botón de configuración de server en la interfaz de AgentDVR
2. En la sección Configuration, selecciona Settings
3. Haz clic en el menú de la esquina superior derecha y selecciona la opción AI Servers
4. En la sección AI Servers, haz clic en el botón Configure
5. Haz clic en el botón Add para agregar un nuevo servidor de Inteligencia Artificial
6. Configura el servidor con los siguientes valores

    - **Name**: CodeProject.AI (Puede ser el que tu quieras)
    - **AI Server URL**: http://localhost:32168/ (Usa uno diferente si tu server de codeproject.ai corre en una ruta diferente)

    Puedes dejar los demas campos con su valor predeterminado.
7. Haz clic en OK hasta guardar todos los cambios y salir del menú.

Este proceso agrega el servidor de CodeProject.AI a tu AgentDVR. Es necesario agregar el reconocimiento facial a cada cámara que tengas configurada.

### Configuración de cámara para Face Recognition

Para que cada cámara sea capáz de hacer uso del servidor de CodeProject.AI para hacer el reconocimiento de rostro, necesitas configurar cada cámara de forma independiente.

**Nota**: La configuración de reconocimiento facial con CodeProjet.AI permite diferenciar e identificar rostros específicos, no solo detectar la presencia de un rostro en la imagen.

Para realizar esta configuración ya debes tener cámaras agregadas a AgentDVR. Puedes encontrar mas detalles mas adelante en la sección **Referencias**.

1. Haz clic derecho en una cámara que tengas agregada en tu AgentDVR, selecciona la opción editar.
2. En el menú superior derecho selecciona la opción Detector.
3. Selecciona la opción de detector en Objects y el timeout en 2.
4. Haz clic en el botón configurar Objects.
5. Configura la detección de objetos de la siguiente forma:
    - Frame Size: Large. Este valor depende de las capacidades de tu servidor. Debes probar con diferentes configuraciones para optimizar el funcionamiento. Se recomienta Small para procesadores de 4 nucleos y tarjetas gráficas nVidia de gama básica de 2016 o superior. Se recomienda Medium para procesadores de 4 nucelos y tarjetas gráficas nVidia de gama básica de 2018 o superior. Se recomienda Large para procesadores de 4 nucelos y tarjetas gráficas nVidia de gama básica de 2020 o superior. Estas configuraciones son una guia muy rudimentaria, se recomienda probar multimples configuraciones en tu sistema. Ve el tutorial referenciado al final para mas detalles.
    - Detect Interval: 300. Este valor está en milisegundos y representa la detección de rostro por GPU en el feed normal de video. Esta configuración varía de acuerdo a tu sistema y lo recomendable es que ajutes un valor para que observes una detección fluida. Ve el tutorial referenciado al final para mas detalles.
    - Width Limits & Height limits: Esta configuración determina el area de detección. Se recomienda configurar este espacio de acuerdo a las capacidades de tu servidor y la posición de tu cámara. Ve el tutorial referenciado al final para mas detalles.
    - Use GPU: se recomienda tener esta opción activada. Para ello es necesario contar con una tarjeta gráfica nVidia dedicada.
    - File: face. Esta configuración te permite detectar distintos tipos de objetos. Para el caso de las cámaras que se asocian a la detección y diferenciación de rostros, es necesario seleccionar la opción Face.
    - Alert Condition: More Than. Esta configuración define la condicion que detona el concepto de detección para activar la grabación y la detección de rostros, en la cual se basa el resto del proyecto. La idea es configurar esto para que se detone al detectar mas de cero rostros.
    - Alert Number: 0. Define el numero de rostros detectados de acuerdo a la configuración anterior. Será cero para mas de un rostro si la configuración anterior es "More Than". 

    Puedes dejar el resto de configuraciones con el valor predeterminado.

    Para guardar estas configuraciones haz clic en OK hasta cerrar todos los menús. Esto se recomienda para garantizar el guardado de las configuraciones.

6. Haz clic derecho en la misma cámara, y selecciona la opción edit.
7. Selecciona el menú Face Recognition de la esquina superior derecha. Para realizar los siguientes pasos, debes haber completado la configuración de CodeProject.AI
8. Activa la detección de rostros por Inteligencia artificial. Configura el switch de detección a Enabled.
9. AI Server: Selecciona CodeProject.AI en el menu desplegable. El nombre puede cambiar si configuraste uno diferente en la sección anterior.
10. Mode: Motion Detected. Esta parte es muy importante, esta configuración debe coincidir con la mecánica de detección que has seleccionado. En nuestro caso, es la función Detect de la sección anterior. Alert es en el caso de que configures alertas, tema que hasta el momento no he desarrollado en documentación o en videos; su desventaja es que se basa en un sistema de inteligencia artificial de AgentDVR que es muy falible y debe "activarse" la seguridad de AgentDVR, lo cual genera notificaciones que son difícles de filtrar, motivo por el cual no se usa. Interval selecciona un intervalo fijo de detección, lo cual puede ser conveniente para ahorrar energía y procesamiento pero inconveniente para una fluidez del sistema.

    - Alert Conditions: Para modificar esta configuración debes hacer clic en el boton de tres puntos [...], después, lo unico que debes configurar es Alert Condition: More Than One y Alert Number: 0.
    - Use Snapshot URI: Desactivado. Esta opción guarda una captura de la detección de rostro en la ruta URI en caso de que tengas un servidor URI configurado. Esta es una opción de paga.
    - Overlay Results on Live Video: Activado. Esta opción dibuja el recuadro anaranjado alrededor de la cara detectada. Esta configuración es opcional.
    - Minimum Interval: 1. Esta configuración describe el espacio entre peticiones al servidor CodeProject.AI. Esta configuración debe estar de acuerdo a las capacidades de tu sistema. Esta configuración afecta directamente el consumo energético del sistema.
    - Confidence: Esta configuración establece el procentaje mínimo para lanzar la detección de un rostro. 
    - Edit Faces: Esta configuración se explicará en detalle en la siguiente sección.
    - AI Photos. Esta opción se activa en caso de que quieras guardar las fotos detectadas por el sistema de reconocimiento de inteligencia artificial de CodeProject.AI en el directorio predeterminado de guardado de archivos.

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
