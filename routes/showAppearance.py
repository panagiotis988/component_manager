from main import app, render_template, Blueprint
from mydb import mysql

show_select = Blueprint('show_select', __name__, )


@show_select.route('/')
def show_fname():
    query = "SELECT * FROM component;"
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()

    print('data===', data)
    return render_template('show.html', data=data)


@show_select.route('/lname')
def show_lname():
    return "lname"
