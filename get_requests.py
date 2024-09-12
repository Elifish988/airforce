import requests
import json



# מציאת מיקום ומזג אויר
def get_requests(citi_name, API_kew:str) -> dict:
    request = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={citi_name}&appid={API_kew}')
    data = request.json()

    dic ={
        "weather" : {
            "main_weather": data["list"][0]["weather"][0]["main"],
            "clouds" : data["list"][0]["clouds"]["all"],
            "speed_wind" : data["list"][0]["wind"]["speed"],
            "dt_txt": data["list"][0]["dt_txt"]
        },
        "loction" : {
            "lat": data["city"]["coord"]["lat"],
            "lon": data["city"]["coord"]["lon"]
        }

    }

    return dic


