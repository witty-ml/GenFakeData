#generate test data
#python 3
import pandas as pd
import random as rd
import names
from datetime import datetime, timedelta
import random


#function to generate male or female
def assign_Geneder(row_num):
    if row_num%2==0:
        return 'male'
    else:
         return 'female'

#function to abbreviate gender
def abb_Geneder(gender):
    if gender=='female':
        return 'f'
    else:
        return 'm'

def assign_suffix(gender):
    suffix =''
    cutoff = rd.randint(0, 100)
    if cutoff >= 80:
        choice = rd.randint(0, 8)
        if choice==0:
            suffix = ''
        elif choice==1:
            suffix = ''
        elif choice==2:
            suffix = 'III'
        elif choice==3:
            suffix = 'CPA.'
        elif choice==4:
            suffix = 'M.D.'
        elif choice==5:
            suffix = 'Ph.D.'
        elif choice==6:
            suffix = 'J.D.'
        elif choice == 7:
            suffix = 'MBA'
        elif choice == 8:
            suffix = 'MSc'
    return suffix



#function to generate user name
def genUserName(last, first):
    ll=len(last)
    fl=len(first)
    username=last[0:rd.randint(1,ll)-1]+first[0:rd.randint(1,fl)-1]+str(rd.randint(1,9999))
    return username

#function to generate email
def genEmail(user):
    providers=['@icloud.com', '@gmail.com', '@hotmail.com', '@live.com', '@yahoo.com', '@outlook.com',
    '@someschool.edu', '@verizon.net', '@comcast.com']
    email=user+providers[rd.randint(0,len(providers)-1)]
    return email

def genCountry():
    c=['Argentina','Armenia','Australia','Austria','Belgium','Brazil','British Virgin Islands',
 'Bulgaria','Canada','Chile','China','Colombia','Costa Rica','Croatia','Cyprus','Czechia','Denmark',
 'Dominica','Dominican Republic','Ecuador','Egypt','Estonia','Finland','France','Georgia','Germany',
 'Greece','Greenland','Grenada','Guatemala','Hong Kong','Hungary','Iceland','India','Indonesia',
 'Ireland','Isle of Man','Israel','Italy','Jamaica','Japan','Laos','Latvia','Liechtenstein',
 'Lithuania','Luxembourg','Malaysia','Maldives','Malta','Mayotte','Mexico','Moldova','Netherlands',
 'New Zealand','Norway','Palestine','Panama','Philippines','Poland','Portugal','Puerto Rico',
 'Romania','Russia','Saudi Arabia','Serbia','Singapore','Slovakia','Slovenia','South Africa',
 'South Korea','Spain','Sri Lanka','Sweden','Switzerland','Syria','Taiwan','Tanzania','Thailand',
 'Trinidad & Tobago','Turkey','U.S. Virgin Islands','UK','US','Uganda','Ukraine',
 'United Arab Emirates','Uruguay','Uzbekistan','Vatican City','Venezuela','Vietnam','UK','US'
,'US','US','US','US','US','US','US','US','US','US','US']
    return c[rd.randint(0,len(c)-1)]

def genSSN():
    return str(rd.randint(100,999))+'-'+str(rd.randint(10,99))+'-'+str(rd.randint(1000,9999))

def genXid():
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

def genDate():
    year=random.randint(1950, 1999)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = datetime(year, month, day)
    return date

def transSite(country):
    if country=='US' or country=='Argentina' or country=='Mexico' or country=='Colombia':
        return 'www.site.com'
    elif country=='Canada':
        return 'www.site.com.ca'
    elif country=='Australia':
        return 'www.site.com.at'
    elif country=='Belgium':
        return 'www.site.com.be'
    elif country=='France':
        return 'www.site.com.fr'
    elif country=='Germany':
        return 'www.site.com.de'
    elif country=='Ireland':
        return 'www.site.com.ie'
    elif country=='UK':
        return 'www.site.com.uk'
    else:
        return 'www.site.com'

def sysLoc(country):
    num=rd.randint(1,10)
    if num<9.5:
        return country
    else:
        return genCountry()


#parameters
amountOfRowsWeWant=4631
#amountOfRowsWeWant=100
lastColId=1



#load 100000 set from mockaroo for some help creating structure and functions for generating more data
roo=pd.read_csv('Users.csv')

#load in a country table
countries=pd.read_csv('Country_Table.csv', encoding = "ISO-8859-1")

#load webiste table
sites=pd.read_csv('websites.csv')

cols=list(roo.columns.values) #column headers
cols.append('internalCC')

cust_cols=['id', 'first', 'last', 'gender', 'email', 'country', 'username', 'race', 'dob', 'registered_site', 'suffix' ]

data=pd.DataFrame(columns=cust_cols) #create empty frame named data


#to add a row at a time
for i in range(amountOfRowsWeWant):
    try:
        x=names.get_first_name(gender=assign_Geneder(i))
        y=names.get_last_name()
        z=genUserName(y, x)
        c=genCountry()
        d=genDate()
        dd=d + timedelta( days=rd.randint(0,400))
        ddd=dd + timedelta( days=rd.randint(0,30))
        data.loc[i]=[ lastColId+i ,
                        x,
                        y,
                        #assign_Geneder(i),
                        abb_Geneder(assign_Geneder(i)),
                        genEmail(z),
                        c,
                        #countries.loc[countries['name']==c].iloc[0]['ISO3166-1-Alpha-2'],
                        z,
                        #genSSN(),
                        roo['USER_race'][rd.randint(0,len(roo)-1)],
                        #genXid(),
                        str(d)[:-9],
                        #str(dd)[:-9],
                        #str(ddd)[:-9],
                        transSite(c),
                        #sysLoc(c),
                        assign_suffix(assign_Geneder(i))]
                        #countries.loc[countries['name']==c].iloc[0]['internalCC']]
        print ('Added row '+ str(i))
    except:
        print ('error with row ' + str(i))

#save dataframe to csv
data.to_csv('test4631.csv',  index = False)
