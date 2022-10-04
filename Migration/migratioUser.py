from mydb import mysql


class users(mysql.Model):
    id = mysql.Column('userId', mysql.Integer, primary_key=True)
    username = mysql.Column(mysql.String(100))
    password = mysql.Column(mysql.String(50))
    email = mysql.Column(mysql.String(200))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
