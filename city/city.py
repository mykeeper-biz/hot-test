#!/usr/bin/env python3
from url_con_man.url_con_man import PoolMan
import json
from url_con_man.url_con_man import PoolMan


class City():
    _pm = PoolMan()

    def __init__(self):
        pass

    # @_pm.setter
    def pm(self, value):
        self._pm = value

    def _get_city_woeid_url(self, location):
        return 'https://www.metaweather.com/api/location/search/?query={0}'.format(location)

    def get_city_woeid(self, location):
        try:
            # Set up the pool mannager session
            self._pm.action = 'GET'
            self._pm.url = self._get_city_woeid_url(location)
            resp = self._pm.request()
            data_dict = json.loads(resp.data.decode('utf-8'))
            if data_dict:
                return data_dict[0]['woeid']
            else:
                return None
        except Exception:
            raise Exception('Something went wrong getting the location id for {0}!'.format(location))

        # [{
        # 'title': 'Liverpool',
        # 'location_type': 'City',
        # 'woeid': 26734,
        # 'latt_long': '53.409771,-2.978480'
        # }]

        # city = 'Aalborg' # []
        # city = 'Liverpool' # 26734
        # city = 'Birmingham' # 12723
        # city = 'Penzance'  # 31889
        # city = 'Edinburgh'  # 19344
        # city = 'Belfast' # 44544
        # woeid = get_city_woeid(city)
