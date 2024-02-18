from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from web_dynamic.users.forms import RegistrationForm, LoginForm
from web_dynamic import bcrypt
# from models.user import User
import models

users = Blueprint('users', __name__)

@users.route("/register", methods=['POST', 'GET'], strict_slashes=False)
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        from models.user import User
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hash_password, first_name=form.first_name.data, last_name=form.last_name.data, country=form.country.data)
        models.storage.new(user)  
        models.storage.save()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.home'))
    form = LoginForm()
    if form.validate_on_submit():
        from models.user import User
        user = models.storage.all(User)
        for use in user.values():
            if use.email == form.email.data:
                user_profile = use
                break
        if user_profile and bcrypt.check_password_hash(user_profile.password, form.password.data):
                login_user(user_profile, remember=form.remember.data)
                next_page = request.args.get('next') 
                flash('You have been logged in!', 'success')
                return redirect(url_for('users.home'))
        else:
            flash('Login Unsuccessful, Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)



@users.route("/", methods=['GET', 'POST'])
@users.route("/home", methods=['GET', 'POST'])  
def home():
    return render_template('home.html')   


@users.route("/logout", strict_slashes=False)
def logout():
    logout_user()
    return redirect(url_for('users.register'))
