from models import Aircrafts, Pilots, CityTarget, Command_goals



# יוצר רשימה בעלת כל האופציות האפשריות למטרה
def command_goals(aircraft_list, pilots_list, city_target_list):
    goals_list = []
    for city_target in city_target_list:
        for pilot in pilots_list:
            for aircraft in aircraft_list:
                goals = Command_goals.Command_goals(
                    target_city = city_target.city,
                    priority = city_target.priority,
                    assigned_pilot = pilot.name,
                    assigned_aircraft = aircraft.type,
                    distance = city_target.distanse,
                    weather_conditions = city_target.weather_conditions,
                    weather = city_target.weather,
                    pilot_skill = pilot.skill_level,
                    aircraft_speed = aircraft.speed,
                    fuel_capacity = aircraft.fuel_capacity,
                    mission_fit_scores = mission_fit_scores\
                        (score_distance(city_target_list , city_target.distanse)\
                         , score_aircraft_type(aircraft_list, aircraft.fuel_capacity )\
                         , score_pilot_skill(pilots_list, pilot.skill_level)\
                         , score_weather_conditions(city_target_list, city_target.weather)\
                         , score_execution_time()\
                         , score_priority(city_target_list, city_target.priority))
                )
                goals_list.append(goals)

    goals_list.sort(key=lambda x: x.mission_fit_scores , reverse=True)
    return goals_list


# מייצרת ציוני התאמה למשימה
def mission_fit_scores(distanse, aircraft_type, pilot_skill, weather_conditions, execution_time, priority):
    mission_fit_scores = ((distanse * 0.15)/
           + (aircraft_type * 0.20)/
           + (pilot_skill * 0.20)/
           + (weather_conditions * 0.20)/
           + (execution_time * 0.10)/
           + (priority * 0.15))
    return mission_fit_scores * 1000

# פןנקציית עזר ליצירת ציון ספציפי מאחד עד עשר עבור כל פרמטר

def score_distance(city_target_list, distanse):
    max_skill_level = max(city_target_list, key=lambda x: x.distanse)
    return (float(distanse)/ float(max_skill_level.distanse)) *10


def score_aircraft_type(aircraft_list, fuel_capacity):
    max_fuel_capacity = max(aircraft_list, key=lambda x: x.fuel_capacity)
    return (float(fuel_capacity) / float(max_fuel_capacity.fuel_capacity)) * 10

def score_pilot_skill(pilots_list, pilot_skill):
    max_pilot_skill = max(pilots_list, key=lambda x: x.skill_level)
    return (float(pilot_skill) / float(max_pilot_skill.skill_level)) * 10

def score_weather_conditions(city_target_list, weather):
    max_city_target_list = max(city_target_list, key=lambda x: x.weather)
    return (float(weather) / float(max_city_target_list.weather)) * 10

def score_execution_time():
    return 100


def score_priority(city_target_list, priority):
    max_priority = max(city_target_list, key=lambda x: x.priority)
    return (float(priority) / float(max_priority.priority)) * 10


