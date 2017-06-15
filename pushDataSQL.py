import cx_Oracle as cx
import pandas as pd


##### Step 1 : Connect to Oracle Database#########
conn_str = u'system/oracle@//52.90.246.44:49161/xe'
conn = cx.connect(conn_str)
cur = conn.cursor()
#######################################
#### Step 2: FETCH LATEST ROW ID FROM TABLE###
query = "SELECT * from integris.TALL1000"
cur.execute(query)
cur.fetchone()

datafile = pd.read_csv('/ path / to / file')
for index, row in datafile.iterrows():
    sqlquery = "INSERT INTO integris.TALL1000 VALUES ('%s','%s','%s','%s','%s')" % (
    row['user_id'], row['gid'], row['enum'], row['value'], row['last_modified'])

    # cur.execute(sqlquery)
    print(x)
    print(sqlquery)
    x = x + 1


conn.commit()

conn.close()