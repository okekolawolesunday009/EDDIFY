import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
import models

from models.user import User

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bbd123498b9401f18479f4e5e705963d'
bcrypt =  Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = "info"
app.config['MAIL_SERVER'] = 'smtp-relay.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)
moment = Moment(app)

from web_dynamic.users.view import users

app.register_blueprint(users)

if models.storage_t == 'db':
    @login_manager.user_loader
    def load_user(user_id):
	    return models.storage.get(User, user_id)