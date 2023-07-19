# Instrucciones para Docker

## Instalar Docker
Se ralizará la instalación de Docker para Windows con ayuda de WSL. Para que Docker funcione es necesario activar la virutalización.

https://www.docker.com/get-started/

**Notas:** Para completar correctamente la instalación de Docker se requiere lo siguiente:
- Activar la virtutalización de tu procesador en la BIOS de tu PC
- Al instalar Docker es necesario activar WSL2
- Para que funcionen correctamente las configuraciones del algunos contenedores es necesario contar con una distro para poder gestionar el sistema de archivos. Se usó Ubuntu para este proyecto.
- Hay que configurar Ubuntu para que funcione en WSL2

### Mover Docker Data a un directorio diferente
https://www.youtube.com/watch?v=gWBNk2KYg3M

- Detener WSL 

    <code>wsl --shutdown</code>
- Comprobar el estado de WSL
    
    <code> wsl -l -v</code>
- Crear un directorio para docker en un disco externo 
    
    <code>wsl --export docker-desktop-datad:\docker-data\dockerdesktop.tar </code>
- Cambiar el registro del contenedor 

    <code>wsl --unregister docker-desktop-data</code>
- Registrar el nuevo directorio del contenedor de volumen de Docker

    <code>wsl --import docker-desktop d:\docker-data\desktop d:\docker-data\desktop\dockerdesktop.tar</code>
- Reiniciar docker
- Para cambiar el subsistema predeterminado

    <code>wsl -s [nombre_del_contenedor]</code>

### Mosquitto Docker
Broker MQTT

- Documentación https://hub.docker.com/_/eclipse-mosquitto/

### NodeRed Docker

Servidor de propósito general

https://nodered.org/docs/getting-started/docker

Descargar contenedor con:

<code>docker run -it -p 1880:1880 -v node_red_data:/data --name mynodered nodered/node-red</code>

## Integración con WSL2

Para usar Docker en Windows, es recomendable usar la versión 2 de Windows Subsystem for Linux. Una vez instalado deberás activar la integración con WSL2. Una vez que hayas activado WSL2, deberás instalar una distribución de Linux, para este proyecto se usará Ubuntu. Debes configurar Docker Desktop para integrarse con esa distribución. Se recomienda usar Windows Terminal en lugar de CMD y PowerShell.

### Instrucciones
- En la sección de configuración entra a la sección General. Asegurate de activar la opción Use the WSL 2 based engine
- Abre la sección Resources y dirigete a la opción WSL Integration. Asegurate de activar la casilla de verificación Enable integration with my default WSL distro.
- En esa misma sección, activa la el switch de tu distribución, en este caso, Ubuntu.

## Solución de problemas

En caso de que al ejecutar comandos de Docker en la terminal de Ubuntu, intenta lo siguiente:

1. Asegurate de usar Windows 10 version 2004 (Build 19041) o posterior.
2. Instala los paquetes de Docker
    
    ```sudo apt-get update && sudo apt-get install apt-transport-https ca-certificates curl software-properties-common```

3. Agrega el GPG key de Docker

    ```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg```

4. Agrega el repositorio de Docker

    ```echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null```

5. Actualiza el índice de Docker

    ```sudo apt-get update && sudo apt-get install docker-ce docker-ce-cli containerd.io```

6. Agrega tu usuario al grupo de ejecución de Docker

    ```sudo usermod -aG docker $USER```

7. Comprueba la versión de Docker

    ```docker --version```

8. Verifica que Docker esté corriendo

    ```docker run --rm hello-world```

En caso de que la configuración sea correcta, deberás ver el mensaje "Hello World" seguido de información del sistema.

    

# Notas

- Volumenes de almacenamiento con Docker https://www.docker.com/get-started/

## Referencias

- [Lista de reproducción del proyecto](https://www.youtube.com/watch?v=_F277YnKmog&list=PLm5nY_UPV5A7sAQCkPrWafyoOXLW3rvgx&pp=iAQB)
- [Tutorial: Desarrollo de Proyecto 002 - Configuración de Docker 1](https://youtu.be/Ljne-GhgDC0)