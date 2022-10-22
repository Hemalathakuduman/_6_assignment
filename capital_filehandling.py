import json
file = open("E:\\DS290822B\\_json_assignment\\_2_capital.json")

# convert json into dict
data = json.load(file)
print(data)