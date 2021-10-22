#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from coapthon.server.coap import CoAP
from coap_api import NTPResource, Weather3DResource, WeatherNowResource
import threading

HOST = "0.0.0.0"
PORT = 5683


class CoAPServer(CoAP, threading.Thread):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        threading.Thread.__init__(self)
        self.add_resource('weather/3d/', Weather3DResource())
        self.add_resource('weather/now/', WeatherNowResource())
        self.add_resource('ntp/', NTPResource())

    def run(self):
        print("Server Start")
        try:
            self.listen()
        except KeyboardInterrupt:
            print("Server Shutdown")
            self.close()
            print("Exiting...")


if __name__ == '__main__':
    t = CoAPServer(HOST, PORT)
    t.start()

    while True:
        pass



