from flask import render_template
from Migration.migrationUser import *
from main import Blueprint, mysql
from mydb import *

insert_user = Blueprint('insert_user', __name__)


@insert_user.route('/', methods=['GET', 'POST'])
def insert():
    if request.method == "POST":
        details = request.form
        print('details===', details)
        username = details['username']
        password = details['password']
        email = details['email']
        insertUser = (mysql.insert(Users).values(id=None,
                                                 username=username,
                                                 password=password,
                                                 email=email))
        print("inputs ==", insertUser, username, email, password)
        return 'success'
    return render_template('sign_up.html')
