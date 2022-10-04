from main import app
from flask_sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship

mysql = SQLAlchemy(app)
# base = declarative_base()

base = 'mysql://root:toulio@localhost:3306/MyDB'

app.config['SQLALCHEMY_DATABASE_URI'] = base
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from Migration.migratioUser import *
from Migration.migrationComponent import *

mysql.create_all()
