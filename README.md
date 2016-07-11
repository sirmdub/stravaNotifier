# stravaNotifier
To watch athletes and segments in Strava and notify (or display)

### Setup
This app uses the stravalib python library, so install it: pip install -t . stravalib

### Todo

- [ ] make my own simple summary objects that are pickleable
- [ ] summary obj for segment?
- [ ] summary obj for segment leaderboard
- [ ] summary obj for activity feed
- [ ] profit $$$

### Notes about design decisions (you don't have to like it...)
I like pickle for serializing objects as a simple persistence model.
I think I can contain the whole thing, persisted data and all in Docker, and run it from anywhere.
