#!/usr/bin/env python3
import json

import certifi
import urllib3

from hoti_utils import get_date_parts, check_date


def getUrl():
    return 'https://www.gov.uk/bank-holidays.json'


def getHolidays():
    bankholidays_url = getUrl()

    try:
        # Set up the pool mannager session
        http = urllib3.PoolManager(ca_certs=certifi.where())
        resp = http.request('GET', bankholidays_url)

        if resp.status == 200:
            # print('jason bank holiday data loaded')
            data_dict = json.loads(resp.data.decode('utf-8'))  # ['json']
            # print(data_dict)
            return data_dict
    except:
        raise Exception('Something went wrong!')


def getDivision(division):
    data_dict = getHolidays()
    divi_list = []
    for divi in data_dict:
        d = data_dict[divi]['division']
        divi_list.append(d)
        print(division)

    print('Available divisions in the UK [{0}]'.format(divi_list))
    return divi_list


# for DropDown
def getHolidayList(division):
    # Divisions 'england-and-wales', 'scotland', 'northern-ireland'
    data_dict = getHolidays()
    bankholidays_set = set()

    for divi in data_dict:
        d = data_dict[divi]['division']
        if d == division:
            events = data_dict[divi]['events']
            # using a set to automatically filter out duplicates
            for event in events:
                bankholidays_set.add(event['title'])

    bankholidays_list = []
    if len(bankholidays_set):
        for s in bankholidays_set:
            bankholidays_list.append(s)

    print('Available unique bank holidays in  [{0}]'.format(bankholidays_list))
    return bankholidays_list


def getDateFromeHolidayAndYear(division, holiday, year):
    # Divisions 'england-and-wales', 'scotland', 'northern-ireland'
    # holiday, from dropdown as predefined in holiday lest
    # some bank holidays have a floating date, or is granted on a
    # separate day, if the original date is a sunday

    data_dict = getHolidays()

    for divi in data_dict:
        d = data_dict[divi]['division']
        if d == division:
            events = data_dict[divi]['events']
            # using a set to automatically filter out duplicates
            for event in events:
                if event['title'] == holiday:
                    yyyy, mm, dd = get_date_parts(event['date'])
                    if yyyy == year:
                        return '{0}/{1}/{2}'.format(yyyy, mm, dd)
    return ''


def getSpecificHolidayDateList(division, holiday):
    # Divisions 'england-and-wales', 'scotland', 'northern-ireland'
    data_dict = getHolidays()
    bankholidays_list = []
    for divi in data_dict:
        d = data_dict[divi]['division']
        if d == division:
            events = data_dict[divi]['events']
            # using a set to automatically filter out duplicates
            for event in events:
                if holiday == event['title']:
                    yy, mm, dd = get_date_parts(event['date'])
                    if check_date(yy, mm, dd): # If this is a valid past date, add it
                        bankholidays_list.append(event['date'])
    print('{0} fell on the following dates [{1}]'.format(holiday, bankholidays_list))
    return bankholidays_list


def getDebug():
    # e = data_dict['england-and-wales']
    # s = data_dict['scotland']
    # ni = data_dict['northern-ireland']
    data_dict = getHolidays()
    for divi in data_dict:
        division = data_dict[divi]['division']
        print(division)
        events = data_dict[divi]['events']
        print(events)
        for event in events:
            title = event['title']
            date = event['date']
            # notes = event['notes']
            # bunting = event['bunting']
            print(title, ": ", date)

            # 'england-and-wales', 'scotland', 'northern-ireland'
            #
            #   'england-and-wales': {
            #     'division': 'england-and-wales',
            #     'events': [
            #       {
            #         'title': 'New Year’s Day',
            #         'date': '2015-01-01',
            #         'notes': '',
            #         'bunting': True
            #       },
# print(getHolidays())
