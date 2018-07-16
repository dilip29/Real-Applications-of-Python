import json
from difflib import get_close_matches

data=json.load(open("data.json",'r'))

print(data["rain"])
