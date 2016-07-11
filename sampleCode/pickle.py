import ConfigParser
import json
import pickle


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
