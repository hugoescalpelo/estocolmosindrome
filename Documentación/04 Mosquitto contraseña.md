# Agregar contraseña a mosquitto en docker

## Requisitos

- Windows
- Docker Desktop. La versión de Windows ya incluye docker-compose (opcional).
- WSL2
- Ubuntu (WSL2 para )
- Activar la integración de Ubuntu en Docker Desktop
- Visual Studio Code
- Windows Terminal

# Instrucciones

1. Modificar el archivo mosquitto.conf
    - Abrir una terminal de Ubunto en Windows Terminal
    - <code>sudo nano ~/mosquitto/config/mosquitto.conf</code>
    - Debe contener lo siguiente

        <code>listener 1883 0.0.0.0</code>        
        <code>allow_anonymous false</code>
       <code> password_file /mosquitto/config/passwordfile</code>

2. Crear el archivo de contraseñas en una terminal del contenedor mosquitto en el directorio /mosquitto/config del contenedor

<code>osquitto_passwd -c passwordfile nombre_de_usuario</code>

3. Reiniciar el contenedor

## Comprobar el funcionamiento

A continuación se muestran los comandos a ejecutar para comprobar el funcionamiento, cada uno en su propia terminal

Ubuntu Shell:

<code>docker exec id_del_contenedor mosquitto_sub -h localhost -t hugo/test -u nombre_de_usuario -P contraseña</code>

Ubuntu shell:

<code>docker exec id_del_contenedor mosquitto_pub -h localhost -t hugo/test -m "hola mosquitto contraseña" -u nombre_de_usuario -P contraseña</code>

### Documentación

- http://www.steves-internet-guide.com/mqtt-username-password-example/
- https://iotechonline.com/password-protect-your-mosquitto-mqtt-broker/
- https://mosquitto.org/man/mosquitto_sub-1.html
- https://mosquitto.org/man/mosquitto_pub-1.html

