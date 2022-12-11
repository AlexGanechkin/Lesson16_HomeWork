from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship
from offers import offers
from utils import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)

""" ------------ создаем классы -------------------"""


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(50))
    role = db.Column(db.String(20))
    phone = db.Column(db.String(20))

    # user_order = relationship('Order')
    # user_offer = relationship('Offer')


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    start_date = db.Column(db.String(100))
    end_date = db.Column(db.String(100))
    address = db.Column(db.String(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # user = relationship('User')
    # offer = relationship('Offer')


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # executor = relationship('User')


db.create_all()

""" -------------- наполняем таблицы -----------------"""

users = load_users()
orders = load_orders()

with db.session.begin():
    for item in users:
        empty_user = User()
        new_user = class_user(item, empty_user)
        db.session.add(new_user)

    for item in orders:
        empty_order = Order(id=item["id"])
        new_order = class_order(item, empty_order)
        db.session.add(new_order)

    for item in offers:
        empty_offer = Offer(id=item["id"])
        new_offer = class_offer(item, empty_offer)
        db.session.add(new_offer)

    db.session.commit()

""" -------------- запускаем вьюшки по пользователю -----------------"""


@app.route('/users/')
def all_users():
    user_list = User.query.all()
    users_dict = []

    for one_user in user_list:
        users_dict.append(json_user(one_user))
    return users_dict


@app.route('/users/<int:uid>')
def current_user(uid):
    one_user = json_user(User.query.get(uid))
    return one_user


@app.route('/users/', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        json_data = json.loads(request.data)
        empty_user = User()
        add_user = class_user(json_data, empty_user)

        db.session.add(add_user)
        db.session.commit()

    return "user was added"


@app.route('/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def update_user(uid):
    if request.method == 'PUT':
        json_data = json.loads(request.data)
        updated_user = User.query.get(uid)
        updated_user = class_user(json_data, updated_user)
        db.session.add(updated_user)
        db.session.commit()
        return "user was updated"
    elif request.method == 'DELETE':
        deleted_user = User.query.get(uid)
        db.session.delete(deleted_user)
        db.session.commit()
        return "user was deleted"


""" -------------- запускаем вьюшки по заказам -----------------"""


@app.route('/orders/')
def all_orders():
    order_list = Order.query.all()
    order_dict = []

    for one_order in order_list:
        order_dict.append(json_order(one_order))
    return order_dict


@app.route('/orders/<int:uid>')
def current_order(uid):
    one_order = json_order(Order.query.get(uid))
    return one_order


@app.route('/orders/', methods=['GET', 'POST'])
def create_order():
    if request.method == 'POST':
        json_data = json.loads(request.data)
        empty_order = Order()
        add_order = class_order(json_data, empty_order)

        db.session.add(add_order)
        db.session.commit()

    return "order was added"


@app.route('/orders/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def update_order(uid):
    if request.method == 'PUT':
        json_data = json.loads(request.data)
        updated_order = Order.query.get(uid)
        updated_order = class_order(json_data, updated_order)
        db.session.add(updated_order)
        db.session.commit()
        return "order was updated"
    elif request.method == 'DELETE':
        deleted_order = Order.query.get(uid)
        db.session.delete(deleted_order)
        db.session.commit()
        return "order was deleted"


""" -------------- запускаем вьюшки по предложениям -----------------"""


@app.route('/offers/')
def all_offers():
    offer_list = Offer.query.all()
    offers_dict = []

    for one_offer in offer_list:
        offers_dict.append(json_offer(one_offer))
    return offers_dict


@app.route('/offers/<int:uid>')
def current_offer(uid):
    one_offer = json_offer(Offer.query.get(uid))
    return one_offer


@app.route('/offers/', methods=['GET', 'POST'])
def create_offer():
    if request.method == 'POST':
        json_data = json.loads(request.data)
        empty_offer = Offer()
        add_offer = class_offer(json_data, empty_offer)

        db.session.add(add_offer)
        db.session.commit()

    return "offer was added"


@app.route('/offers/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def update_offer(uid):
    if request.method == 'PUT':
        json_data = json.loads(request.data)
        updated_offer = Offer.query.get(uid)
        updated_offer = class_offer(json_data, updated_offer)
        db.session.add(updated_offer)
        db.session.commit()
        return "offer was updated"
    elif request.method == 'DELETE':
        deleted_offer = Offer.query.get(uid)
        db.session.delete(deleted_offer)
        db.session.commit()
        return "offer was deleted"


if __name__ == '__main__':
    app.run()

# query = db.session.query(User.first_name, Order.name).join(User)
# print(f'request: {query}')
# print(f'Result: {query.all()}')
