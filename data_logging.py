from dataclasses import dataclass
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
    attribute_list = ["timestamp", "display_temp", "sensor_1", "sensor_2", "sensor_3"]
    string_attribute_list = ["timestamp"]
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
