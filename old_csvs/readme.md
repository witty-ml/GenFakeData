# Read Me

## contents
- Country_Table.csv : a table that has country name, aplha 2 code, and internal cc
- Users.csv : a table that holds 100,000 rows of fake data (gen by 3rd party and has some data logic errors, mainly use it to strip format)
- websites.csv : a table that holds countries and their country websites
- genTestData.py : a script to generate fake data

### genTestData.py

- needs python libs: pandas, names, random, and datetime
- needs the three tables above to run
- saves fake data as 'Users1.csv'
- currently gens 10000000 rows of fake data
- change variable 'amountOfRowsWeWant' from 10000000 to any number you want
