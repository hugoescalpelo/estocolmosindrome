
## Direccionamiento

En lugar de escribir localhost para enviar un mensaje entre contenedores corriento en el mismo equipo, es necesario usar como nombre de host el nombre del servicio.

## Intercambio de información entre contenedores

Para que los contenedores puedan interactuar entre ellos cuando están instalados de manera local en la misma computadora, deberás usar las configuraciones de red de Docker Compose.

Para ello, cada servicio dado de alta en el archivo .yaml deberá contener la opción networks con el nombre de cada red en la que puedan interactuar. Puedes agregar multiples redes para incluir o excluir contenedores como si fueran grupos de redes.

Al final del archivo, se debe agregar la opción networks al mismo nivel que services y dentro de esta sección deberás agregar el nombre de red. A continuación se muestra un ejemplo

```
version: '3'

services:
nodered:
    image: nodered/node-red
    restart: always
    volumes:
    - /home/user/nodered/data:/data
    ports:
    - 1880:1880
    networks:
    - network_1

mySQL:
    image: mysql
    restart: always
    command: --default-authentication-plugin=mysql_native_password
    volumes:
    # - /home/user/mysql/config/config.cnf:/etc/my.cnf
    - /home/user/mysql/db:/var/lib/mysql
    ports:
    - 3306:3306
    environment:
    MYSQL_ROOT_PASSWORD: password
    networks:
    - network_1

networks:
network_1:

```

Este ejemplo se asegura de que MySQL y NodeRed puedan interactuar en la misma red.
## Fuentes

- https://www.youtube.com/watch?v=PXo3AAquPy0

## Referencias

- [Lista de reproducción del proyecto](https://www.youtube.com/watch?v=_F277YnKmog&list=PLm5nY_UPV5A7sAQCkPrWafyoOXLW3rvgx&pp=iAQB)
