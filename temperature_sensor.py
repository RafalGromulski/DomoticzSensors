import pandas as pd
# import matplotlib.pyplot as plt

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)

bedroom_sensor = r"./last_year_room.csv"
hall_sensor = r"./last_year_hall.csv"
bathroom_sensor = r"./last_year_bathroom.csv"

bedroom = pd.read_csv(bedroom_sensor, delimiter=";", parse_dates=["DateTime"])
hall = pd.read_csv(hall_sensor, delimiter=";", parse_dates=["DateTime"])
bathroom = pd.read_csv(bathroom_sensor, delimiter=";", parse_dates=["DateTime"])

bedroom = bedroom.set_index("DateTime")
hall = hall.set_index("DateTime")
bathroom = bathroom.set_index("DateTime")

bedroom.columns = ["Humidity", "Average_temperature", "Min_temperature", "Max_temperature"]
hall.columns = ["Humidity", "Average_temperature", "Min_temperature", "Max_temperature"]
bathroom.columns = ["Humidity", "Average_temperature", "Min_temperature", "Max_temperature"]

# print(bedroom)
# print(hall)
# print(bathroom)
