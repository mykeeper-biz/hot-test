#!/usr/bin/env python3
import json
from os import path
from datetime import date
from hoti_utils import get_date_parts, check_date, get_file_mod_stamp
from url_con_man.url_con_man import PoolMan


def _get_datafile_name():
    return 'bank-holidays.json'


def _get_url():
    return 'https://www.gov.uk/bank-holidays.json'


class BankHolidays():
    _pm =  PoolMan()

    def __init__(self):
        pass

    # @_pm.setter
    def pm(self, value):
        self._pm = value

    def _get_holidays_data(self):
        datafile = _get_datafile_name()
        if path.exists(datafile) and path.isfile(datafile):
            # Check if valid datafile already exits
            mtime = get_file_mod_stamp(datafile)
            if date.today() == date.fromtimestamp(mtime):
                # just load the file, its from today
                return
        else:
            # load a new file from the url
            try:
                self._pm.url = _get_url()
                self._pm.action = 'GET'
                resp = self._pm.request()
                if resp.status == 200:
                    # print('jason bank holiday data loaded')
                    data_dict = json.loads(resp.data.decode('utf-8'))  # ['json']
                    with open(datafile, 'w') as outfile:
                        json.dump(data_dict, outfile)
            except Exception:
                raise Exception('Something went wrong loading data from {0}'.format(_get_url()))

    def _get_holidays(self):
        self._get_holidays_data()
        datafile = _get_datafile_name()
        try:
            # with open(datafile) as json_file:   # , encoding='raw_unicode_escape'
            #     data = json.loads(json_file)
            with open(datafile, encoding='raw_unicode_escape') as f:
                data = json.loads(f.read().encode('raw_unicode_escape').decode('utf-8'))
            return data
        except:
            raise Exception('Something went wrong loading holiday data from {0} !'.format(datafile))

    def get_divisions(self):
        data_dict = self._get_holidays()
        divi_list = []
        for divi in data_dict:
            d = data_dict[divi]['division']
            divi_list.append(d)
        print('Available divisions in the UK')
        print(divi_list)

        return divi_list

    # for DropDown
    def get_holiday_list(self, division):
        # Divisions 'england-and-wales', 'scotland', 'northern-ireland'
        data_dict = self._get_holidays()
        bankholidays_set = set()
        for divi in data_dict:
            d = data_dict[divi]['division']
            if d == division:
                events = data_dict[divi]['events']
                # using a set to automatically filter out duplicates
                for event in events:
                    bankholidays_set.add(event['title'])
        bankholidays_list = []
        if len(bankholidays_set): # Add the reduced set as a list
            for s in bankholidays_set:
                bankholidays_list.append(s)
        print('Available unique bank holidays in [{0}]'.format(division))
        print(bankholidays_list)
        return bankholidays_list

    def get_date_from_holiday_and_year(self, division, holiday, year):
        # Divisions 'england-and-wales', 'scotland', 'northern-ireland'
        # holiday, from dropdown as predefined in holiday lest
        # some bank holidays have a floating date, or is granted on a
        # separate day, if the original date is a sunday
        data_dict = self._get_holidays()
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

    def get_specific_holiday_date_list(self, division, holiday):
        # Divisions 'england-and-wales', 'scotland', 'northern-ireland'
        data_dict = self._get_holidays()
        bankholidays_list = []
        for divi in data_dict:
            d = data_dict[divi]['division']
            if d == division:
                events = data_dict[divi]['events']
                # using a set to automatically filter out duplicates
                for event in events:
                    if holiday == event['title']:
                        yy, mm, dd = get_date_parts(event['date'])
                        if check_date(yy, mm, dd):  # If this is a valid past date, add it
                            bankholidays_list.append(event['date'])
        print('{0} fell on the following dates:'.format(holiday))
        print(bankholidays_list)
        return bankholidays_list
