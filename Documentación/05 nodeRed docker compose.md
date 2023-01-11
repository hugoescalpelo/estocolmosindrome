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

**Fuentes**
- Permisos de nodeRed en docker https://github.com/node-red/node-red-docker/wiki/Permissions-and-Persistence