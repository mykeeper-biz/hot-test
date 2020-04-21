# from city.city import get_city_woeid
# from hoti_utils import get_date_parts, check_date

# from weather.weather import get_weather_on_day
# from weather.weather import get_hottest_temp_on_holiday_at_location
#####################################################
from hoti_utils import get_date_parts
from bank_holidays.bank_holidays import BankHolidays
from url_con_man.url_con_man import PoolMan
from city.city import City
from weather.weather import Weather

class Tester():
    _pm = None
    _locations = None
    _hday = None
    _weather = None

    def __init__(self):
        self._pm = PoolMan()
        self._locations = City()
        self._hday = BankHolidays()
        self._weather = Weather()
        self._locations.pm = self._pm
        self._hday.pm = self._pm
        self._weather.pm = self._pm
        self._weather.holiday = self._hday


    def run_exe1(self, division, location, bhday, the_year):
        # Exersize 1
        woeid = self._locations.get_city_woeid( location )
        the_date = self._hday.get_date_from_holiday_and_year(division, bhday,the_year)
        y, m, d = get_date_parts(the_date)     # '2019-12-26'

        maxtemp, mintemp = self._weather.get_weather_on_day(woeid, y, m, d)
        print('Min {1}° and max {0}° temperature\
               in Liverpool on {2}/{3}/{4}'.format(round(maxtemp, 4),
                                                   round(mintemp, 4),
                                                   y, m, d))

    def run_exe2(self, division, location, bhday):
        # Exersize 2
        woeid = self._locations.get_city_woeid( location )
        thehottestdate, max_temp = self._weather.get_hottest_temp_on_holiday_at_location(division, woeid, bhday)
        print('The hottest [{2}] was [{4}°] on {3}'.format(division,
                                                           woeid,
                                                           the_day,
                                                           thehottestdate,
                                                           round(max_temp)))


division = 'england-and-wales'  # Divisions 'england-and-wales', 'scotland', 'northern-ireland''
location = 'Liverpool'
the_day = "New Year’s Day"
the_year = '2015'
t = Tester()

t.run_exe1(division, location, the_day, the_year)

t.run_exe2(division, location, the_day)
