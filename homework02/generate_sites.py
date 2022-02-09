import random
import json

meteorites= {}
meteorites['sites']= []
for i in range(5):
    x = random.uniform(16.0, 18.0)
    y = random.uniform(82.0, 84.0)
    z = random.choice(["stony", "iron", "stony-iron"])
    meteorites['sites'].append( {'site_id':i+1, 'latitude':x, 'longitude':y, 'composition':z} )

with open('meteorites.json', 'w') as out:
    json.dump(meteorites, out, indent=2)

