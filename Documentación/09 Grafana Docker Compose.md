# Instala Grafana con Docker Compose en WSL2

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
2. Agregar la configuración del contenedor de grafana en la sección de services y los volumenes para que se pueda guardar la información de grafana de manera permanente. 
    ```
    grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    networks:
      - localnetwork01
    ```
3. Ejecutar la nueva configuración
    
    ```sudo docker-compose up -d```

## Acceder a mysql-server

Asegurate de que el contenedor de grafana está corriendo desde la aplicación de Docker.

Para acceder al servidor de grafana, dirigete a la siguiente dirección en algun navegador en la computadora donde instalaste grafana.

```http://localhost:3000```

## Realiza la primer configuración de Grafana

Al acceder al sitio local de grafana por primera vez, usa el nombre de usuario y contraseña predeterminados.
```
admin_user = admin
admin_password = admin
```
Se te solicitará crear una nueva contraseña. Guardarla en un lugar seguro.

## Fuente

- Sitio de grafana https://grafana.com/
- Página de grafana en docker https://hub.docker.com/r/grafana/grafana/
- Página de documentación de docker para grafana https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/
- Página de configuración de docker para grafana https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/
