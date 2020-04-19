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


@bp.route('/exe1/view')
def show():
    message = ''
    return render_template('exercise_1_view.html', division, location, holiday, year, message)


@bp.route('/exe1/get_one_holiday', methods=['POST', 'GET'])
def search():
    # Create objects
    pm = PoolMan()
    locations = City()
    hday = BankHolidays()
    weather = Weather()
    # Set properties
    locations.pm = pm
    hday.pm = pm
    weather.pm = pm
    weather.holiday = hday

    # setup exports
    division_list = hday.get_divisions()
    holiday_list = hday.get_holiday_list(division_list[1])
    _datelist = hday.get_specific_holiday_date_list(division_list[1], holiday_list[1])
    print('Dates: %s' % _datelist)
    year_list = []
    for d in _datelist:
        y, m, d = get_date_parts(d)
        year_list.append(y)
    print('years: %s' % year_list)

    if request.method == 'POST':
        location = request.form.get('exe1_location')
        print('location: %s' % location)
        division = request.form.get('exe1_division')
        print('division: %s' % division)
        holiday = request.form.get('exe1_holiday')
        print('holiday: %s' % holiday)
        the_year = request.form.get('exe1_year')
        print('year: %s' % the_year)

        yy, mm, dd = hday.get_date_from_holiday_and_year(division, holiday, the_year)
        woeid = locations.get_city_woeid(location)
        maxtemp, mintemp = weather.get_weather_on_day(woeid, yy, mm, dd)
        message = 'Min {1}° and max {0}° temperature in Liverpool on {2}/{3}/{4}'.format(round(maxtemp, 4), round(mintemp, 4), yy, mm, dd)
        # '/exe1/view/'
        return render_template('exercise_1_view.html',
                               division=division,
                               location=location,
                               holiday=holiday,
                               year=the_year,
                               message=message)

    return render_template('exercise_1.html',
                           divisions=division_list,
                           holidays=holiday_list,
                           years=year_list)


# @bp.route('/view/<hoti_id>')
# def view(hoti_id):
#     return render_template('hoti_view.html', hoti=get_hoti_by_id(hoti_id))


# # Load the file into memory
# with open("servers.json", "r") as f:
#     data = json.load(f)

# Return the JSON in the template#
#  @app.route("/")
# def index():
#    return render_template("index.html", servers=data)


# /Users/user/.local/share/virtualenvs/hot-instinet-gStob4mw
# (
