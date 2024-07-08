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

### Step 1: Initialise Data Recording for Microcontroller
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

## Perfrom Data Acquitition
Now you have sucessfully uploaded the data aqutition code, your device is ready to Data Recording. Go back to jyputer notebook where the package is installed. Run the below code. 

```sh

from easyRTML import DataAQ

filename = "fsr" # Enter the name you want for your recorded CSV file Eg. "fsr"
serial_port = '/dev/tty.usbserial-XXXX'  # Enter the serial port name Eg. COMX, /dev/tty.usbserial-XXXX
baud_rate = 115200  # Enter the same BaudRate used in Data Recording code at Arduino IDE.

data_acquisition = DataAQ(filename=filename, serial_port=serial_port, baud_rate=baud_rate)

"""
-Protocol to record data:
  * Data should be recorded in Continious Motion
  * Mean geature duration should be aproximately 1 sec.
  * For good results, record for minimum 30 sec with 30 repetation of motion for that label.

- The code will pormt to enter the Duration of data to be recorded.
- You can record multiple labels, to perfrom multiclass classificcation as required.
- You can record the data again for any label if not recorded perfectly.
- Csv file will be saved in your directory with the mentioned "filename_sampling_freq.csv"
Tip : If code stops while recording or doesn't, pulg out the serial port and plug in back.

"""

```

Cool, once the CSV file is been exported it's ready for PreProcessing!

## Step 2: PreProcessing

```sh

from easyRTML import Processor, Plot
file_name = 'fsr.csv' # Replace with your recorded, saved CSV file in directory.
processor = Processor(file_name)

Plot.plot(processor.df) #Plots the CSV file features
Plot.plot_normalized(processor.normalized_df) #Plots the normalized features
Plot.plot_separated(processor.normalized_df)  #Separetly plots every normlaized label

```

## Step 3: Feature Extraction 

```sh
from easyRTML import Extractor

#Update the sampling_freq with your recorded CSV file. Update mean_geature_duration and shift if needed. (Experiemnt with it)
extractor = Extractor(sampling_freq=1000, mean_gesture_duration=1000, shift=0.3)

features_df, shuffled_df, variables = extractor.process_data(processor.normalized_df)
features_df.describe()

```

## Step 4: Feature Selection + Model Training 

Now we are all set to Train out Machine Learning model. Before that we select the best features among the features_df dataframe which corresponds to highest accursy with limited number of features eventually resulting in prediction time 10-100 macroseconds.

Outputs and Visual results:
- List of Selected Features
- Folds Accuracy, Mean Folds Accuracy, Training Accuracy, Testing Accuracy
- Classification Report of Tranined Model
- Confusion Matrix
- Coorelation matrix of selected features
- Pair Plot of select features


Currently we support 2 Machine learning models Xgboost and Random Forest compatible for offline classification, Python online classification and Deployment in microcontroller.

### Xgboost Model Traning 

```sh

from easyRTML import XGML

xgml = XGML(shuffled_df)
xgml.Xgboost(
    xgb_params={'max_depth': 3, 'n_estimators': 10},
    cv_params={'n_splits': 5},
    filename='xgboost_model.pkl'
)
#Change xgb_params and cv_params as required.

```

### Random Forest Model Traning 

```sh

from easyRTML import RBML

rfml = RBML(shuffled_df)
rfml.Random_forest(
    rf_params={'max_depth': 3, 'n_estimators': 10},
    cv_params={'n_splits': 5},
    filename='rf_model.pkl'
)
#Change rf_params and cv_params as required.

```

## Step 5: Model deployment to perfrom Real-Time Machine Learning (RTML)

You are all set at this point to deploy your model in various platforms and get live predictions from new data by sensor.

You can:
- Perfrom RTML in jupyter notebook or VSCode though Python 
- Perfrom RTML in ESP32, ESP8266, Arduino 33 BLE Microcontroller through Classifier.h and Pipeline.h generted code
- Perfrom RTML in RaspberryPi through Miropython generted code (....Comming soon)

To use any of this code, you should get an Authetication Key from https://easyrtml.pythonanywhere.com/


Note: Make sure you enter proper Email and Name, Since you will be reciving Authetication Key on your provided Email.

Next, save your Authetication Key and Email you recived, it would be required to execute the code. 


### RTML through Python code (for Jupyter Notebook or VSCode)

```sh

from easyRTML import authenticate
email = "abc@gmail.com" #Enter your email here

#Authetication Key: 136126847XXXXXXXXXXXXX 

if authenticate(email=email):
    
    from easyRTML import pyRTML

    py_RTML = pyRTML(processor, extractor, xgml) #Change rfml/xgml depending upon which model been used
    
    """
    - Run the below code to access the generted python script to Execute the Real-time classification.
    - Make sure you define model_file, serial_port, baud_rate correctly.
    - Genearted code will be saved in your directory.
    """
    generated_code = py_RTML.easyRTML_python_generate(model_file="xgboost_model.pkl", serial_port='/dev/cu.usbserial-0001', baud_rate=115200)
    py_RTML.save_code_to_file(generated_code) # Save the generated code to a file
    print(generated_code)

    """
    - Run the below code to Execute the Real-time classification directly without getting generted code.
    - Make sure you define model_file, serial_port, baud_rate correctly.
    - Genearted code will be saved in your directory.
    """
    # py_RTML.execute_generated_code(model_file="xgboost_model.pkl", serial_port='/dev/cu.usbserial-0001', baud_rate=115200) 
    
else:
    print("Access denied")

    """
    - A promt will apprear, please enter your Authetication code to proceed.
    """

```





