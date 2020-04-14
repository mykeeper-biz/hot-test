import json
import os
import random
from string import ascii_lowercase
from datetime import date


DB_FILENAME = 'database.json'

def check_date(y, m, d):
    if 2015 < int(y) <= int(date.today().year):
        if int(m) <= int(date.today().month):
            if int(d) <= int(date.today().day):
                return True
            else:
                return False
    else:
        return False


def get_date_parts(d):
    # assuming dates presented as '2015-01-01' or '2015/01/01'
    # yyyy, mm, dd = get_date_parts(date)
    sep = ''
    if d.find('/') > 0:
        sep = '/'
    elif d.find('-') > 0:
        sep = '-'
    yyyy, mm, dd = d.split(sep)
    return yyyy, mm, dd


def _generate_id():
    return ''.join([
        random.choice(ascii_lowercase + '1234567890')
        for i in range(16)
    ])


def get_hotties():
    if not os.path.isfile(DB_FILENAME):
        return []

    return json.loads(open(DB_FILENAME).read())


def get_hoti_by_id(hoti_id):
    hotties = list(filter(lambda x: x['id'] == hoti_id, get_hotties()))
    return hotties[0] if hotties else None


def create_hoti(title, content):
    hotties = get_hotties()
    hoti = dict(
        id=_generate_id(),
        title=title,
        content=content
    )
    hotties.append(hoti)

    open(DB_FILENAME, 'w+').write(json.dumps(hotties))

    return hoti


def delete_hoti():
    pass

# print(_generate_id())
