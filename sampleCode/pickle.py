import ConfigParser
import json
import pickle


pkl_file = open('data.pkl', 'rb')
config = pickle.load(pkl_file)
pkl_file.close()

print(config.get("access","access_token"))
print(json.loads(config.get("app","friends")))

config = ConfigParser.ConfigParser()
config.read('config.ini')

print(config.get("access","access_token"))
print(json.loads(config.get("app","friends")))

output = open('data.pkl', 'wb')
pickle.dump(config, output)
output.close()
