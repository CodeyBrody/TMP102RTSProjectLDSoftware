from tkinter import *

error_decoding = {
    '`': "/ COMM_ERROR: Missing Reading /",
    '*': "/ OUTLIER: Marked as Outlier /",
    '-': "/ BELOW_BOUNDS: Reading Below Sensor Operational Bounds /",
    '+': "/ ABOVE_BOUNDS: Reading Above Sensor Operational Bounds /",
}



class TMPSensorGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("TMP Sensor Data")
        self.display_temp = "00.00"

        self.sensor1_temp = "01.00"
        self.sensor2_temp = "02.00"
        self.sensor3_temp = "03.00"

        self.sensor1_err = ""
        self.sensor2_err = ""
        self.sensor3_err = ""

        self.display_temp_text = Label(text = self.display_temp)
        self.display_temp_text.grid(row=0, column = 0)

        self.sensor1_temp_text = Label(text = self.sensor1_temp)
        self.sensor1_temp_text.grid(row=1, column = 0)

        self.sensor1_err_text = Label(text = self.sensor1_err)
        self.sensor1_err_text.grid(row=1, column = 1)

        self.sensor2_temp_text = Label(text = self.sensor2_temp)
        self.sensor2_temp_text.grid(row=2, column = 0)

        self.sensor2_err_text = Label(text = self.sensor2_err)
        self.sensor2_err_text.grid(row=2, column = 1)

        self.sensor3_temp_text = Label(text = self.sensor3_temp)
        self.sensor3_temp_text.grid(row=3, column = 0)

        self.sensor3_err_text = Label(text = self.sensor3_err)
        self.sensor3_err_text.grid(row=3, column = 1)


    def update_gui(self, display_temp, sensor1_temp, sensor2_temp, sensor3_temp, sensor1_err, sensor2_err, sensor3_err):
        self.update_display_temp(display_temp)
        self.update_sensor1(sensor1_temp, sensor1_err)
        self.update_sensor2(sensor2_temp, sensor2_err)
        self.update_sensor3(sensor3_temp, sensor3_err)

    def update_display_temp(self, display_temp):
        self.display_temp_text.config(text = display_temp)

    def update_sensor1(self, sensor1_temp, sensor1_faults):
        self.sensor1_temp_text.config(text = sensor1_temp)

        if sensor1_faults == "":
            self.sensor1_err_text.config(text = sensor1_faults)
        else:
            new_sensor1_err_text = ""
            for symbol in sensor1_faults:
                new_sensor1_err_text += error_decoding[symbol]
            self.sensor1_err_text.config(text = new_sensor1_err_text)

    def update_sensor2(self, sensor2_temp, sensor2_faults):
        self.sensor2_temp_text.config(text=sensor2_temp)

        if sensor2_faults == "":
            self.sensor2_err_text.config(text = sensor2_faults)
        else:
            new_sensor2_err_text = ""
            for symbol in sensor2_faults:
                new_sensor2_err_text += error_decoding[symbol]
            self.sensor2_err_text.config(text = new_sensor2_err_text)

    def update_sensor3(self, sensor3_temp, sensor3_faults):
        self.sensor3_temp_text.config(text=sensor3_temp)

        if sensor3_faults == "":
            self.sensor3_err_text.config(text = sensor3_faults)
        else:
            new_sensor3_err_text = ""
            for symbol in sensor3_faults:
                new_sensor3_err_text += error_decoding[symbol]
            self.sensor3_err_text.config(text = new_sensor3_err_text)

