import ConfigParser
import json
import io
import pickle
import redis

config = ConfigParser.ConfigParser()

config.read('config.ini')
redis_host = config.get("access", "redis_host")


###pickle serialization examples###
pkl_file = open('data.pkl', 'rb')
config = pickle.load(pkl_file)
#subsequent calls will load multiple objects in sequence
pkl_file.close()

print(config.get("access","access_token"))
print(json.loads(config.get("app","friends")))

config = ConfigParser.ConfigParser()
config.read('config.ini')

print(config.get("access","access_token"))
print(json.loads(config.get("app","friends")))

output = open('data.pkl', 'wb')
pickle.dump(config, output)
#subsequent calls will dump multiple objects in sequence
output.close()



###json serialization examples###
made_json = json.dumps(["1234", "1766377", "7587139", "6853684", "11361212", "1755537"])
of = open('basic.json', 'wb')
json.dump(made_json, of)
of.close()

f = open('basic.json', 'rb')
got_json = json.load(f)
f.close()

print(got_json)

##redis examples##
r = redis.StrictRedis(host=redis_host)

stuff = [12345, 661433997, 660910621, 660773605, 661171413, 660742477, 660319359, 660862539, 659821469, 659814635, 659584841, 658886683, 658652335, 658634949, 659030864, 658387262, 661833033]
print(r.spop("stuff"))

for i in stuff:
  print("processing " + str(i))
  if not r.sismember("stuff", i):
    print("not found in db...")
    r.sadd("stuff", i)

print(r.smembers("stuff"))