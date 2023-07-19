# Instala CodeProject.AI

[CodeProject.AI](https://www.codeproject.com/) es un servidor de Inteligencia Artificial autogestionado, local, que se usará para la función de reconocimiento facial de AgentDVR. Es multi plataforma y en esta nota se muestra la instalación en Docker Compose.

## Requisitos

- Windows
- Docker Desktop. La versión de Windows ya incluye docker-compose (opcional).
- WSL2
- Ubuntu (WSL2)
- Activar la integración de Ubuntu en Docker Desktop
- Visual Studio Code
- Windows Terminal
- CodeProject.AI with GPU

## Instrucciones

1. Modificar el el archivo docker-compose.yaml, agregar la siguiente sección

```
CodeProjectAI:
    image: codeproject/ai-server:gpu
    container_name: CodeProject.AI
    ports:
      - 32168:32168
    volumes:
      - /home/user/codeproject/ai:/etc/codeproject/ai
      - /home/user/codeproject/ai:/app/modules
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    restart: unless-stopped
```

2. Crear las carpetas correspondientes a los volumenes. Recuerda cambiar el usuario de la ruta por tu usuario en caso de usar una ruta absoluta o usar una ruta relativa.
```
mkdir /home/user/codeproject
cd codeproject
mkdir ai
```
3. Dirígete al dircetorio de tu archivo docker-compose.yaml y ejecuta el siguiente comando ```sudo docker-compose up -d```. La instalación tomará varios minutos segun tu conexión, la instalación es de varios GB.

4. Dirígete a Docker Desktop o ejecuta el comando ```docker ps -a``` y comprueba que el contenedor ha arrancado.
        
5. Comprueba que el servidor se encuentra corriendo visitando [localhost:32168](http://localhost:32168/). Verás un sitio con el resumen del funcionamiento del servidor de inteligencia artifical

## Pasos siguientes

El servidor de inteligencia artifical se usa para el reconocimiento facial en AgentDVR. Será necesario indicar la IP del servidor y configurar las cámaras.

## Referencias

- [Lista de reproducción del proyecto](https://www.youtube.com/watch?v=_F277YnKmog&list=PLm5nY_UPV5A7sAQCkPrWafyoOXLW3rvgx&pp=iAQB)
- [Tutorial: Desarrollo de proyecto 013 - Servidor de CodeProject.AI para reconocimiento facial](https://youtu.be/_mnCV-Gkf0c)