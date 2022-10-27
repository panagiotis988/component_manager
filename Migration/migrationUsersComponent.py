from sqlalchemy import *
from sqlalchemy.orm import relation

from mydb import base, mysql
from Migration.migrationUser import *
from Migration.migrationComponent import *


class UserComponent(mysql.Model, base):
    __tablename__ = "usercomponent"
    id = mysql.Column(mysql.Infetteger, primary_key=True)
    component = mysql.Column(mysql.Integer, mysql.ForeignKey("components.id"),onupdate="cascade")
    user = mysql.Column(mysql.Integer, mysql.ForeignKey("users.id"),onupdate="cascade")
