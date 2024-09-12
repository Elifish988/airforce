import get_requests
from models import distanse

API_kew = "733864aba624102da7e50ae2c4b581ea"
# יצירת המיקום של ירושלים
dic_from_Jerusalem = get_requests.get_requests("Jerusalem", API_kew)
let1 = dic_from_Jerusalem['loction']['lat']
lon1 = dic_from_Jerusalem['loction']['lon']

#קבלת המרחק מירושלים ליעד
def get_distanse(dic_from_request):

    let2 = dic_from_request['loction']['lat']
    lon2 = dic_from_request['loction']['lon']
    return distanse.haversine_distance(let1, lon1, let2, lon2)

#קבלת חומרת מזג האוויר
def weather_score(dic_from_request):
    weather = dic_from_request["weather"]['main_weather']
    if weather == "Clear":
        return 1.0
    elif weather == "Clouds":
        return 0.7
    elif weather == "Rain":
        return 0.4
    elif weather == "Stormy":
        return 0.2
    else:
        return 0