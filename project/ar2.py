from twython import Twython, TwythonError
from LanguageStatements import CHAT_RESPONSES1,CHAT_RESPONSES2
from random import randint

APP_KEY = "XxpvWiSLKa4FZwDIX8IGTFPne"
APP_SECRET = "Bwf24lSZ5ckkXVmYkt3nzjuZ7deD5YXpfmsqOhQVYvLfkBVSf6"
OAUTH_TOKEN="3323815266-XC6R7Uee7Rzq8OKbsaGABtEmXiHqpWIpbwrUYek"
OAUTH_TOKEN_SECRET="ybSHOfDBE5hW773biampNrKDnguqcEHO7Zj1l4eKzXX7Q"


twitter = Twython(APP_KEY, APP_SECRET)
#auth = twitter.get_authentication_tokens()
#auth=twitter.get_authentication_tokens(callback_url='http:// ? ')

#OAUTH_TOKEN = auth['oauth_token']
#OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
index1=randint(0,1000)
size1=5
index2=randint(0,1000)
size2=4
index1=(index1+1)%size1
index2=(index2+1)%size2
screenName="anichavan20"
chatResponse="can you please specify your location"
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
replyText = '@' + screenName + ' ' +CHAT_RESPONSES1[index1]

try:
	twitter.update_status(status=replyText)
except TwythonError as e:
    print e