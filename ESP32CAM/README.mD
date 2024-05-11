# Configuración de Arduino IDE para cargar programas al ESP32CAM

- [ Configuración de IDE] (https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html#before-installing)

- [Instrucciones Windows](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html#windows-manual-installation)

- [Instrucciones Linux](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html#linux)

- Instrucciones Linux Externally managed

```
sudo apt update
sudo usermod -a -G dialout $USER
wget https://bootstrap.pypa.io/get-pip.py
sudo apt-get install python3-distutils
sudo apt-get install python3-apt
sudo apt install python3-pip
sudo apt install python3.11-venv
python3 -m venv myenv
source myenv/bin/activate
pip install pyserial
mkdir -p ~/Arduino/hardware/espressif
cd ~/Arduino/hardware/espressif
sudo apt install git
git clone https://github.com/espressif/arduino-esp32.git esp32
cd esp32
git submodule update --init --recursive
cd tools
python3 get.py
```