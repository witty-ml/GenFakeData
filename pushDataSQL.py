import cx_Oracle as cx
import pandas as pd


##### Step 1 : Connect to Oracle Database#########
conn_str = u'system/oracle@//52.90.246.44:49161/xe'
conn = cx.connect(conn_str)
cur = conn.cursor()
#######################################
#### Step 2: Check connection###
# query = "SELECT * from integris.TALL1000"
# cur.execute(query)
# cur.fetchone()

datafile = pd.read_csv('tall/tall_0.csv')
d_cols = list(datafile.columns)
for index, row in datafile.iterrows():
    sqlquery = "INSERT INTO integris.TALLCONNECTIONTEST VALUES ('%s','%s','%s','%s','%s')" % (tuple([row[i] for i in d_cols]))


    #row['user_id'], row['gid'], row['enum'], row['value'], row['last_modified'])
    # add batching
    print(index)
    cur.execute(sqlquery)
    if index % 10 == 0:
        conn.commit()
        print('conn.commit()')

    if index == 50:
        break
    #print(sqlquery)

# conn.commit()

conn.close()