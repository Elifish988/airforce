import requests
import json
from  load_functions import load_aircrafts_from_file, load_pilots_from_file, load_city_targets_from_csv
import requests
# קריאת המטוסים לליסט
aircraft_list = load_aircrafts_from_file()

for aircraft in aircraft_list:
    print(f"Type: {aircraft.type}, Speed: {aircraft.speed}, Fuel Capacity: {aircraft.fuel_capacity}")


# קריאת המטרות לליסט
pilots_list = load_pilots_from_file()

for pilots in pilots_list:
    print(f"name: {pilots.name}, skill_level: {pilots.skill_level}")

# קריאת  המטרות לליסט
city_target_list = load_city_targets_from_csv()


for city_target in city_target_list:
    print(f"City: {city_target.city}, Priority: {city_target.priority} ,  distanse: {city_target.distanse} , weather: {city_target.weather} , weather_conditions: {city_target.weather_conditions}" )







