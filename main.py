from flask import Flask, render_template, request, Blueprint, redirect, url_for

app = Flask(__name__)

from routes.showAppearance import *
from routes.insertComponent import *
from routes.deleteComponent import *
from mydb import *

app.register_blueprint(show_select, url_prefix='/show_select')
app.register_blueprint(insert_component, url_prefix='/insert_component')


# app.register_blueprint(delete_component, url_prefix='/delete_component')


@app.route('/')
def index():
    return render_template("form.html")


if __name__ == '__main__':
    app.run()
