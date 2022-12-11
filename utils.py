import json


def load_users():
    with open('users.json', 'r', encoding='utf-8') as file:
        users = json.load(file)
        return users


def load_orders():
    with open('orders.json', 'r', encoding='utf-8') as file:
        orders = json.load(file)
        return orders


def class_user(json_data, fill_element):
    fill_element.first_name = json_data["first_name"]  # убрал id=json_data["id"], - положился на автоинкремент
    fill_element.last_name = json_data["last_name"]
    fill_element.age = json_data["age"]
    fill_element.email = json_data["email"]
    fill_element.role = json_data["role"]
    fill_element.phone = json_data["phone"]
    return fill_element


def class_order(json_data, fill_element):
    fill_element.name = json_data["name"]  # id=json_data["id"],
    fill_element.description = json_data["description"]
    fill_element.start_date = json_data["start_date"]
    fill_element.end_date = json_data["end_date"]
    fill_element.address = json_data["address"]
    fill_element.price = json_data["price"]
    fill_element.customer_id = json_data["customer_id"]
    fill_element.executor_id = json_data["executor_id"]
    return fill_element


def class_offer(json_data, fill_element):
    fill_element.order_id = json_data["order_id"]
    fill_element.executor_id = json_data["executor_id"]
    return fill_element


def json_user(one_user):
    new_user = {
        'id': one_user.id,
        'first_name': one_user.first_name,
        'last_name': one_user.last_name,
        'age': one_user.age,
        'email': one_user.email,
        'role': one_user.role,
        'phone': one_user.phone,
    }
    return new_user


def json_order(one_order):
    new_order = {'id': one_order.id,
                 'name': one_order.name,
                 'description': one_order.description,
                 'start_date': one_order.start_date,
                 'end_date': one_order.end_date,
                 'address': one_order.address,
                 'price': one_order.price,
                 'customer_id': one_order.customer_id,
                 'executor_id': one_order.executor_id,
                 }
    return new_order


def json_offer(one_offer):
    new_offer = {'id': one_offer.id,
                 'order_id': one_offer.order_id,
                 'executor_id': one_offer.executor_id,
                 }
    return new_offer


if __name__ == '__main__':
    pass
