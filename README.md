# stravaNotifier
To watch athletes and segments in Strava and notify (or display)

### Setup
This app uses the stravalib python library, so install it: pip install -t . stravalib

### Todo

- [ ] How to archive old notifications out of activity history json?
- [ ] deploy on lambda (currently running on cron *nix environment)
- [ ] profit $$$


### Workflow
* Get activity feed
* Get persisted notification history json
* For each activity feed json item:
	* If activity id not in notification history json:
		* Send notification
		* Append activity id in notification json list
			* Store activity history json
