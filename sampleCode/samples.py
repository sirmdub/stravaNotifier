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
redis_host = config.get("access", "redis_host")

# get my profile
#curr_athlete = client.get_athlete()
# inspect the athlete object
#print(type(curr_athlete))
#print(dir(curr_athlete))

# get another athlete profile
#curr_athlete = client.get_athlete(4658463)
#print(curr_athlete)

# get a segment
#curr_segment = client.get_segment(11493495)
#print(type(curr_segment))
#print(dir(curr_segment))
#print(curr_segment)
# get a segment leaderboard
#curr_segmentldr = client.get_segment_leaderboard(11493495)
#print(type(curr_segmentldr))
#print(dir(curr_segmentldr))
#will need to iterate through the curr_segmentldr object (its a collection), based on .entry_count
#print(curr_segmentldr.entry_count)
#segmentldr_json = {"segmentldr": []}
#for i in range(0, 10):
#  segmentldr_json["segmentldr"].append(json.dumps({"athlete_name": curr_segmentldr[i].athlete_name,
#    "athlete_id": curr_segmentldr[i].athlete_id,
#    "activity_id": curr_segmentldr[i].activity_id,
#    "rank": curr_segmentldr[i].rank}))

#print(segmentldr_json)

# get my friends activities
activity_feed = client.get_friend_activities()
#print(type(activity_feed))
#print(dir(activity_feed))
#print(activity_feed)
#once you get the feed, you have to call list() on it to get a dict object
activity_feed_list = list(activity_feed)
print(len(activity_feed_list))
#print(activity_feed_list[0])
#print(activity_feed_list[0].athlete)
afl_json = {"afl": []}
afl_list = []
for i in range(0, len(activity_feed_list)):
  if str(activity_feed_list[i].athlete.id) in app_friends:
    afl_json["afl"].append(json.dumps({"id": activity_feed_list[i].id}))
    afl_list.append(activity_feed_list[i].id)

print(type(afl_json))
print(afl_json)
print(afl_list)

of = open('basic.json', 'wb')
json.dump(afl_json, of)
of.close()
of = open('basic.list', 'wb')
json.dump(afl_list, of)
of.close()

f = open('basic.json', 'rb')
got_json = json.load(f)
f.close()
print(type(got_json))
print(got_json)
f = open('basic.list', 'rb')
got_list = json.load(f)
f.close()
print(type(got_list))
print(got_list)

if 65732142 not in got_list:
  print("Notification not found, notify on")
  got_list.append(65732142)
  print(got_list)
