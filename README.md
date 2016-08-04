# stravaNotifier
To watch athletes and segments in Strava and notify (or display)

### Setup
This app uses the stravalib python and redis libraries, so install it: pip install -t . stravalib redis

### Todo

- [ ] How to archive old notifications out of activity history json?
- [ ] deploy on lambda (currently running on cron *nix environment)
- [ ] profit $$$
- [ ] if profit then write tests :)


### Activity Feed Workflow
* Get activity feed
* Get persisted notification history json
* For each activity feed json item:
	* If activity id not in notification history json:
		* Send notification
		* Append activity id in notification json list
			* Store activity history json

### Segment Workflow
* Get segment leaderboard
* Get persisted segment leaderboard
* If leaderboards diff
  * Find a meaningful way to show what changed?
	* Send notification
	* Store updated leaderboard
