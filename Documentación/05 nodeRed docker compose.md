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
