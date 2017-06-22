#!/usr/bin/python3.6
import pandas as pd
import dataGenFunctions as df
import random as rd
import os
import sys

# hyper parameters
totalnumoftables=2
userspertable = 10
startingdatasubjectid = 1000000000


# generate 1 users data
def gen_user_data():
    # dict to hold data
    user_data = {}
    # assign pi values
    user_data['gender'] = [df.assign_gender()]
    user_data['firstname'] = [df.assign_first_name(user_data['gender'][0])]
    user_data['lastname'] = [df.assign_last_name()]
    user_data['name'] = [user_data['firstname'][0] + ' ' + user_data['lastname'][0]]
    user_data['birthdate'] = [df.gen_birthdate()]
    user_data['username'] = [df.gen_username(user_data['lastname'][0], user_data['firstname'][0])]
    user_data['email'] = [df.gen_email(user_data['username'][0])]
    user_data['country'] = [df.gen_country()]
    street, city, state, postal = df.gen_address()
    user_data['address'] = [street + '|' + city + '|' + state + '|' + postal]
    user_data['street'] = [street]
    user_data['city'] = [city]
    user_data['state'] = [state]
    user_data['postal'] = [postal]
    user_data['nid'] = [df.gen_nid(user_data['country'][0])]
    user_data['xid'] = [df.gen_xid()]
    user_data['phone'] = [df.gen_phone()]
    user_data['ip'] = [df.generate_ip4()]

    # assign extra data
    duplicates = ['address', 'email', 'phone', 'xid', 'ip']
    for d in duplicates:
        flag = True
        while flag:
            number = rd.randint(1,10)
            if d == 'address' and number == 5:  # 20% chance
                street0, city0, state0, postal0 = df.gen_address()
                user_data['address'].append(street0 + '|' + city0 + '|' + state0 + '|' + postal0)
                user_data['street'].append(street0)
                user_data['city'].append(city0)
                user_data['state'].append(state0)
                user_data['postal'].append(postal0)
                flag = True if rd.randint(0,1) == 1 else False

            if d =='email' and number >= 9:
                user_data['email'].append(df.gen_email(df.gen_username(user_data['lastname'][0],
                                                                       user_data['firstname'][0])))
                flag = True if rd.randint(0, 1) == 1 else False

            if d =='phone' and number >= 9:
                user_data['phone'].append(df.gen_phone())
                flag = True if rd.randint(0, 1) == 1 else False

            if d =='xid' and number == 5:
                user_data['xid'].append(df.gen_xid())
                flag = True if rd.randint(0, 1) == 1 else False

            if d =='ip' and number >= 9:
                user_data['ip'].append(df.generate_ip4())
                flag = True if rd.randint(0, 1) == 1 else False

    # dict with probability in percentage of generating that piece of information
    user_probs = {
        'firstname': 100,
        'lastname': 100,
        'country':99,
        'gender': 91,
        'username': 100,
        'email': 99.9,
        'address': 80,
        'nid': 80,
        'xid': 88,
        'phone': 78,
        'ip': 64,
        'birthdate': 60
    }

    # run through user probs to drop data from user_data
    for k,v in user_probs.items():
        if k == 'address':
            if rd.randint(0,100) > v:
                del user_data[k]
                del user_data['street']
                del user_data['city']
                del user_data['state']
                del user_data['postal']
        else:
            if rd.randint(0,100) > v:
                del user_data[k]

    return user_data


def read_input(file):
    for line in file:
        yield line.rstrip()


def main(separator='\t'):
    # send file with one line
    for line in read_input(sys.stdin):
        # =======================================================================
        # create tall and flat table
        # user_id | enum value | value | date
        enum_dict = {
            'gender': 1,
            'name': 2,
            'birthdate': 3,
            'username': 4,
            'email': 5,
            'country': 6,
            'nid': 7,
            'xid': 8,
            'phone': 9,
            'address': 10,
            'ip': 11,
         cd   'postal': 12
        }

        current_dir = os.getcwd()
        table = 0  # holds var for table we are constructing
        group = 1
        gid_flag = True

        tall_cols = ['user_id', 'gid', 'enum', 'value', 'last_modified']

        flat_cols = ['first_name', 'last_name', 'phone', 'cell', 'address1', 'address2',
                     'ip_address', 'email', 'username', 'secondary_email', 'nid', 'x_id',
                     'gender', 'name', 'birth_date', 'fax', 'city', 'state', 'street', 'postal',
                     'unique_id', 'mask_7', 'first_created', 'last_mod', 'gid', 'house_size_approx']

        ts_cols = ['table', 'gender', 'name', 'birthdate', 'username', 'email', 'country', 'nid', 'xid',
                     'phone', 'address', 'ip', 'postal']

        fs_cols = ['table', 'first_name', 'last_name', 'phone', 'cell', 'address1', 'address2',
                     'ip_address', 'email', 'username', 'secondary_email', 'nid', 'x_id',
                     'gender', 'name', 'birth_date', 'fax', 'city', 'state', 'street', 'postal',
                     'unique_id', 'mask_7', 'first_created', 'last_mod', 'gid', 'house_size_approx']

        tall_stats = pd.DataFrame(columns=ts_cols)
        flat_stats = pd.DataFrame(columns=fs_cols)

        while table < totalnumoftables:  # loop condition to construct tables

            tall = pd.DataFrame(columns=tall_cols)  # create empty frame for tall
            flat = pd.DataFrame(columns=flat_cols)  # create empty frame for flat
            tall_row = 0  # counter to write rows to tall table

            for user in range(userspertable):
                try:
                    userdata = gen_user_data()
                    firstdateofuse = str(df.gen_date())
                    # generate addional dates after irstdateofuse
                    numofdates = rd.randint(0,9)
                    added_dates = [df.update_date(firstdateofuse) for i in range(numofdates)]
                    max_date = added_dates[-1] if len(added_dates) >= 1 else firstdateofuse
                    added_dates.append(firstdateofuse)
                except:
                    print('error with user creation function')

                #
                try:
                    # generate group ids
                    while gid_flag == True: # flag is true get new group size and set groupid
                        dist = rd.randint(1,10)
                        group_size = rd.randint(1,4) if dist < 10 else rd.randint(1,8)

                        grs = group_size  # household approx
                        group_id = 'GID' + '000' + str(table) + '-' + str(group)
                        gid_flag = False

                    # set a counter to flip the flag back to true
                    group_size -= 1
                    if group_size == 0:
                        group += 1
                        gid_flag = True

                    # print('user %d has flag %r and gid of %s, group size of %d, grs of %d' % (user, gid_flag, group_id, group_size, grs))

                except:
                    print('error with groupid')

                try:
                    # create a tall table
                    for k,v in enum_dict.items():
                        if k in userdata:
                            if k in ['name', 'username', 'email']:
                                for values in userdata[k]:
                                    row = [str(startingdatasubjectid + user),
                                           group_id,
                                           str(v),
                                           values,
                                           firstdateofuse
                                           ]
                                    # add row to tall
                                    tall.loc[tall_row] = row
                                    # TODO ADD Mapper print HERE
                                    print('%s%s%s' % ('TALL', separator, str(row)[1:-1]))
                                    tall_row += 1
                            else:
                                for values in userdata[k]:
                                    row = [str(startingdatasubjectid + user),
                                           group_id,
                                           str(v),
                                           values,
                                           rd.choice(added_dates)
                                           ]
                                    # add row to tall
                                    tall.loc[tall_row] = row

                                    # TODO ADD Mapper print HERE
                                    print('%s%s%s' % ('TALL', separator, str(row)[1:-1]))

                                    tall_row += 1


                    # print(str(user) + ' done (tall)')

                except:
                    print('error (tall) with user ' + str(user))

                try:
                    # create a flat table
                    fname = userdata['firstname'][0] if 'firstname' in userdata else ''
                    lname = userdata['lastname'][0] if 'lastname' in userdata else ''
                    phone1 = userdata['phone'][0] if 'phone' in userdata else ''
                    phone2 = userdata['phone'][1] if len(userdata.get('phone', ''))>=2 else ''
                    add1 =  userdata['address'][0] if 'address' in userdata else ''
                    add2 = userdata['address'][1] if len(userdata.get('address', ''))>=2 else ''
                    ipadd = userdata['ip'][0] if 'ip' in userdata else ''
                    email1 = userdata['email'][0] if 'email' in userdata else ''
                    uname = userdata['username'][0] if 'username' in userdata else ''
                    email2 = userdata['email'][1] if len(userdata.get('email', ''))>=2 else ''
                    ssn = userdata['nid'][0] if 'nid' in userdata else ''
                    x_id = userdata['xid'][0] if 'xid' in userdata else ''
                    sex = userdata['gender'][0] if 'gender' in userdata else ''
                    fullname = userdata['name'][0] if 'name' in userdata else ''
                    bdate = userdata['birthdate'][0] if 'birthdate' in userdata else ''
                    fax = userdata['phone'][2] if len(userdata.get('phone', ''))>=3 else ''
                    city = userdata['city'][0] if 'city' in userdata else ''
                    state = userdata['state'][0] if 'state' in userdata else ''
                    street = userdata['street'][0] if 'street' in userdata else ''
                    postal = userdata['postal'][0] if 'postal' in userdata else ''
                    uid = str(startingdatasubjectid + user)
                    mask7 = userdata['xid'][1] if len(userdata.get('xid', ''))>=2 else ''

                    f_row = [fname, lname, phone1, phone2, add1, add2, ipadd, email1, uname, email2,
                              ssn, x_id, sex, fullname, bdate, fax, city, state, street, postal, uid,
                              mask7, firstdateofuse, max_date, group_id, grs]

                    f_row = [str(i) for i in f_row] # make sure everything is str

                    flat.loc[user] = f_row

                    # TODO ADD Mapper print HERE for flat file
                    print('%s%s%s' % ('FLAT', separator, str(f_row)[1:-1]))

                    # print(str(user) + ' done (flat)')

                except:
                    print('error (flat) with user ' + str(user))


            # # for tall stats
            # ts = tall['enum'].value_counts().to_dict() # create a dict with enum counts
            # tall_stats.loc[table] = [table, ts.get(str(enum_dict['gender']), 0), ts.get(str(enum_dict['name']), 0),
            #                      ts.get(str(enum_dict['birthdate']), 0), ts.get(str(enum_dict['username']), 0),
            #                      ts.get(str(enum_dict['email']), 0), ts.get(str(enum_dict['country']), 0),
            #                      ts.get(str(enum_dict['nid']), 0), ts.get(str(enum_dict['xid']), 0),
            #                      ts.get(str(enum_dict['phone']), 0), ts.get(str(enum_dict['address']), 0),
            #                      ts.get(str(enum_dict['ip']), 0), ts.get(str(enum_dict['postal']), 0)]
            #
            # # TODO ADD Mapper print HERE
            # print([table, ts.get(str(enum_dict['gender']), 0), ts.get(str(enum_dict['name']), 0),
            #                      ts.get(str(enum_dict['birthdate']), 0), ts.get(str(enum_dict['username']), 0),
            #                      ts.get(str(enum_dict['email']), 0), ts.get(str(enum_dict['country']), 0),
            #                      ts.get(str(enum_dict['nid']), 0), ts.get(str(enum_dict['xid']), 0),
            #                      ts.get(str(enum_dict['phone']), 0), ts.get(str(enum_dict['address']), 0),
            #                      ts.get(str(enum_dict['ip']), 0), ts.get(str(enum_dict['postal']), 0)])
            #
            # # for flat table
            # fs = []
            # for col in flat_cols:
            #     description = flat[col].describe().to_dict()
            #     description['null'] = flat[flat[col] == ''][col].count()
            #     fs.append(description)
            #
            # # fs = [flat[col].describe().to_dict().update({'null': flat[flat[col] == ''][col].count()}) for col in flat_cols]
            # fs.insert(0, table)
            #
            #
            # flat_stats.loc[table] = fs
            #
            # # TODO ADD Mapper print HERE
            # print(fs)
            #
            # # add noise and update stats
            # # ToDo add noise
            # # noise_functions = [df.gen_date(), df.gen_phone(), df.]



        #     # create stats table for each table written to disk
        #     tallfile = current_dir + '/tall/tall_' + str(table) + '.csv'
        #     tall.to_csv(tallfile,  index = False)
        #     flatfile = current_dir + '/flat/flat_' + str(table) + '.csv'
        #     flat.to_csv(flatfile, index=False)
            table += 1
        #     startingdatasubjectid += userspertable
        #
        # # write stats
        # tallstatsfile = current_dir + '/stats/tallstats.csv'
        # tall_stats.to_csv(tallstatsfile,  index = False)
        # flatstatsfile = current_dir + '/stats/flatstats.csv'
        # flat_stats.to_csv(flatstatsfile,  index = False)


if __name__ == "__main__":
    main()