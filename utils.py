import json

def load_1():
    with open('orders.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            print(item)