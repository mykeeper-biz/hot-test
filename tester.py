from city.city import getCityId
from hoti_utils import get_date_parts, check_date

from weather.weather import get_weather_on_day
from weather.weather import get_hottest_temp_on_holidat_at_location

division = 'england-and-wales'  # Divisions 'england-and-wales', 'scotland', 'northern-ireland''
location = 'Liverpool'
Holiday = "New Year’s Day"
woeid = getCityId(location)
y, m, d = get_date_parts('2019-12-26')

# Exersize 1
maxtemp, mintemp = get_weather_on_day(woeid, y, m, d)
print(
    'Min {1} and max {0} temperature in Liverpool on {2}/{3}/{4}'.format(round(maxtemp, 4), round(mintemp, 4), y, m, d))

# Exersize 2
thehottestdate, max_temp = get_hottest_temp_on_holidat_at_location(division, woeid, Holiday)
print('The hottest [{2}] was [{4}°] on {3}'.format(division, woeid, Holiday, thehottestdate, round(max_temp)))
