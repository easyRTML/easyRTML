# A Complete Guide to use easyRTML
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/yourusername/easyRTML/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-brightgreen.svg)](https://www.python.org/downloads/)


<img width="1282" alt="Screenshot 2024-07-08 at 11 09 00 PM" src="https://github.com/easyRTML/easyRTML/assets/174990499/716f350f-f6fd-405e-b849-51762d5a5fbc">

**Dear ML Enthusiasts and Aspiring Beginners,**

Welcome to the world of Machine Learning! It’s perfectly okay to be a beginner in ML—I'm still learning myself! Today, you're about to start on a journey to train your first Machine Learning signal classification model. Deploy it on any microcontrollers like ESP32, ESP8266, Arduino 33 BLE, or platforms like Raspberry Pi and Python, you’ll be able to perform Real-Time classification with lightning-fast prediction times ranging from **10 to 100 microseconds.**

I’m a 4th-year Engineering student at IIT (BHU), and this package has been used for research work. The use case is detailed in my research paper, so you can be confident that this package is genuine and verified. Let's get started!

**Developer - Aryan Jadhav**
  

## Getting Started

- Any compatible microcontroller board
- Sensor (IMU, EMG, EOG, Flex_sensor, Force Resistve Sensor , etc)
- No Prior Coding Knowledge Required: Our solution is designed to be accessible even to those with no coding experience.
- Beginner-Friendly: User-friendly interface and straightforward processes ensure a smooth start for beginners.
- Easy to Use: Simple code to understand, less paramaters to tweak, press only enter that's it. That easy!.
- Comprehensive Solution: Includes all essential components—Data Acquisition, Data Cleaning, Data Preprocessing, Feature Extraction, Feature Selection, Model Training, Scientific Visualization, Optimal Model Fit, and Deployment Code Generation.

  
## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Step 1: Initialize Data Recording for Microcontroller](#step-1-initialize-data-recording-for-microcontroller)
  - [Step 2: PreProcessing](#step-2-preprocessing)
  - [Step 3: Feature Extraction](#step-3-feature-extraction)
  - [Step 4: Feature Selection and Model Training](#step-4-feature-selection-and-model-training)
    - [XGBoost Model Training](#xgboost-model-training)
    - [Random Forest Model Training](#random-forest-model-training)
  - [Step 5: Model Deployment for Real-Time Machine Learning (RTML)](#step-5-model-deployment-for-real-time-machine-learning-rtml)
    - [RTML Code Generator for Python (Jupyter Notebook & VSCode)](#rtml-code-generator-for-python-jupyter-notebook-vscode)
    - [RTML for Microcontroller (ESP32, ESP8266, Arduino 33 BLE, etc)](#rtml-for-microcontroller-esp32-esp8266-arduino-33-ble-etc)
      - [Generate Pipeline.h](#generate-pipelineh)
      - [Generate Classifier.h](#generate-classifierh)
      - [Modify the Data Recording Code of Arduino IDE (main.ino)](#modify-the-data-recording-code-of-arduino-ide-mainino)

## Installation

Install latest easyRTML package in your jupyter notebook environment

```sh
pip install easyRTML

```   


## Usage

## Step 1: Initialize Data Recording for Your Microcontroller
To get started with recording data from your microcontroller (for example, the ESP8266), you'll need to upload the recording code using the Arduino IDE. This code will set up your sensor (like the MPU6050 IMU sensor) to send data in a comma-separated format.

Here’s a sample data recording code for the MPU6050 and ESP8266:

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

Select the COMX port and upload the code to your microcontroller. Once the upload is complete, head over to 'Tools' -> 'Serial Plotter' in the Arduino IDE to verify that the data is plotting successfully.

> <span style="background-color: #FFFF00">**Tip:** If the data isn't plotting, double-check the baud rate to ensure it matches the code. If the issue persists, try unplugging and reconnecting the serial port.</span>

## Perform Data Acquisition
With the data acquisition code successfully uploaded, your device is now ready for Data Acquisition. Next, return to your Jupyter Notebook where the easyRTML package is installed. Execute the following code to start recording data: 

```sh

from easyRTML import DataAQ

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

filename = "fsr" # Enter the name you want for your recorded CSV file Eg. "fsr"
serial_port = '/dev/tty.usbserial-XXXX'  # Enter the serial port name Eg. COMX, /dev/tty.usbserial-XXXX
baud_rate = 115200  # Enter the same BaudRate used in Data Recording code at Arduino IDE.

data_acquisition = DataAQ(filename=filename, serial_port=serial_port, baud_rate=baud_rate)

```

**Voila!** Once the CSV file is exported, you're all set and ready to dive into PreProcessing! 🎉

## Step 2: PreProcessing

In this step, we’ll handle data cleaning, address any missing values, normalize the data, and visualize it through plots.

```sh

from easyRTML import Processor, Plot
file_name = 'fsr.csv' # Replace with your recorded, saved CSV file in directory.
processor = Processor(file_name)

Plot.plot(processor.df) #Plots the CSV file features
Plot.plot_normalized(processor.normalized_df) #Plots the normalized features
Plot.plot_separated(processor.normalized_df)  #Separetly plots every normlaized label

```

## Step 3: Feature Extraction 

Now we dive into one of the crucial stages: Feature Extraction. We'll employ a rolling window approach with a shift logic to extract time-domain features.

Features Extracted:
- Minimum
- Maximum
- Mean
- Root Mean Square

This features are enough to capture the essential characteristics of the data while keeping the model straightforward and manageable.

```sh
from easyRTML import Extractor

#Update the sampling_freq with your recorded CSV file. Update mean_geature_duration and shift if needed. (Experiemnt with it)
extractor = Extractor(sampling_freq=1000, mean_gesture_duration=1000, shift=0.3)

features_df, shuffled_df, variables = extractor.process_data(processor.normalized_df)
features_df.describe()

```

## Step 4: Feature Selection + Model Training 

Now we're ready to train our Machine Learning model! 🎉 Before diving in, we'll identify the best features from the features_df dataframe. This ensures we use the most relevant features for the highest accuracy while keeping the model efficient, with prediction times in the range of 10-100 microseconds.

Outputs and Visual results:
- List of Selected Features
- Folds Accuracy, Mean Folds Accuracy, Training Accuracy, Testing Accuracy
- Classification Report of Tranined Model
- Confusion Matrix
- Coorelation matrix of selected features
- Pair Plot of select features


At this stage, we support two fantastic Machine Learning models: XGBoost and Random Forest. These models are compatible for offline classification, Python-based online classification, and deployment on microcontrollers.

You’re all set to train and evaluate your model with ease and precision.

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

Here’s what you can do:
- Perform RTML in Jupyter Notebook or VSCode using Python
- Deploy RTML on ESP32, ESP8266, Arduino 33 BLE microcontrollers with the generated Classifier.h and Pipeline.h code
- Upcoming: Deploy RTML on Raspberry Pi using MicroPython (stay tuned!)

To utilize any of these deployment options, you'll need an Authentication Key from [easyRTML.com](https://easyrtml.pythonanywhere.com/)

<img width="1440" alt="Screenshot 2024-07-08 at 11 27 34 PM" src="https://github.com/easyRTML/easyRTML/assets/174990499/18616df1-3c39-4738-ac85-439331e1401e">


> <span style="background-color: #FFFF00">**Note:** Ensure you provide a valid email address and name, as your Authentication Key will be sent to the email you provide.</span>

Once you receive your Authentication Key, save it along with your email, as you'll need these details to execute the code.


### RTML code generator for Python (Jupyter Notebook & VSCode)

For Xgboost and Random Forest both trained classifier models:

```sh

"""
Python RTML Code generator
"""
from easyRTML import authenticate
email = "abc@gmail.com" #Enter your email here

#Authetication Key: 136126847XXXXXXXXXXXXX 

if authenticate(email=email):
    
    from easyRTML import pyRTML

    py_RTML = pyRTML(processor, extractor, xgml) # Change the below rfml/xgml depending upon which model been used
    
    """
    - Run the below code to access the generted python script to Execute the Real-time classification.
    - Make sure you define model_file, serial_port, baud_rate correctly.
    - Genearted code will be saved in your directory.
    """
    generated_code = py_RTML.easyRTML_python_generate(model_file="xgboost_model.pkl", serial_port='/dev/cu.usbserial-0001', baud_rate=115200)
    py_RTML.save_code_to_file(generated_code) # Save the generated code to a file
    print(generated_code)

    """
    - Run the below code if you wish to Execute the Real-time classification directly without getting generted code.
    - Make sure you comment out the above code completly.
    - Make sure you define model_file, serial_port, baud_rate correctly.
    - Genearted code will be saved in your directory.
    """
#    py_RTML.execute_generated_code(model_file="xgboost_model.pkl", serial_port='/dev/cu.usbserial-0001', baud_rate=115200) 
    
else:
    print("Access denied")

    """
    - A promt will apprear, please enter your Authetication code to proceed.
    """

```


### RTML for Microcontroller (ESP32, ESP8266, Arduino 33 BLE, etc)

To deply the Xgboost or Random Forest trained saved model, we require to generate:

- pipeline.h
- classifier.h
- Modify the Data Recording code of Arduino IDE 

### Generate Pipeline.h 

Same for both model, Xgboost and Random Forest both:

```sh

"""
pipeline.h code
"""

from easyRTML import authenticate
email = "abc@gmail.com"  #Enter your email here

#Authetication Key: 136126847XXXXXXXXXXXXX

if authenticate(email=email):
    from easyRTML import Pipe

    """
    - Change rfml/xgml depending upon which model been used.
    - Genearted code will be saved in your directory.
    """

    pipe = Pipe(processor, extractor, xgml) 
    pipe.save_cpp_code()

else:
    print("Access denied")

    """
    - A promt will apprear, please enter your Authetication code to proceed.
    """
```


### Generate Classifier.h 

For Xgboost porting:

```sh

"""
classifier.h code
"""

from easyRTML import authenticate
email = "abc@gmail.com"  #Enter your email here

#Authetication Key: 136126847XXXXXXXXXXXXX

if authenticate(email=email):
    from easyRTML import generate_code

    """
    - Make sure to import XgBoost model properly as .pkl file.
    - Genearted code will be saved in your directory.
    """

    cpp_code = generate_code("easyRTML_Xgboost", 'xgboost_model.pkl', xgml)
    print(cpp_code)

else:
    print("Access denied")
    
    """
    - A promt will apprear, please enter your Authetication code to proceed.
    """
```


For Random Forest porting:

```sh

"""
classifier.h code
"""

from easyRTML import authenticate
email = "abc@gmail.com"  #Enter your email here

#Authetication Key: 136126847XXXXXXXXXXXXX

if authenticate(email=email):
    from easyRTML import generate_code

    """
    - Make sure to import Random Forest model properly as .pkl file.
    - Genearted code will be saved in your directory.
    """

    cpp_code = generate_code("easyRTML_RandomForest", 'rf_model.pkl', rfml)
    print(cpp_code)

else:
    print("Access denied")
    
    """
    - A promt will apprear, please enter your Authetication code to proceed.
    """
```

### Modify the Data Recording code of Arduino IDE (main.ino)

Marked with "// Modified code" are the extra lines added in the data recording code which are required to integrate with classifier.h and pipeline.h code. Also Additional conditional code included to perfrom any task based upon prediction results. 

```sh
#include <Adafruit_MPU6050.h>
#include <Wire.h>
#include "pipeline.h" // Modified code

Adafruit_MPU6050 mpu;
Pipeline pipeline; // Modified code

//const int esp8266LedPin = LED_BUILTIN;

void setup() {
  Serial.begin(115200);
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
  
// Initialize ESP8266 onboard LED pin
//  pinMode(esp8266LedPin, OUTPUT);

}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  float rawData[6] = {a.acceleration.x, a.acceleration.y, a.acceleration.z, g.gyro.x, g.gyro.y, g.gyro.z}; // Modified code

  pipeline.normalizeAndBuffer(rawData); // Modified code

// Check the prediction result from Pipeline
//  String prediction = pipeline.getPrediction();
//  if (prediction == "ud") {
//    digitalWrite(esp8266LedPin, HIGH); // Turn ESP8266 LED on
//  } else {
//    digitalWrite(esp8266LedPin, LOW); // Turn ESP8266 LED off
//  }
  
}
```

This is how the Arduino IDE should look like, main.ino code, pipeline.h code and classifier.h code, all 3 in different tabs in same file.

<img width="1433" alt="Screenshot 2024-07-08 at 11 24 34 PM" src="https://github.com/easyRTML/easyRTML/assets/174990499/e30c381f-8e17-4d77-8a18-7317d70b2fe2">



