# Instala NodeRed en Docker WSL2 con Docker Compose

## Requisitos

- Windows
- Docker Desktop. La versión de Windows ya incluye docker-compose (opcional).
- WSL2
- Ubuntu (WSL2)
- Activar la integración de Ubuntu en Docker Desktop
- Visual Studio Code
- Windows Terminal

# Instrucciones

1. Abrir el archivo docker-compose en visual studio code
    - Abrir una terminal Ubuntu en Windows Terminal
    - Dirigirse al directorio donde está docker-compose.yaml
        ```
        cd compose
        code .
        ```
2. Agregar la configuración del contenedor de nodeRed
    ```
    nodered:
        image: nodered/node-red
        restart: always
        volumes:
        - /home/hugoe/nodered/data:/data
        ports:
        - 1880:1880
    ```
3. Crear la carpeta de datos de nodered
    - Dirigirse a la carpeta home
    - ```mkdir -p nodered/data```
4. Ejecutar la nueva configuración
    
    ```sudo docker-compose up -d```

## Compobar el funcionamiento de NodeRed

- Abrir un navegador en ```localhost:1880```

## Agregar contraseña a NodeRed

1. Abrir el documento settings.js ubicado en ~/nodered/data
2. Descomentar la sección adminAuth:
3. Generar una nueva contraseña desde una terminal en el contenedor de nodered con el comando ```node-red admin hash-pw```
4. Pegar en la sección de password del archivo settings.js el hash creado en el paso anterior.
5. Guardar los cambios en el archivo settings.js
6. Reiniciar el contenedor de node-red
7. Entrar a localhost:1880 desde un navegador en la computadora donde está instalado node-red con Docker y colocar la contraseña para acceder a los flows.

**Fuentes**
- Permisos de nodeRed en docker https://github.com/node-red/node-red-docker/wiki/Permissions-and-Persistence
- Seguridad en NodeRed https://nodered.org/docs/user-guide/runtime/securing-node-red

## Referencias

- [Lista de reproducción del proyecto](https://www.youtube.com/watch?v=_F277YnKmog&list=PLm5nY_UPV5A7sAQCkPrWafyoOXLW3rvgx&pp=iAQB)
- [Tutorial: Desarrollo de Proyecto 006 - NodeRed Docker Compose WSL](https://youtu.be/iDpIBC3Q8DI)