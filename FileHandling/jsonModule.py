# serialization using json module
# list

import json
L =  [1,2,3,4]
with open('demo.json', 'w') as f:
    json.dump(L, f)

# using dict
d = {
    'name' : 'Saurabh',
    'age':'23',
    'gender' : 'male'
}

with open('demo.json', 'w') as f:
    json.dump(d, f, indent=4)


# deseriallization

with open('demo.json', 'r') as f:
    d = json.load(f)
    print(d)


# Serialize and deserialize
# it's shows as List

import json
t = (1,2,3,4)
with open('demo.json', 'w') as f:
    json.dump(t, f)