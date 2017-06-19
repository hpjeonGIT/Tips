#!/usr/bin/python3

import sqlite3
import sys
import time
if (len(sys.argv) <2 ):
    print ("input argument error")
    sys.exit()

action = (sys.argv)[1]
action = action.lower()

today = time.strftime("%m-%d-%Y")


con = sqlite3.connect('DB2017.db')
cur = con.cursor()
if (action == 'search'):
    if (len(sys.argv) <2 ):
        print ("search element is not entered")
        sys.exit()
    target = (sys.argv)[2]
    query = """select HeadWord from Solution where SiteName ==?"""
    cur.execute(query, (target,))
    for any in cur:
        print(any[0])
        
elif (action == 'insert'):
    print(sys.argv, len(sys.argv))
    if (len(sys.argv) < 3):
        print ("site name is not entered")
        sys.exit()
    if (len(sys.argv) < 4):
        print ("key is missing")
        sys.exit()
        
    site = (sys.argv)[2]
    key  = (sys.argv)[3]

    if (len(sys.argv) <5):
        etc = 'no comment'
    else:
        etc = (sys.argv)[4]
        
    cur.execute("insert into Solution values(?, ?, ?, ?)",(site,key,today,etc))
    con.commit()
else:
    print('unknown action')

con.close()
