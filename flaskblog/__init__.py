
from flask import Flask
# for database
from flask_sqlalchemy import SQLAlchemy

# for authentication
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '0973c607a91561bba572d39a8da1f845'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# creating sqlalchemy instances
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # function name of our route
login_manager.login_message_category = 'info'

from flaskblog import routes