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


# Notas

- Volumenes de almacenamiento con Docker https://www.docker.com/get-started/