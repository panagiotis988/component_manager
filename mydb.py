from main import app
from flask_sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toulio@localhost:3306/MyDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine('mysql://root:toulio@localhost:3306/MyDB', echo = True)

base = declarative_base()
mysql = SQLAlchemy(app)

from Migration.migratioUser import *
from Migration.migrationComponent import *
from Migration.migrationUsersComponent import *


base.metadata.create_all(engine)

mysql.create_all()
