from models import Aircrafts, Pilots, CityTarget, Command_goals
import main


# יוצר רשימה בעלת כל האופציות האפשריות למטרה
def command_goals():
    goals_list = []
    for aircraft in main.aircraft_list:
        for pilot in main.pilots_list:
            for city_target in  main.city_target_list:
                goals = Command_goals.Command_goals(
                    target_city = city_target[]
                    priority = priority
                    assigned_aircraft = assigned_aircraft
                    distance = distance
                    weather_conditions = weather_conditions
                    pilot_skill = pilot_skill
                    aircraft_capacity = aircraft_capacity
                    fuel_capacity = fuel_capacity
                    mission_fit_scores = mission_fit_scores
                )
                goals_list.append(goals)


