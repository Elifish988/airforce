import requests
import json
from command_goals import command_goals
from  load_functions import load_aircrafts_from_file, load_pilots_from_file, load_city_targets_from_csv
import requests

# משתנים למקרה שעוד לא הוטען הקובץ
aircraft_list = []
pilots_list = []
city_target_list = []
goals_list = []

# יצירת אינדקס
bool = True
while bool:
    chous = int(input(" אנא בחר פעולה: \n 1 - טעינת קבצים \n 2 - הצגת טבלת המלצה לתקיפות\n 3 - שמירת כל התקיפות לקובץ \n 4 - יציאה \n :"))


    if chous == 1:
        # קריאת המטוסים לליסט
        aircraft_list = load_aircrafts_from_file()

        # קריאת המטרות לליסט
        pilots_list = load_pilots_from_file()

        # קריאת  המטרות לליסט
        city_target_list = load_city_targets_from_csv()

        for aircraft in aircraft_list:
            print(f"Type: {aircraft.type}, Speed: {aircraft.speed}, Fuel Capacity: {aircraft.fuel_capacity}")

        for pilots in pilots_list:
            print(f"name: {pilots.name}, skill_level: {pilots.skill_level}")

        for city_target in city_target_list:
            print(
                f"City: {city_target.city}, Priority: {city_target.priority} ,  distanse: {city_target.distanse} , weather: {city_target.weather} , weather_conditions: {city_target.weather_conditions}")
    if chous == 2:
        # יצירת רשימת מטרות
        goals_list = command_goals(aircraft_list, pilots_list, city_target_list)
        for goals in goals_list:
            print(f" target_city: {goals.target_city},  \
             priority: {goals.priority},  \
              assigned_pilot: {goals.assigned_pilot},  \
               assigned_aircraft: {goals.assigned_aircraft},  \
                distance: {goals.distance},  \
                 weather_conditions: {goals.weather_conditions},  \
                 weather: {goals.weather},  \
                  pilot_skill: {goals.pilot_skill},  \
                   aircraft_speed: {goals.aircraft_speed},  \
                    fuel_capacity: {goals.fuel_capacity},  \
                     mission_fit_scores: {goals.mission_fit_scores}")
    if chous == 3:
        print("קובץ נטען")


    if chous == 4:
        bool = False














