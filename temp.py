import json

with open('orders.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for item in data:
        print(item['id'])

#for item in data:
