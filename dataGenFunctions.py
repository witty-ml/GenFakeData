# files that holds functions to generate test data
# python 3
import pandas as pd
import random as rd
import names
from datetime import datetime
import radar
import usernameLists as usl
import emailDomains as ed
from faker import Factory # pip install Faker
import rstr # pip install rstr


fake = Factory.create()


def assign_gender():
    number = rd.randint(0,1)  # generate a random number to decide gender
    # gender deciding logic
    if number is 0:
        return 'female'
    else:
        return 'male'


def assign_first_name(gender):
    # just pass function gender cell value or a gender
    # must be of form 'female' or 'male'
    return names.get_first_name(gender=gender)


def assign_last_name():
    return names.get_last_name()


def gen_date():
    # generate a random date over a range
    randomdate = radar.random_datetime(
        start=datetime(year=1998, month=1, day=1),
        stop=datetime(year=2017, month=6, day=16)
    )
    # returning random formats
    # TODO add more formats
    formats = { 1: "%Y-%m-%d %H:%M:%S",
                2: '%m/%d/%Y %I:%M %p',
                3: '%b %d, %Y',
                4: '%m-%d-%Y',
                5: '%m/%d/%y',
                6: '%m-%d-%y'
    }
    # randomly get a format
    formatting = formats[rd.randint(1, len(formats))]

    return randomdate.strftime(formatting)


def update_date(date):
    # TODO add more formats
    formats = {1: "%Y-%m-%d %H:%M:%S",
               2: '%m/%d/%Y %I:%M %p',
               3: '%b %d, %Y',
               4: '%m-%d-%Y',
               5: '%m/%d/%y',
               6: '%m-%d-%y'
               }

    # set date string to datetime
    for k,v in formats.items():
        try:
            old_date = datetime.strptime(date, v)
            break
        except:
            pass

    randomdate = radar.random_datetime(
        start=old_date,
        stop=datetime(year=2017, month=6, day=16)
    )

    # randomly get a format
    formatting = formats[rd.randint(1, len(formats))]

    return randomdate.strftime(formatting)





def gen_birthdate():
    # generate a random date over a range
    randomdate = radar.random_datetime(
        start=datetime(year=1950, month=1, day=1),
        stop=datetime(year=1999, month=6, day=16)
    )
    # returning random formats
    # TODO add more formats
    formats = { 1: "%Y-%m-%d %H:%M:%S",
                2: '%m/%d/%Y %I:%M %p',
                3: '%b %d, %Y',
                4: '%m-%d-%Y',
                5: '%m/%d/%y',
                6: '%m-%d-%y'
    }
    # randomly get a format
    formatting = formats[rd.randint(1, len(formats))]

    return randomdate.strftime(formatting)


def gen_username(lastname, firstname):
    # function to generate path
    pathchoice = rd.randint(1,5)
    ll = len(lastname)
    fl = len(firstname)
    # generate username based of last and first
    if pathchoice <= 2:
        username = lastname[0:rd.randint(1, ll) - 1] + firstname[0:rd.randint(1, fl) - 1] + \
                   str(rd.randint(1, 9999))
    # generate username based on sports
    elif pathchoice == 3:
        username = usl.adjectives[rd.randint(1,len(usl.adjectives))] + \
                   usl.sports[rd.randint(1,len(usl.sports))] + \
                   usl.suffixes[rd.randint(1, len(usl.suffixes))] + \
                   str(rd.randint(1, 999))
    # generate username based on sports
    elif pathchoice == 4:
        username = usl.adjectives[rd.randint(1, len(usl.adjectives))] + \
                   usl.popculture[rd.randint(1, len(usl.popculture))] + \
                   usl.suffixes[rd.randint(1, len(usl.suffixes))] + \
                   str(rd.randint(1, 999))
    else:
        username = usl.adjectives[rd.randint(1, len(usl.adjectives))] + \
                   firstname[0:rd.randint(1, fl) - 1] + \
                   usl.suffixes[rd.randint(1, len(usl.suffixes))] + \
                   str(rd.randint(100, 9999))
    return username.replace(' ', '')


def gen_email(username):
    return username + '@' + ed.domains[rd.randint(1, len(ed.domains))]


def gen_country():
    number = rd.randint(0, 5)  # generate a random number to decide country
    if number <=3:
        country = rd.choice(['USA', 'United States', 'United States of America', 'U.S.A.', 'U.S.',
                             'US'])
    else:
        country = ed.countries[rd.randint(1, len(ed.countries))]
    return country


def gen_address():
    # '35654 Gallegos Branch\nWest Aaronfurt, LA 33263-1163'
    address = fake.address().split('\n')
    streetaddress = address[0]
    sndpart = [x.strip() for x in address[1].split(',')]
    try:
        city = sndpart[0]
    except:
        city = ''
    try:
        state = sndpart[1].split(' ')[0]
    except:
        state = ''
    try:
        postal = sndpart[1].split(' ')[1]
    except:
        postal = ''
    return streetaddress, city, state, postal


def gen_nid(country):
    nid = ''
    number = rd.randint(0, 1)  # generate a random number
    if country.lower() in {'usa', 'united states', 'united states of america', 'u.s.a.', 'u.s.', 'us'}:
        if number == 1:
            nid = str(rd.randint(100, 999)) + '-' + str(rd.randint(10, 99)) + '-'+str(rd.randint(1000, 9999))
        else:
            nid = str(rd.randint(100, 999)) + str(rd.randint(10, 99)) + str(rd.randint(1000, 9999))
    return nid


def gen_xid():
    ch=['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    xid=''
    for i in range(8):
        xid+=ch[rd.randint(0,len(ch)-1)]
    xid+='-'
    for i in range(4):
        xid+=ch[rd.randint(0,len(ch)-1)]
    xid+='-'
    for i in range(4):
        xid+=ch[rd.randint(0,len(ch)-1)]
    xid+='-'
    for i in range(4):
        xid+=ch[rd.randint(0,len(ch)-1)]
    xid+='-'
    for i in range(12):
        xid+=ch[rd.randint(0,len(ch)-1)]
    return xid


def gen_phone():
    number = rd.randint(0, 5)  # generate a random number
    if number == 0:
        # (123) 123-1234
        phone = '(' + str(rd.randint(100, 999)) + ') ' + str(rd.randint(100, 999)) + '-' + str(rd.randint(1000, 9999))
    elif number == 1:
        # 1231231234
        phone = str(rd.randint(100, 999)) + str(rd.randint(100, 999)) + str(rd.randint(1000, 9999))
    elif number == 2:
        # 123-123-1234
        phone = str(rd.randint(100, 999)) + '-' + str(rd.randint(100, 999)) + '-' + str(rd.randint(1000, 9999))
    elif number == 3:
        # 123.123.1234
        phone = str(rd.randint(100, 999)) + '.' + str(rd.randint(100, 999)) + '.' + str(rd.randint(1000, 9999))
    elif number == 4:
        # (123) 123.1234
        phone = '(' + str(rd.randint(100, 999)) + ') ' + str(rd.randint(100, 999)) + '.' + str(rd.randint(1000, 9999))
    elif number == 5:
        # (123)1231234
        phone = '(' + str(rd.randint(100, 999)) + ')' + str(rd.randint(100, 999)) + str(rd.randint(1000, 9999))

    number2 = rd.randint(0, 5)
    if number2 <= 4:
        return phone
    else:
        return str(1) + phone


def generate_ip4():
    return rstr.xeger(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

