import json
with open("data.json","r")as file:
    data=json.load(file)
for i in data["students"]:
    print(f"{i["name"]}",f"{i["age"]}")