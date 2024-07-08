import csv
import serial
import time
from tqdm import tqdm
import matplotlib.pyplot as plt
import os
import pandas as pd

class DataAQ:
    def __init__(self, **kwargs):
        """
        Initialize DataAQ class with given keyword arguments.
        Arguments:
        - filename: str, name of the file
        - serial_port: str, name of the serial port
        - baud_rate: int, baud rate for serial communication
        """
        self.filename = kwargs.get('filename', 'fsr')
        self.serial_port = kwargs.get('serial_port', '/dev/tty.usbserial-0001')
        self.baud_rate = kwargs.get('baud_rate', 115200)
        self.file = f"{self.filename}.csv"

    def plot_existing_data(self, **kwargs):
        """
        Plot existing data from the file.
        Arguments: 
        - kwargs: keyword arguments for plotting
        """
        df = pd.read_csv(self.file)
        plt.figure(figsize=kwargs.get('figsize', (15, 3)))  # Adjust figure size as needed
        df.plot(ax=plt.gca())  # Adjust x_column and y_column
        plt.xlabel(kwargs.get('xlabel', 'Samples'))  # Replace with actual labels
        plt.ylabel(kwargs.get('ylabel', 'Amplitude'))  # Replace with actual labels
        plt.title(kwargs.get('title', self.file))  # Replace with actual title
        plt.show()

    def record_data(self, **kwargs):
        """
        Record data from the serial port for a specified duration.
        Arguments:
        - kwargs: keyword arguments containing:
          - duration: int, duration of recording in seconds
          - label_name: str, name of the label
          - label_num: int, number of the label
        Returns:
        - data_rows: list, recorded data
        - sampling_freq: float, sampling frequency
        """
        duration = kwargs.get('duration', 10)
        label_name = kwargs.get('label_name', 'default_label')
        label_num = kwargs.get('label_num', 0)

        # Open serial port
        ser = serial.Serial(self.serial_port, baudrate=self.baud_rate)
      
        # Record data for the specified duration
        start_time = time.time()
        with tqdm(total=duration, desc=f'Recording for label {label_name}') as pbar:
            while time.time() - start_time < duration:
                # Read data from serial port
                line = ser.readline().decode().strip()
                data = line.split(',')  # Assuming data is comma-separated

        # Close serial port
        ser.close()

        return data_rows, sampling_freq

    def record_and_save_data(self, **kwargs):
        """
        Record and save data to a CSV file.
        Arguments:
        - kwargs: keyword arguments for recording and saving data
        """
        # Save all data to CSV file
        file_name = f"{self.filename}_{average_sampling_freq:.2f}.csv"
        with open(file_name, 'w', newline='') as csvfile:
            # Initialize CSV writer
            writer = csv.writer(csvfile)
          
        print(f"Average sampling frequency of the recorded file: {average_sampling_freq:.2f} Hz")
        print(f"All data recorded successfully and saved as '{file_name}'")
