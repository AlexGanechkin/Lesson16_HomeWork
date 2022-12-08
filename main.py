import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from offers import offers

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(50))
    role = db.Column(db.String(20))
    phone = db.Column(db.String(20))

    #user_order = relationship('Order')
    #user_offer = relationship('Offer')


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    start_date = db.Column(db.String(100))
    end_date = db.Column(db.String(100))
    address = db.Column(db.String(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    #user = relationship('User')
    #offer = relationship('Offer')


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    #executor = relationship('User')

db.create_all()

with open('users.json', 'r', encoding='utf-8') as file:
    users = json.load(file)

with open('orders.json', 'r', encoding='utf-8') as file:
    orders = json.load(file)


with db.session.begin():
    for item in users:
        new_user = User(id=item["id"],
                    first_name=item["first_name"],
                    last_name=item["last_name"],
                    age=item["age"],
                    email=item["email"],
                    role=item["role"],
                    phone=item["phone"],
        )
        db.session.add(new_user)

    for item in orders:
        new_order = Order(id=item["id"],
                    name=item["name"],
                    description=item["description"],
                    start_date=item["start_date"],
                    end_date=item["end_date"],
                    address=item["address"],
                    price=item["price"],
                    customer_id=item["customer_id"],
                    executor_id=item["executor_id"],
        )
        db.session.add(new_order)

    for item in offers:
        new_offer = Offer(id=item["id"],
                    order_id=item["order_id"],
                    executor_id=item["executor_id"],
        )
        db.session.add(new_offer)

    db.session.commit()

query = db.session.query(User.first_name, Order.name).join(Order)
print(f'request: {query}')
print(f'Result: {query.all()}')