from twython import Twython, TwythonError
from LanguageStatements import CHAT_RESPONSES1,CHAT_RESPONSES2
from random import randint
import MySQLdb
import sys

APP_KEY = "XxpvWiSLKa4FZwDIX8IGTFPne"
APP_SECRET = "Bwf24lSZ5ckkXVmYkt3nzjuZ7deD5YXpfmsqOhQVYvLfkBVSf6"
OAUTH_TOKEN="3323815266-XC6R7Uee7Rzq8OKbsaGABtEmXiHqpWIpbwrUYek"
OAUTH_TOKEN_SECRET="ybSHOfDBE5hW773biampNrKDnguqcEHO7Zj1l4eKzXX7Q"


twitter = Twython(APP_KEY, APP_SECRET)

db = MySQLdb.connect('localhost','root','9921129688','complaint_registration')
cursor1 = db.cursor ()
cursor2 = db.cursor ()
cursor3 = db.cursor ()
cursor4 = db.cursor ()


cursor1.execute ("select username from complaint where location = 'NONE' and loc_tweet=0")
data = cursor1.fetchall ()
for row in data:

	#auth = twitter.get_authentication_tokens()
	#auth=twitter.get_authentication_tokens(callback_url='http:// ? ')

	#OAUTH_TOKEN = auth['oauth_token']
	#OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
	#if tag=0:
	#print row[0]
	replyText=row[0]
	check1=row[0]
	#cursor3.execute("update complaint set loc_tweet=1 WHERE username=check1")
	sql1 = "update complaint set loc_tweet='%s' where username='%s'"
	cursor4.execute(sql1%("1",check1))
	db.commit()
	#cursor3.execute("insert into complaint(loc_tweet) values (1)")
	#print replyText
	#replyText='@' + replyText + ' ' 
	#print replyText
	index1=randint(0,1000)
	size1=5
	index1=(index1+1)%size1
	chatResponse=CHAT_RESPONSES1[index1]
	#else:
	#index2=randint(0,1000)
	#size2=4
	#index2=(index2+1)%size2
	#chatResponse=CHAT_RESPONSES1[index2]

	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	replyText = '@' + replyText + ' ' +chatResponse
	#print replyText
	#replyText=""
	#print replyText
	try:
		twitter.update_status(status=replyText)
	except TwythonError as e:
		print e

cursor2.execute ("select username from complaint where contact_no is NULL and con_tweet=0")
data = cursor2.fetchall ()
for row in data :

	#OAUTH_TOKEN = auth['oauth_token']
	#OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
	#if tag=0:
	#print row[0]
	replyText=row[0]
	check=row[0]
	#cursor4.execute("update complaint set con_tweet=1 WHERE username=check")
	sql2 = "update complaint set con_tweet='%s' where username='%s'"
	cursor3.execute(sql2%("1",check))
	db.commit()
	#cursor4.execute("insert into complaint(loc_tweet) values (1) from complaint where username=row[0]")
	#print replyText
	#replyText='@' + replyText + ' ' 
	#print replyText
	index2=randint(0,1000)
	size2=4
	index2=(index2+1)%size2
	chatResponse=CHAT_RESPONSES2[index2]
	#else:
	#index2=randint(0,1000)
	#size2=4
	#index2=(index2+1)%size2
	#chatResponse=CHAT_RESPONSES1[index2]


	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	replyText = '@' + replyText + ' ' +chatResponse
	#print replyText
	#replyText=""
	#print replyText
	try:
		twitter.update_status(status=replyText)
	except TwythonError as e:
		print e