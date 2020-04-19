from flask import Blueprint, render_template, request, redirect
from hoti_utils import get_date_parts
from bank_holidays.bank_holidays import BankHolidays
from url_con_man.url_con_man import PoolMan
from city.city import City
from weather.weather import Weather


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates'
)


def get_message():
    message = 'this is a test message'
    return message


@bp.route('/exe2/view')
def show():
    message = ''
    return None
    # return render_template('exercise_1_view.html', division, location, holiday, year, message)


@bp.route('/exe2/get_hottest_holiday', methods=['POST', 'GET'])
def search():
    pm = PoolMan()
    hday = BankHolidays()
    weather = Weather()
    locations = City()
    # Set properties
    locations.pm = pm
    hday.pm = pm
    weather.pm = pm
    weather.holiday = hday
    # setup exports
    division_list = hday.get_divisions()
    print('Regions: %s' % division_list)
    holiday_list = hday.get_holiday_list(division_list[0])
    print('Holidays: %s' % holiday_list)

    if request.method == 'POST':
        location = request.form.get('exe2_location')
        print('location: %s' % location)
        division = request.form.get('exe2_division')
        print('division: %s' % division)
        holiday = request.form.get('exe2_holiday')
        print('Holiday: %s' % holiday)

        _woeid = locations.get_city_woeid(location)
        print('Location ID: %s' % _woeid)
        thehottestdate, max_temp = weather.get_hottest_temp_on_holiday_at_location(division, _woeid, holiday)
        message = 'The hottest [{2}] was [{4}°] on {3}'.format(division,
                                                               _woeid,
                                                               holiday,
                                                               thehottestdate,
                                                               round(max_temp))
        # '/exe2/view/'
        return render_template('exercise_2_view.html',
                               division=division,
                               location=location,
                               holiday=holiday,
                               message=message)

    return render_template('exercise_2.html', divisions=division_list, holidays=holiday_list)