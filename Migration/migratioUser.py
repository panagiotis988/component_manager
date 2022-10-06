from mydb import mysql, base
from sqlalchemy import Column, ForeignKey, Integer, Table, String
from sqlalchemy.orm import declarative_base, relationship
# from Migration.migrationUsersComponent import *


class Users(mysql.Model, base):
    Table('users',
          Column('id', Integer, primary_key=True),
          Column('username', String),
          Column('password', String),
          Column('email', String))
    users = relationship('Components', secondary="UserComponent", backref='Users')

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

