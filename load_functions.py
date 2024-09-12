import json
import csv
import get_requests
import load_servis_functions
from models import Aircrafts, Pilots, CityTarget, distanse

# יוצרת רשימות על ידי קריאת הקבצים השונים

def load_aircrafts_from_file() -> list:
    filepath = r"fils\aircrafts.json"
    with open(filepath, 'r') as file:
        data = json.load(file)

    aircrafts = []
    for item in data:
        aircraft = Aircrafts.Aircraft(
            type=item['type'],
            speed=item['speed'],
            fuel_capacity=item['fuel_capacity']
        )
        aircrafts.append(aircraft)

    return aircrafts


def load_pilots_from_file() -> list:
    filepath = r"fils\pilots.json"
    with open(filepath, 'r') as file:
        data = json.load(file)

    pilots = []
    for item in data:
        aircraft = Pilots.Pilots(
            name=item['name'],
            skill_level=item['skill_level']
        )
        pilots.append(aircraft)

    return pilots


def load_city_targets_from_csv() -> list:
    city_targets = []
    filepath = r"fils\air_strike_targets.csv"

    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # יצירת המיקום של יעד התקיפה
            API_kew = "733864aba624102da7e50ae2c4b581ea"
            dic_from_request = get_requests.get_requests(row['City'], API_kew)
            #יצירת המודל
            city_target = CityTarget.CityTarget(
                city=row['City'],
                priority=int(row['Priority']),
                distanse= load_servis_functions.get_distanse(dic_from_request),
                weather= load_servis_functions.weather_score(dic_from_request),
                weather_conditions = dic_from_request["weather"]['main_weather']
            )
            city_targets.append(city_target)

    return city_targets