import requests
import json
import time

TAG = "NTP"
NTP_URL = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'


def DEBUG(str):
    if False:
        print(str)


def get_time():
    response = requests.get(NTP_URL)

    data_json = json.loads(response.text)
    api = data_json['api']
    ret = data_json['ret']
    data = data_json['data']

    DEBUG(data_json)
    DEBUG(api)
    DEBUG(ret)
    DEBUG(data)

    time_stamp = int(data['t'][0:10])

    DEBUG(time_stamp)

    time_struct = time.localtime(time_stamp)

    DEBUG(time_struct)
    time_format = time.strftime('%m-%d %H:%M:%S', time_struct)
    DEBUG(time_format)
    return time_format


if __name__ == '__main__':

    time = get_time()
    print(time)