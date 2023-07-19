# Docker Compose

Docker Compose es un software para la configuración, instalación y ejecución de contenedores de forma centralizada. Consiste en un archivo de extensión yaml que contiene las configuraciones de cada contenedor.

## Requisitos

- Windows
- Docker Desktop. La versión de Windows ya incluye docker-compose (opcional).
- WSL2
- Ubuntu (WSL2 para )
- Activar la integración de Ubuntu en Docker Desktop
- Visual Studio Code
- Windows Terminal

## Instrucciones

1. Abrir una terminal de Ubuntu en Windows
2. Crear una carpeta en el directorio Home y entrar. Nota: El nombre es arbitrario.

    ```
    mkdir compose
    cd compose
    ```
3. Abrir Visual Studio Code en ese directorio.

   ```
   code .
   ```
4. Crear el archivo docker-compose.yaml haciendo clic en el boton de agregar achivo en el panel de directorio.
5. Crear el archivo mosquitto.conf en el directorio config. 

    Ejemplo: ```/home/username/mosquitto/config/mosquitto.conf``` cuando la configuración del volumen para config es ```/home/hugoe/mosquitto/config:/mosquitto/config```
    
6. Correr el achirvo docker-compose.yaml

    <code>sudo docker-compose -d up</code>

    Esto arrancara mosquitto e instalara el contenedor en caso de que no exista ya

7. Comprobar el funcionamiento de mosquitto

    - Correr los siguientes comandos en una terminal del contenedor. Cada uno de los comandos debe ejecutarse en una terminal diferente.

        ```
        mosquitto_sub -h localhost -t hugo/test
        mosquitto_pub -h localhost -t hugo/test -m "hola mosquitto"
        ```

    Debe verse el mensaje enviado por la terminal del segundo comando en la terminal del primer comando.

    - Puede correrse un comando dentro del contenedor de la siguiente forma

        <code>docker exec id_del_contenedor comando_a_ejecutar</code>

## Contenido de mosquitto.conf
```
listener 1883 0.0.0.0
allow_anonymous true
```


## Documentación

- Detalles sobre docker-compose y el archivo yaml 
https://docs.docker.com/compose/compose-file/


## Enlaces útiles
- Configuración simple https://hub.docker.com/r/toke/mosquitto/
- Configuración con persistencia y seguridad https://hub.docker.com/r/efrecon/mosquitto/#!
- Origen del archivo mosquitto.conf https://github.com/eclipse/mosquitto/blob/master/docker/2.0/mosquitto-no-auth.conf
- Crear usuarios con contraseña https://github.com/vvatelot/mosquitto-docker-compose
- Mosquitto con plugins de autentificación https://github.com/jllopis/docker-mosquitto/blob/master/docker-compose.yml

## Referencias

- [Lista de reproducción del proyecto](https://www.youtube.com/watch?v=_F277YnKmog&list=PLm5nY_UPV5A7sAQCkPrWafyoOXLW3rvgx&pp=iAQB)
- [Tutorial: Desarrollo de proyecto 004 - Configuración de Docker Composer](https://youtu.be/cka6lsQUMHw)