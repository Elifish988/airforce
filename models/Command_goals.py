class Command_goals:
    def __init__(self, target_city: str, priority: int\
                 , assigned_pilot: str, assigned_aircraft: str\
                 , distance: float, weather_conditions: str\
                 ,weather: float, pilot_skill: float\
                 , aircraft_speed: float, fuel_capacity: float\
                 , mission_fit_scores: float):
        self.target_city = target_city
        self.priority = priority
        self.assigned_pilot = assigned_pilot
        self.assigned_aircraft = assigned_aircraft
        self.distance = distance
        self.weather_conditions = weather_conditions
        self.weather = weather
        self.pilot_skill = pilot_skill
        self.aircraft_speed = aircraft_speed
        self.fuel_capacity = fuel_capacity
        self.mission_fit_scores = mission_fit_scores