#!/usr/bin/env python3

import json
import certifi
import urllib3
from bank_holidays.bank_holidays import getSpecificHolidayDateList
from hoti_utils import get_date_parts, check_date


def get_weather_url(woeid, y, m, d):
    return 'https://www.metaweather.com/api/location/{0}/{1}/{2}/{3}'.format(woeid, y, m, d)


def get_weather_on_day(woeid, y, m, d):
    # check valid date, must be before tomorrow
    if check_date(y, m, d):
        raise Exception('There is no data in teh database for [{0}/{1}/{2}]'.format(y, m, d))
    weather_base_url = get_weather_url(woeid, y, m, d)
    try:
        # Set up the pool mannager session
        http = urllib3.PoolManager(ca_certs=certifi.where())
        resp = http.request('GET', weather_base_url)
        if resp.status == 200:
            # print('Data for {0}/{1}/{2}/{3}'.format(woeid, year, month, date))
            data_dict = json.loads(resp.data.decode('utf-8'))  # ['json']
            # print(data_dict)
            # set an unlikely min and max temperature to start the loop.
            min_temp = 200.0
            max_temp = -200.0
            for t in data_dict:
                min = t['min_temp']
                max = t['max_temp']
                if min_temp > min:
                    min_temp = min
                if max_temp < max:
                    max_temp = max
    except:
        raise Exception('Something went wrong getting min and max temp for [{0}/{1}/{2}/{3}]'.format(woeid, y, m, d))
    return max_temp, min_temp


def get_hottest_temp_on_holidat_at_location(division, woeid, holiday):
    # Data is only available in this range  ['2015','2016','2017','2018','2019']:
    # returns thehottestdate, max_temp
    dates = getSpecificHolidayDateList(division, holiday)
    thehottestdate = ''
    for d in dates:
        year, month, date = get_date_parts(d)
        weather_base_url = get_weather_url(woeid, year, month, date)
        try:
            # Set up the pool mannager session
            http = urllib3.PoolManager(ca_certs=certifi.where())
            resp = http.request('GET', weather_base_url)
            if resp.status == 200:
                # print('Data for {0}/{1}/{2}/{3}'.format(woeid, year, month, date))
                data_dict = json.loads(resp.data.decode('utf-8'))  # ['json']
                # print(data_dict)
                # set an unlikely min and max temperature to start the loop.
                max_temp = -200.0
                for t in data_dict:
                    max = t['max_temp']
                    if max_temp < max:
                        thehottestdate = d
                        max_temp = max
        except:
            raise Exception(
                'Something went wrong getting min and max temp for [{0}/{1}/{2}/{3}]'.format(woeid, year, month, date))
    return thehottestdate, max_temp
