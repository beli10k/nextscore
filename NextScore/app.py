from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nexstore_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from models.models import *

with app.app_context():
    db.create_all()

from routes.auth import *
from routes.dashboard import *
from routes.products import *
from routes.clients import *
from routes.sales import *
from routes.finance import *
from routes.reports import *

if __name__ == '__main__':
    app.run(debug=True)