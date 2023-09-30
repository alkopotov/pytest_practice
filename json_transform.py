import json


with open('data/SuperHero.json', 'r') as f:
    heroes = json.loads(f.read())

heroes_list = sorted(heroes['members'], key=lambda x: x['age'], reverse=True)

data = {
    'heroes': heroes_list
}

with open('data/results.json', 'w') as f:
    s = json.dumps(data, indent=4)
    f.write(s)
# print(*heroes_list, sep='\n')