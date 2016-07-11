#!/bin/python
import ConfigParser
import json
from stravalib.client import Client

config = ConfigParser.ConfigParser()
client = Client()

config.read('config.ini')
client.access_token = config.get("access","access_token")
print(json.loads(config.get("app","friends")))

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
#print(curr_segmentldr[0])

# get my friends activities
activity_feed = client.get_friend_activities()
print(type(activity_feed))
print(dir(activity_feed))
print(activity_feed)
#once you get the feed, you have to call list() on it to get a dict object
activity_feed_list = list(activity_feed)
print(len(activity_feed_list))
print(activity_feed_list[0])
print(activity_feed_list[0].athlete)