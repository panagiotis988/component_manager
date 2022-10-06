from sqlalchemy import *
from sqlalchemy.orm import relation

from mydb import base, mysql
from Migration.migratioUser import *
from Migration.migrationComponent import *


class UserComponent(mysql.Model, base):
    __table_args__ = {'mysql_engine': 'InnoDB'}

    __tablename__ = "UserComponent"
    id = mysql.Column(mysql.Integer, primary_key=True)
    component = mysql.Column(mysql.Integer, ForeignKey("components.id"), name="component_id")
    user = mysql.Column(mysql.Integer, ForeignKey("users.id"), name="user_id")
    component_id = relation(Components)
    user_id = relation(Users)

#
# class UserComponent(mysql.Model,base):
#     __tablename__ = "usercomponent"
#     id = mysql.Column('tableId', mysql.Integer, primary_key=True)
#     componentId = mysql.Column(mysql.Integer, ForeignKey("components.id"))
#     userId = mysql.Column(mysql.Integer, ForeignKey("users.id"))
#     componentId = relation(Components)
#     userId = relation(Users)

# association_table = Table(
#     "association_table",
#     base.metadata,
#     Column("asdf", ForeignKey("users.userId"), primary_key=True),
#     Column("asdffs", ForeignKey("components.componentId"), primary_key=True),
#
# )
