# from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource


class WeatherResource(Resource):
    def __init__(self, name="WeatherResource", coap_server=None):
        super(WeatherResource, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)

        self.payload = "Weather Resource"

    def render_GET_advanced(self, request, response):
        return self

    def render_PUT(self, request):
        self.payload = request.payload
        return self

    def render_PUT_advanced(self, request, response):
        pass

    def render_POST(self, request):
        res = WeatherResource()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_POST_advanced(self, request, response):
        pass

    def render_DELETE(self, request):
        return True

    def render_DELETE_advanced(self, request, response):
        pass

    def render_GET(self, request):
        return self

