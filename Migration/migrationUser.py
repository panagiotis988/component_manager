from mydb import mysql, base
from sqlalchemy import Column, ForeignKey, Integer, Table, String, Sequence
from sqlalchemy.orm import declarative_base, relationship
from Migration.migrationUsersComponent import *


class Users(mysql.Model, base):
    id = mysql.Column(mysql.Integer, Sequence("user_id_seq"), primary_key=True)
    username = mysql.Column(mysql.String(100))
    password = mysql.Column(mysql.String(50))
    email = mysql.Column(mysql.String(200))
    component = relationship("Components", secondary="UserComponent")

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
