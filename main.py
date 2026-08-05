import serial, os, pandas, time
from datetime import datetime
import data_logging as dl

#Set up serial communication with the microcontroller
ser = serial.Serial(
    port = "COM3",
    baudrate=115200,
    timeout=1
)

#Create an empty list of data sample objects
temp_data = []

while True:
    #Recieve any incoming messages from the serial communication link
    line = ser.readline().decode("utf-8").strip()

    #If the command is to send the microcontroller the time
    if line == "SEND_TIME":
        formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for num in range(0,2):
            ser.write(formatted_date.encode('utf-8'))


    if line[0:2] == "D:":
        data = dl.remove_message_type_label(line)
        sample = dl.parse_data(data)
        temp_data.append(sample.print_data())
        sample.print_data()

    # if line:
    #     print(line)

#
# while True:
#     line = ser.readline().decode("utf-8").strip()
#
#     if line:
#         print(line)