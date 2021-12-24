import tweepy
import os
import re

#自身でAPIKeyを入れてね

API_KEY="3gI0OOUVZQ3cSK09IGOuaV1H8"
API_SECRET="ijYdgwjvR4Lu9tEBwVoMtV9nx0tZUfWa4Mqgnj01wAj5mdplOJ"
ACCESS_TOKEN="979980770633592832-MnSj8VLn7gwQ6sNMLwTmIL47GUfNNkl"
ACCESS_TOKEN_SECRET ="HbLjY6xN0W0HVbO3mfRHCckZSVkwAhkzBar7GAboHgqGX"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#ここにTwitterアカウントのIDを入れてください(例:twitterid = 'Chromium_Linux')

twitterid = '@mouse_soft_y'

class MyStream(tweepy.Stream):
 def on_status(self, status):
  message = status.text
  print(message)
  name = (message)
  twitterid = (me.id_str)
  if 'シェル' in name:
   result = 'python3 commandstart.py ' +  "\"" + (name) + "\""
   print(result , sep="\n")
  # print("元")
  # print(name)
   current_time = os.popen(result).read().strip()
   print(current_time)
   api.update_status('@%s %s' % (status.user.screen_name, current_time) , in_reply_to_status_id = status.id)
  else:
   print("この条件は無視されます")

me = api.get_user(screen_name=twitterid)
flist = []
flist.append(me.id_str)

myStreamObj = MyStream(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
myStreamObj.filter(follow=flist)
