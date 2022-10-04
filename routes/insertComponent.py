from flask import render_template

from main import *

insert_component = Blueprint('insert_component', __name__)


@insert_component.route('/', methods=['GET', 'POST'])
def insert():
    if request.method == "POST":
        details = request.form
        print('details===', details)
        code = details['code']
        characteristics = details['characteristics']
        quantity = details['quantity']
      
        mysql.sension.commit()

        return 'success'
    return render_template('insert.html')
