from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:root@localhost/college'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Address(db.Model):
    id = db.Column('adr_id', db.Integer(), primary_key=True)
    city = db.Column('adr_city',db.String(100))
    state = db.Column('adr_state', db.String(50))
    pincode = db.Column('adr_pincode', db.Integer())
    active = db.Column('adr_active', db.String(10), default='Y')
    cid = db.relationship('College', backref='address', lazy=True, uselist=False)


class College(db.Model):
    id = db.Column('clg_id', db.Integer(), primary_key=True)
    name = db.Column('clg_name', db.String(100))
    code = db.Column('clg_code', db.String(50))
    active = db.Column('clg_active', db.String(10), default='Y')
    aid = db.Column('aid', db.ForeignKey('address.adr_id'), unique=True, nullable=False)


# if __name__ == '__main__':


#  To get address city from college
# c1.aid
# 10
# c1.address
# <Address 10>
# c1.address.city
# 'Pune'
