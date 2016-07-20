import csv
import MySQLdb
import os

# Open database connection
db = MySQLdb.connect('localhost', 'root', '9921129688', 'complaint_registration')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
cursor1 = db.cursor()

ch = 0;
#
#print("chut")

bol=0

with open('GSTweets.csv', 'rU') as f:
    reader = csv.reader(f)
     

    for row in reader:
    	bear=row[2]
    	if bol==1:
    		cursor1.execute ("select complaint_type from type_lookup where complaint_name=%s",[bear])
    		dat1 = cursor1.fetchall()
    		dr=0;
    		for qwe in dat1:
    			dr=qwe[0]
    			#print dr

    		sql = ("INSERT INTO complaint (complaint_type,compaint_desc,username) VALUES ('%s','%s','%s')")
    		#data = (dat1,row[3],row[7])
    		#print row
    		cursor.execute(sql%(dr,row[3],row[7]))
    		db.commit()
    	else:
    		bol=1
    		continue




#os.remove('GSTweets.csv')


#### RUNNING##############