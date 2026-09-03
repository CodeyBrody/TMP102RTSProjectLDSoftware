import serial, os, pandas, time
import pandas as pd
import csv
from datetime import datetime
import data_logging as dl
from gui import TMPSensorGUI


AUTO_LOG_COUNT = 100

#Set up serial communication with the microcontroller
ser = serial.Serial(
    port = "COM3",
    baudrate=115200,
    timeout=1
)

#Create an empty list of data sample objects
temp_data = []

#Set up a 'GUI' object to control or access the GUI
GUI = TMPSensorGUI()

# Log the Session Start Time in the "raw_data.txt" file
dl.export_data_append(f"Session: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}", "raw_data.txt")

def refresh():
    # Receive any incoming messages from the serial communication link
    line = ser.readline().decode("utf-8").strip()

    # If the command is to send the microcontroller the time
    if line == "SEND_TIME":
        formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
        ser.write(formatted_date.encode('utf-8'))

    if line[0:2] == "D:":
        print(line)
        dl.export_data_append(line, f"raw_data.txt")

        data = dl.remove_message_type_label(line)
        sample = dl.parse_data(data)
        temp_data.append(sample)

        GUI.update_gui(
            sample.display_temp,
            str(sample.sensor1),
            str(sample.sensor2),
            str(sample.sensor3),
            sample.sensor1_err,
            sample.sensor2_err,
            sample.sensor3_err
        )

        if len(temp_data) % AUTO_LOG_COUNT == 0:
            temp_df = pd.DataFrame(temp_data)
            temp_df.to_csv("sensor_log.csv", index=False)

    # if line:
    #     print(line)

    GUI.window.after(100, refresh)

refresh()
GUI.window.mainloop()