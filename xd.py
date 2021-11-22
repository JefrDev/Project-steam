import json
jsonfile = open('steam.json')
pythonfile = json.load(jsonfile)
aantalitems = 0
for item in pythonfile:
    aantalitems = aantalitems + 1
print(f'er zitten {aantalitems} items in dit file')




