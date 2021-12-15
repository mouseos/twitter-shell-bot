import tweepy
import os
import re

#自身でAPIKeyを入れてね

API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#ここにTwitterアカウントのIDを入れてください(例:twitterid = 'Chromium_Linux')

twitterid = ''

class MyStream(tweepy.Stream):
 def on_status(self, status):
  message = status.text
  print(message)
  name = (message)
  twitterid = (me.id_str)
  if 'シェル' in name:
   timestamp = 'sh commandstart.sh ' +  '"' + (name) + '"'
   print(timestamp)
   current_time = os.popen(timestamp).readline().strip()
   print(current_time)
   api.update_status('@%s %s' % (status.user.screen_name, current_time) , in_reply_to_status_id = status.id)
  else:
   print("この条件は無視されます")

me = api.get_user(screen_name=twitterid)
flist = []
flist.append(me.id_str)

myStreamObj = MyStream(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
myStreamObj.filter(follow=flist)
