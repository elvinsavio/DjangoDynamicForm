import json

f = open('./drug3.json')

data=json.load(f)

line = sorted(data['fields'], key=lambda k: k.get('order', 0))
print(json.dumps(line, indent = 1))


# sort json before template
