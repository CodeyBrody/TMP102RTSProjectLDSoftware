from dataclasses import dataclass
import csv
from datetime import datetime
from math import nan

@dataclass
class Sample:

    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    display_temp: float = nan
    sensor_1: float = nan
    sensor_2: float = nan
    sensor_3: float = nan

    def print_data(self):
        print("Time:", self.timestamp, "Display Temp:", self.display_temp, "Sensor 1:", self.sensor_1, "Sensor 2:", self.sensor_2, "Sensor 3:", self.sensor_3, "\n")

def parse_data(data: str):
    sample = Sample()

    data_dict = {}

    data_list = [d.strip() for d in data.split(",")]
    attribute_list = ["timestamp", "display_temp", "sensor_1", "sensor_2", "sensor_3", "sensor_1_err", "sensor_2_err", "sensor_3_err"]
    string_attribute_list = ["timestamp", "sensor_1_err", "sensor_2_err", "sensor_3_err"]
    float_attribute_list = ["display_temp", "sensor_1", "sensor_2", "sensor_3"]

    for num in range(0, len(attribute_list)):
        data_dict[attribute_list[num]] = data_list[num]

    for key, value in data_dict.items():
        if key in float_attribute_list:
            setattr(sample, key, float(value))
        elif key in string_attribute_list:
            setattr(sample, key, value)
        else:
            print("Key Missing from {type}_attribute_list lists")

    return sample

def remove_message_type_label(string: str):
    return string[3:]

def export_data(samples, filename):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for s in samples:
                writer.writerow([s])
        print(f"'{filename}' created successfully.")
    except csv.Error as e:
        print(f"Error writing to file: {e}")

def export_data_append(sample, filename):
    try:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow([sample])
        print(f"'{filename}' appended to successfully.")
    except csv.Error as e:
        print(f"Error appending to file: {e}")

def log_dataframe(df, filename):
    df.to_csv(filename, index=False)
