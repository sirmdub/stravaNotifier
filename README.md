# stravaNotifier
To watch athletes and segments in Strava and notify (or display)

### Setup
This app uses the stravalib python library, so install it: pip install -t . stravalib

### Todo

- [ ] persist data as JSON on disk (can I diff JSON objects?)
- [ ] research/pick mature persistence (dataset, tinydb, redis, postgres, mysql)
- [ ] mature persistence to another data store
- [ ] profit $$$

### Notes about design decisions (you don't have to like it...)
I want to serialize objects into json as a simple persistence model.
Pickle works, but I need to create my own summary object types with only simple pieces of data, and its not portable.
Looks like JSON can do the job, and keep me open to future portability (code and datastore).
Notifications:
	once an actiity is identified and loaded, a process to create notifications comes through, notifies, then marks the activity as notified
	notifications can be email? sns? sms? hipchat running group?

