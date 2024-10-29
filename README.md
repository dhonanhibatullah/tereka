# **tereka**

The short for "Teknologi Rekonstruksi Kecelakaan", created by Dhali', with the help of Dhonan.

## **1. Firmware Uploading**

Please make sure you have the PlatformIO Core and CLI installed in your machine. Check out this [link](https://docs.platformio.org/en/latest/core/installation/index.html). If already installed, remember to source the Platformio's virtual enviroment, which usually can be done with:

```bash
source ~/.platformio/penv/bin/activate
```

After sourcing the environment, proceed with the upload:

```bash
cd /{TO_TEREKA_PATH}/mcu
pio init
pio run --target upload
```

If you want to toggle the calibration, you can comment/uncomment the `#define __CALIBRATE__` inside `./mcu/src/main.cpp`.

## **2. Application**

Initialise the required virtual environment with:

```bash
sudo apt install python3-dev build-essential
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the app with:

```bash
python3 app.py --visual
# or
python3 app.py --process
```

Make sure you have grant the access to `/dev/ttyUSB0` or your serial port with:

```bash
sudo chmod a+rw /dev/ttyUSB0
```
