import ConfigParser
import json
import io
import pickle


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