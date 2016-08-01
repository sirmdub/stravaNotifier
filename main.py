#!/bin/python
import ConfigParser
import json
import io
from stravalib.client import Client

config = ConfigParser.ConfigParser()
client = Client()

config.read('config.ini')
client.access_token = config.get("access","access_token")
app_friends = config.get("app","friends")

# get my friends activities
activity_feed = client.get_friend_activities()
activity_feed_list = list(activity_feed)
afl_list = []
for i in range(0, len(activity_feed_list)):
  if str(activity_feed_list[i].athlete.id) in app_friends:
    afl_list.append(activity_feed_list[i].id)

#print(afl_list)

#get the history of notifications
f = open('notification.list', 'rb')
notification_list = json.load(f)
f.close()

for activity in afl_list:
  print("processing activity id " + str(activity))
  if activity not in notification_list:
    print("Notification not found, carry on with notification")
    notification_list.append(activity)
    of = open('notification.list', 'wb')
    json.dump(notification_list, of)
    of.close()
