from mydb import mysql, base
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship
from Migration.migrationUsersComponent import *


class Components(mysql.Model, base):
    __tablename__ = "components"
    id = mysql.Column(mysql.Integer, primary_key=True)
    code = mysql.Column(mysql.String(100))
    types = mysql.Column(mysql.String(100))
    characteristics = mysql.Column(mysql.String(100))
    quantity = mysql.Column(mysql.Integer)
    user = relationship("Users", secondary="UserComponent")

    def __init__(self, code, types, characteristics, quantity):
        self.code = code
        self.types = types
        self.characteristics = characteristics
        self.quantity = quantity
