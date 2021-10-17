import requests
import json

TAG = "WEATHER"
WEATHER_URL_3D = 'https://devapi.qweather.com/v7/weather/3d?'
WEATHER_URL_NOW = 'https://devapi.qweather.com/v7/weather/now?'


def DEBUG(str):
    if True:
        print(str)


def get_weather_3d(location, key, lang='zh', unit='m'):
    data = {}
    list_daily = []
    data_daily = {}
    url = WEATHER_URL_3D+"location="+location + "&key="+key + "&lang="+lang + "&unit="+unit
    DEBUG(url)
    response = requests.get(url)
    DEBUG(response.text)
    data_json = json.loads(response.text)
    code = data_json['code']
    data['code'] = code
    if code != "200":
        return str(data)
    daily = data_json['daily']
    for d in daily:
        data_daily['fxDate'] = d['fxDate']
        data_daily['tempMin'] = d['tempMin']
        data_daily['tempMax'] = d['tempMax']
        data_daily['iconDay'] = d['iconDay']
        data_daily['textDay'] = d['textDay']
        list_daily.append(data_daily)
    data['daily'] = list_daily
    return str(data)


def get_weather_now(location, key, lang='zh', unit='m', gzip='n'):
    data = {}
    url = WEATHER_URL_NOW + "location=" + location + "&key=" + key + "&lang=" + lang + "&unit=" + unit + "&gzip=" + gzip
    DEBUG(url)
    response = requests.get(url)
    DEBUG(response.text)
    data_json = json.loads(response.text)
    code = data_json['code']
    data['code'] = code
    if code != "200":
        return str(data)

    now = data_json['now']
    temp = now['temp']  # 温度
    icon = now['icon']
    text = now['text']  # 天气状况 -> 晴
    humidity = now['humidity']  # 湿度

    data['temp'] = temp
    data['icon'] = icon
    data['text'] = text
    data['humidity'] = humidity
    return str(data)



if __name__ == '__main__':
    # weather = get_weather_now("117.282488,31.775297", "9e54b1e3d00e4f36b813065e30b0eec7")
    # print(weather)
    weather = get_weather_3d("117.282488,31.775297", "9e54b1e3d00e4f36b813065e30b0eec7")
    print(json.dumps(weather))

