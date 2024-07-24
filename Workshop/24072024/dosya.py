import json
file = json.load(open("Workshop/24072024/dosya1.json"))
# print(type(file))
counter = 0
for item in file:
    if item["isActive"]:
        counter += 1
print(counter)