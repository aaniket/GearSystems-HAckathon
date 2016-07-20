

import csv
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","django","complaint_registration" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.





with open('sky.csv','rb') as f:
	reader=csv.reader(f)
	for row in reader:
		sql = ("INSERT INTO initcomplaint (location,username,description)" "VALUES(%s,%s,%s)" )
		data = ('NONE',row[10],row[1])
		try:			
			cursor.execute(sql,data)
			db.commit()
		except:
			print "Could not do"			
			db.rollback()


