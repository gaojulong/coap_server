import requests
import json

TAG = "WEATHER"
WEATHER_URL_3D = 'https://devapi.qweather.com/v7/weather/3d?'
WEATHER_URL_NOW = 'https://devapi.qweather.com/v7/weather/now?'


def DEBUG(str):
    if True:
        print(str)


def get_weather_3d(location, key, lang='zh', unit='m'):
    url = WEATHER_URL_3D+"location="+location + "&key="+key + "&lang="+lang + "&unit="+unit
    DEBUG(url)
    response = requests.get(url)
    DEBUG(response.text)
    data_json = json.loads(response.text)
    return data_json


def get_weather_now(location, key, lang='zh', unit='m', gzip='n'):
    url = WEATHER_URL_NOW + "location=" + location + "&key=" + key + "&lang=" + lang + "&unit=" + unit + "&gzip=" + gzip
    DEBUG(url)
    response = requests.get(url)
    DEBUG(response.text)
    data_json = json.loads(response.text)
    return data_json


# 只返回所需要的天气数据
def get_weather(location, key, lang='zh', unit='m', gzip='n'):
    success_data = ""
    error_data = "error"
    weather_3d = get_weather_3d(location, key, lang, unit)
    weather_now = get_weather_now(location, key, lang, unit, gzip)

    code_3d = weather_3d['code']
    code_now = weather_now['code']

    if (code_3d != "200") or (code_now != "200"):
        return error_data

    now = weather_now['now']
    temp = now['temp']              # 温度
    icon = now['icon']
    text = now['text']              # 天气状况 -> 晴
    # windDir = now['windDir']        # 风向
    # windScale = now['windScale']    # 风力等级
    humidity = now['humidity']      # 湿度
    precip = now['precip']          # 降雨量
    pressure = now['pressure']      # 大气压

    DEBUG(now)
    DEBUG("温度:"+temp)
    DEBUG("icon"+icon)
    DEBUG("天气状况"+text)
    DEBUG("湿度"+humidity)
    DEBUG("降雨量"+precip)
    DEBUG("大气压"+pressure)

    dailys = weather_3d['daily']
    for daily in dailys:
        DEBUG(daily)

    return success_data


if __name__ == '__main__':
    weather = get_weather("101010100", "9e54b1e3d00e4f36b813065e30b0eec7")
    print(weather)
