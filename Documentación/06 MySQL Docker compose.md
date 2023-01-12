# Instala mySQL con Docker Compose en WSL2

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
2. Agregar la configuración del contenedor de mysql
    ```
    mySQL:
    image: mysql
    restart: always
    command: --default-authentication-plugin=mysql_native_password
    volumes:
      - /home/hugo/mysql/db:/var/lib/mysql
    ports:
      - 3306:3306
    environment:
      MYSQL_ROOT_PASSWORD: password
    ```
3. Ejecutar la nueva configuración
    
    ```sudo docker-compose up -d```

## Acceder a mysql-server

Para acceder a la linea de commandos de MySQL Server, debes abrir una terminal de Ubuntu en Windows Terminal y ejecutar el siguiente comando. Deberás proporcionar la contraseña que configuraste en el archivo docker-compose.yaml

```docker exec -it mysql-container-id mysql -p```

## Fuente

- Página de MySQL en Docker Hub https://hub.docker.com/_/mysql/
- Documentación de Docker Compose en en el sitio de MySQL https://dev.mysql.com/blog-archive/docker-compose-and-app-deployment-with-mysql/
- Tutorial de aplicaciones multicontenedores de Microsoft https://learn.microsoft.com/en-us/visualstudio/docker/tutorials/tutorial-multi-container-app-mysql
- Documentación del archivo Compose en Docker https://docs.docker.com/compose/compose-file/
- Tutorial de MySQL en Docker Compose https://medium.com/@chrischuck35/how-to-create-a-mysql-instance-with-docker-compose-1598f3cc1bee
