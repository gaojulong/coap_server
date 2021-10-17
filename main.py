#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from coapthon.server.coap import CoAP
from coap_api import NTPResource, Weather3DResource, WeatherNowResource


Host = "0.0.0.0"  		# 本机IP地址
Port = 5683             # 端口号


class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('weather', Weather3DResource())
        self.add_resource('weather', WeatherNowResource())
        self.add_resource('ntp', NTPResource())


def main():
    print("CoAPServer IP addr : %s port : %d " % (Host, Port))
    server = CoAPServer(Host, Port)
    try:
        server.listen()
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")


if __name__ == '__main__':
    main()
