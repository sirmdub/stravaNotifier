#!/bin/python
import ConfigParser
import json
from stravalib.client import Client
import requests
import sys
import redis
import logging

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

config = ConfigParser.ConfigParser()
client = Client()

config.read('config.ini')
client.access_token = config.get("access","access_token")
app_friends = config.get("app","friends")
hipchat_token = config.get("access","hipchat_token")
redis_host = config.get("access", "redis_host")
r = redis.StrictRedis(host=redis_host)

def hipchat_notify(token, room, message, color='yellow', notify=False,
                   format='text', host='api.hipchat.com'):
    """Send notification to a HipChat room via API version 2

    Parameters
    ----------
    token : str
        HipChat API version 2 compatible token (room or user token)
    room: str
        Name or API ID of the room to notify
    message: str
        Message to send to room
    color: str, optional
        Background color for message, defaults to yellow
        Valid values: yellow, green, red, purple, gray, random
    notify: bool, optional
        Whether message should trigger a user notification, defaults to False
    format: str, optional
        Format of message, defaults to text
        Valid values: text, html
    host: str, optional
        Host to connect to, defaults to api.hipchat.com
    """

    if len(message) > 10000:
        raise ValueError('Message too long')
    if format not in ['text', 'html']:
        raise ValueError("Invalid message format '{0}'".format(format))
    if color not in ['yellow', 'green', 'red', 'purple', 'gray', 'random']:
        raise ValueError("Invalid color {0}".format(color))
    if not isinstance(notify, bool):
        raise TypeError("Notify must be boolean")

    url = "https://{0}/v2/room/{1}/share/link".format(host, room)
    headers = {'Content-type': 'application/json'}
    headers['Authorization'] = "Bearer " + token
    payload = {
        'message': '',
        'link': message,
        'notify': notify,
        'message_format': format,
        'color': color
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    r.raise_for_status()

def main(event, context):
	######
	# MAIN (designed to be imported and ran from another py, so lambda can play, or I can play)
	######

	# get my friends activities
	activity_feed = client.get_friend_activities()
	activity_feed_list = list(activity_feed)
	afl_list = []
	for i in range(0, len(activity_feed_list)):
	  if ( str(activity_feed_list[i].athlete.id) in app_friends and
	      not activity_feed_list[i].private ):
	        afl_list.append(activity_feed_list[i].id)

	#print(afl_list)

	for activity in afl_list:
	  print("processing activity id " + str(activity))
	  if not r.sismember("notifications", activity):
	    print("Notification not found, carry on with notification")
	    hipchat_notify(hipchat_token, 'Running Group', 'https://www.strava.com/activities/' + str(activity))
	    r.sadd("notifications", activity)
