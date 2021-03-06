from coapthon.resources.resource import Resource
import ntp
import weather


class BasicResource(Resource):
    def __init__(self, name="BasicResource", coap_server=None):
        super(BasicResource, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = "Basic Resource"
        self.resource_type = "rt1"
        self.content_type = "text/plain"
        self.interface_type = "if1"

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.edit_resource(request)
        return self

    def render_POST(self, request):
        res = self.init_resource(request, BasicResource())
        return res

    def render_DELETE(self, request):
        return True

    def render_GET_advanced(self, request, response):
        pass

    def render_PUT_advanced(self, request, response):
        pass

    def render_POST_advanced(self, request, response):
        pass

    def render_DELETE_advanced(self, request, response):
        pass


class NTPResource(Resource):
    def __init__(self, name="NTPResource", coap_server=None):
        super(NTPResource, self).__init__(name, coap_server, visible=True,
                                          observable=True, allow_children=True)
        self.payload = ""

    def render_GET_advanced(self, request, response):
        return self

    def render_PUT(self, request):
        self.payload = request.payload
        return self

    def render_PUT_advanced(self, request, response):
        pass

    def render_POST(self, request):
        pass

    def render_POST_advanced(self, request, response):
        pass

    def render_DELETE(self, request):
        return True

    def render_DELETE_advanced(self, request, response):
        pass

    def render_GET(self, request):
        print(request)
        self.payload = ntp.get_time()
        return self


class WeatherNowResource(Resource):
    def __init__(self, name="WeatherNowResource", coap_server=None):
        super(WeatherNowResource, self).__init__(name, coap_server, visible=True,
                                                 observable=True, allow_children=True)
        self.payload = ""

    def render_GET_advanced(self, request, response):
        return self

    def render_PUT(self, request):
        self.payload = request.payload
        return self

    def render_PUT_advanced(self, request, response):
        pass

    def render_POST(self, request):
        pass

    def render_POST_advanced(self, request, response):
        pass

    def render_DELETE(self, request):
        return True

    def render_DELETE_advanced(self, request, response):
        pass

    def render_GET(self, request):
        self.payload = weather.get_weather_now(request.uri_query)
        print(request.uri_query)
        return self


class Weather3DResource(Resource):
    def __init__(self, name="Weather3DResource", coap_server=None):
        super(Weather3DResource, self).__init__(name, coap_server, visible=True,
                                                observable=True, allow_children=True)
        self.payload = ""

    def render_GET_advanced(self, request, response):
        return self

    def render_PUT(self, request):
        self.payload = request.payload
        return self

    def render_PUT_advanced(self, request, response):
        pass

    def render_POST(self, request):
        pass

    def render_POST_advanced(self, request, response):
        pass

    def render_DELETE(self, request):
        return True

    def render_DELETE_advanced(self, request, response):
        pass

    def render_GET(self, request):

        self.payload = weather.get_weather_3d(request.uri_query)
        print(request.uri_query)
        return self
