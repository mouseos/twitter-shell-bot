import tweepy
import os
import re
import sys

#自身でAPIKeyを入れてね

API_KEY=""
API_SECRET=""
ACCESS_TOKEN=""
ACCESS_TOKEN_SECRET =""

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#ここにTwitterアカウントのIDを入れてください(例:twitterid = '@mouse_soft_y')

twitterid = '@mouse_soft_y'

class MyStream(tweepy.Stream):
 def on_status(self, status):
  message = status.text
  print(message)
  name = (message)
  twitterid = (me.id_str)
  cmd = name.replace( '\n' , '' )
  if 'シェル' in cmd:

  
   command = "python3 commandstart.py " +  "\"" + (cmd) + "\""
   print(command , sep="\n")
  # print("元")
  # print(name)
   result = os.popen(command).read().strip()
   print((result))
   api.update_status('@%s %s' % (status.user.screen_name, result) , in_reply_to_status_id = status.id)
  else:
   print("この条件は無視されます")

me = api.get_user(screen_name=twitterid)
flist = []
flist.append(me.id_str)

myStreamObj = MyStream(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
myStreamObj.filter(follow=flist)
