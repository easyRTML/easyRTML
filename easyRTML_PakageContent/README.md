# easyRTML

![Project Logo](images/logo.png)

Now train your first Machine Learning signal classification model and deploy it in any microcontroller (ESP32, ESP8266, Arduino 33 BLE, RaspberryPi and Python) and perfrom classification in Real-Time.

# Prerequisite
- Any compatible microcontroller board
- Sensor (IMU, EMG, EOG, Flex_sensor, Force Resistve Sensor , etc)
- No Coding Knowledge Required
- Beigineer Friendly
- Easy to Use
- All in one (Data Acquisition, Data Cleaning, Data preprocessing, Feature Extraction, Feature Selection, Model selection, Scientific Visual Outputs, Best model fit, Deployment code generator)

## Table of Contents

- [Installation](#installation)


## Installation

1. Install easyRTML package in your jupyter notebook environment 
    ```sh
    pip install easyRTML
    ```

## Usage

### Perfrom Data Aquitition
To record the data from your microcontoller (for Instance Esp8266), recording code must be uploaded in it through Arduino IDE, initilizing the required sensor (for Instance MPU6050, IMU Sensor) with comma separted values.

Example Data Recording code of Arduino IDE for MPU6050 and ESP8266:
```sh

#include <Adafruit_MPU6050.h>
#include <Wire.h>
Adafruit_MPU6050 mpu;

void setup() {
Serial.begin(115200); //(Note the baudrate)
while (!Serial) {
delay(10); 
}

if (!mpu.begin()) {
while (1) {
delay(10);
}
}

mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
mpu.setGyroRange(MPU6050_RANGE_500_DEG);
}

void loop() {
sensors_event_t a, g, temp;
mpu.getEvent(&a, &g, &temp);

Serial.print(a.acceleration.x);
Serial.print(",");
Serial.print(a.acceleration.y);
Serial.print(",");
Serial.print(a.acceleration.z);
Serial.print(",");
Serial.print(g.gyro.x);
Serial.print(",");
Serial.print(g.gyro.y);
Serial.print(",");
Serial.print(g.gyro.z);
Serial.println("");
}

```

Select COMX port and upload the code. Once the is been uploaded in Arduino IDE go to Tools->Serial Ploter and check is the data is been plotting suceessfully. 

Tip: If The data is not plotting, check the baudrate match it to code if still problem exsit, plug out the serial port and pulg in back.

Now you have sucessfully uploaded the data aqutition code, your device is ready to Data Recording. Go back to jyputer notebook where the package is installed. Run the below code. 

```sh

from easyRTML import DataAQ

filename = "fsr" # Enter the name you want for your recorded CSV file Eg. "fsr"
serial_port = '/dev/tty.usbserial-XXXX'  # Enter the serial port name Eg. COMX, /dev/tty.usbserial-XXXX
baud_rate = 115200  # Enter the same BaudRate used in Data Recording code at Arduino IDE.

data_acquisition = DataAQ(filename=filename, serial_port=serial_port, baud_rate=baud_rate)

"""
- The code will pormt to enter the Duration of data to be recorded.
- You can record multiple labels, to perfrom multiclass classificcation as required.
- You can record the data again for any label if not recorded perfectly.
- Csv file will be saved in your directory with the mentioned "filename_sampling_freq.csv"
Tip : If code stops while recording or doesn't, pulg out the serial port and plug in back.

"""

```

