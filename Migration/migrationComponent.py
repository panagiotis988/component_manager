from mydb import mysql
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship


class components(mysql.Model):
    id = mysql.Column('componentId', mysql.Integer, primary_key=True)
    code = mysql.Column(mysql.String(100))
    type = mysql.Column(mysql.String(100))
    characteristics = mysql.Column(mysql.String(100))
    quantity = mysql.Column(mysql.Integer)

    def __init__(self, code, type, characteristics, quantity):
        self.code = code
        self.type = type
        self.characteristics = characteristics
        self.quantity = quantity
