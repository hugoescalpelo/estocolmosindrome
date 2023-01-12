# Configuración de MySQL

Este documento contiene las instrucciones necesarias para la configuracion y creación de bases de datos necesarias en MySQL

## Accede a MySQL

Para acceder a MySQL debes tener instalado MySQL Server. Funciona en cualquier sistema operativo.

1. Abre una terminal
2. Escribe el comando ```sudo mysql```

En caso de tener una instalación en Docker, deberás ejecutar el siguiente comando.

```docker exec -it mysql-container-id mysql -p```

## Instrucciones

1. Crear bases de datos necesarias
```
create nombre_db;
use nombre_db;
```
2. Crear tablas

3. Crear usuario con permisos limitados e identificado por una contraseña simple. Es importante configurar el acceso remoto. 

```
CREATE USER 'nombre_usuario'@'localhost' IDENTIFIED BY 'tu_password';
CREATE USER 'nombre_usuario'@'%' IDENTIFIED BY 'tu_password';
GRANT SELECT, INSERT ON nombre_db.* TO nombre_usuario@’localhost’;
GRANT SELECT, INSERT ON nombre_db.* TO nombre_usuario@’%’;
```

## Notas

- No es necesario vincular un archivo de configuración para realizar un binding a 0.0.0.0 como se realiza tradicionalmente, solo hace falta crear el usuario con acceso remoto en %

## Fuentes

- Configuración de usuarios remotors https://itman.in/en/mysql-add-user-for-remote-access/