# Instrucciones para configurar WSL

## Instalar WSL

Para instalar Windows Subusystem for Linux usar el siguiente comando

PowerShell:

<code>wsl -- install</code>

## Configurar Ubuntu para que use WSL2

Es necesario que Ubuntu o cualquier distro instalada bajo WSL use WSL2 para activar la integración con Docker Desktop

### Consultar la versión de Ubuntu
PowerShell:

<code>wsl.exe -l -v</code>

### Configurar la versión de Ubuntu
PowerShell:

<code> wsl.exe --set-version Ubuntu 2</code>

### Configurar las versiones default
PowerShell:

<code>wsl.exe --set-default-version 2</code>

**Fuentes**

- https://docs.docker.com/desktop/windows/wsl/
- https://learn.microsoft.com/en-us/windows/wsl/install
- https://learn.microsoft.com/es-mx/windows/wsl/-install-manual#step-4---download-the-linux-kernel-update-package

## Referencias

- [Lista de reproducción del proyecto](https://www.youtube.com/watch?v=_F277YnKmog&list=PLm5nY_UPV5A7sAQCkPrWafyoOXLW3rvgx&pp=iAQB)
- [Tutorial: Desarrollo de proyecto 003 - Configuración de WSL](https://youtu.be/HiNEgwn-EPQ)