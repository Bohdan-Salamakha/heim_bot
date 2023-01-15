import googlemaps

from core.settings import GOOGLE_MAPS_API_KEY


class GoogleMapsRouteBuilder:
    def __init__(self, from_, to_):
        # print(f'FROM: {from_}')
        # print(f'TO: {to_}')
        self.__from_ = from_
        self.__to_ = to_
        self.__client: googlemaps.client.Client = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

    def get_route_url(self) -> str:
        location_from = self.__client.geocode(self.__from_)[0].get('geometry').get('location')
        location_to = self.__client.geocode(self.__to_)[0].get('geometry').get('location')
        url = self.__build_url(location_from, location_to)
        return url

    @staticmethod
    def __build_url(coords_from, coords_to) -> str:
        lat_from, lng_from = coords_from.get('lat'), coords_from.get('lng')
        lat_to, lng_to = coords_to.get('lat'), coords_to.get('lng')
        url_api = "https://www.google.com/maps/dir/?api=1&" \
                  f"origin={lat_from},{lng_from}&" \
                  f"destination={lat_to},{lng_to}&" \
                  "travelmode=driving"
        # print(url_api)
        return url_api
