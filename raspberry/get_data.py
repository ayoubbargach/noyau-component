#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect( host="172.17.0.2", user="root", passwd="123456", db="test")

cur = db.cursor()
cur.execute("SELECT * FROM test")

for row in cur.fetchall() :
	print( row )

db.close()
