#!/usr/bin/env python3

import json

import certifi
import urllib3


def getCityIdUrl(city):
    return 'https://www.metaweather.com/api/location/search/?query={0}'.format(city)


def getCityId(city):
    cityUrl = getCityIdUrl(city)

    # print('Looking up {0}'.format(city))
    try:
        # Set up the pool mannager session
        http = urllib3.PoolManager(ca_certs=certifi.where())
        resp = http.request('GET', cityUrl)

        if resp.status == 200:
            data_dict = json.loads(resp.data.decode('utf-8'))  # ['json']
            if data_dict != []:
                return data_dict[0]['woeid']
    except:
        raise Exception('Something went wrong!')

#    else:
#        print('Return code is [{0}] message is [{1}]'.format(rs,resp.data.decode('utf-8')))
#        return data_dict[0]

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
# woeid = getCityId(city)
# if woeid:
#     print(woeid)
# else:
#     print('Location not registered in database')
