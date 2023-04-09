# Configura NodeRed con los nodos del proyecto

## Requisitos

- Windows
- Docker Desktop. La versión de Windows ya incluye docker-compose (opcional).
- WSL2
- Ubuntu (WSL2)
- Activar la integración de Ubuntu en Docker Desktop
- Visual Studio Code
- Windows Terminal
- nodeRed

## Instrucciones

1. Importar los nodos del proyecto. 
    - Hacer clic en el menu
    - Seleccionar la opción imprtar
    - Abrir el archivo flows.json que se ecuentra en github>estocolmosindrome>NodeRed

2. Solucionar las dependencias de nodos. Instalar desde el menu manage pallet
    - Nodos Dashboard. https://flows.nodered.org/node/node-red-dashboard    
    - Nodos Alexa. https://flows.nodered.org/node/node-red-contrib-alexa-cakebaked
        - alexa-remote-account
        - alexa-remote-smarphone
        - alexa-remote-routine
        - alexa-remote-echo. 
    - Nodos Twitter. https://flows.nodered.org/node/node-red-node-twitter
        - twitter in
        - twitter out
        - twitter-credentials
    - Nodo Ping. https://flows.nodered.org/node/node-red-node-ping
    - Nodo ReadDir. https://flows.nodered.org/node/node-red-contrib-readdir
    -Nodos Telegram. https://flows.nodered.org/node/node-red-contrib-telegrambot
    - Nodos e-mail. https://flows.nodered.org/node/node-red-node-email
    
        