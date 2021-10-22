import requests
import json

TAG = "WEATHER"
WEATHER_URL_3D = 'https://devapi.qweather.com/v7/weather/3d?'
WEATHER_URL_NOW = 'https://devapi.qweather.com/v7/weather/now?'


def DEBUG(str):
    if False:
        print(str)


def get_weather_3d(uri_query):
    data = {}
    list_daily = []
    # data_daily = {}
    url = WEATHER_URL_3D + uri_query
    DEBUG(url)
    response = requests.get(url)
    DEBUG(response.text)
    data_json = json.loads(response.text)
    code = data_json['code']
    data['code'] = code
    if code != "200":
        data = json.dumps(data, ensure_ascii=False)
        return data
    daily = data_json['daily']
    for d in daily:
        data_daily = {}
        data_daily['fxDate'] = d['fxDate']
        data_daily['tempMin'] = d['tempMin']
        data_daily['tempMax'] = d['tempMax']
        data_daily['iconDay'] = d['iconDay']
        data_daily['textDay'] = d['textDay']
        list_daily.append(data_daily)
        # data_daily.clear()
        data['daily'] = list_daily
    data = json.dumps(data, ensure_ascii=False)
    return data


def get_weather_now(uri_query):
    data = {}
    url = WEATHER_URL_NOW + uri_query
    DEBUG(url)
    response = requests.get(url)
    DEBUG(response.text)
    data_json = json.loads(response.text)
    code = data_json['code']
    data['code'] = code
    if code != "200":
        data = json.dumps(data, ensure_ascii=False)
        return data

    now = data_json['now']
    temp = now['temp']  # 温度
    icon = now['icon']
    text = now['text']  # 天气状况 -> 晴
    humidity = now['humidity']  # 湿度

    data['temp'] = temp
    data['icon'] = icon
    data['text'] = text
    data['humidity'] = humidity
    data = json.dumps(data, ensure_ascii=False)
    return data