# Instala Traccar con Docker Compose en WSL2

## Requisitos

- Windows
- Docker Desktop. La versión de Windows ya incluye docker-compose (opcional).
- WSL2
- Ubuntu (WSL2)
- Activar la integración de Ubuntu en Docker Desktop
- Visual Studio Code
- Windows Terminal

## Instrucciones
1. Abrir el archivo docker-compose en visual studio code
    - Abrir una terminal Ubuntu en Windows Terminal
    - Dirigirse al directorio donde está docker-compose.yaml
        ```
        cd compose
        code .
        ```
2. Agrega lo siguiente a la sección de servicios del archivo docker-compose.yaml

    ```
    traccar:
        image: traccar/traccar:latest
        container_name: traccar
        restart: unless-stopped
        ports:
        - "8082:8082"
        - "5000-5150:5000-5150"
        environment:
        - "TZ=UTC"
        volumes:
        - /home/user/traccar/data:/opt/traccar/data
        - /home/user/traccar/logs:/opt/traccar/logs
        #- /home/user/traccar/conf:/opt/traccar/conf
        networks:
        - network_0_1
    ```
3. Abre una terminal de Ubuntu en Windows Terminal y crea el directorio traccar. Dentro del directorio traccar crea los directorios data y logs. Puedes usar los siguientes comandos.

    ```
    mkdir traccar
    cd traccar
    mkdir data
    mkdir logs
    ```
4. Ejecuta el archivo docker-compose.yaml

    ```
    sudo docker-compose up -d
    ```
5. Para entrar a traccar abre cualquier navegador en el equipo donde instalaste Docker y dirígiete a ```http://localhost:8082/```

6. Inicia sesión con las credenciales predeterminadas

    ```
    user: admin
    password: admin
    ```

    En caso de que no funcione, registra un nuevo usuario con los datos de tu preferencia. Estos datos son completamente locales. No olvides guardar las credenciales en un lugar seguro, las necesitarás mas adelante.

## Referencias

- [Lista de reproducción del proyecto](https://www.youtube.com/watch?v=_F277YnKmog&list=PLm5nY_UPV5A7sAQCkPrWafyoOXLW3rvgx&pp=iAQB)
- [Tutorial: Desarrollo de proyecto 010 - Traccar con Docker Compose](https://youtu.be/7bo0OQqjoFg)