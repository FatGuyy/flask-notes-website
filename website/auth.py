'''
This sets the routes of the website.
'''

from flask import Blueprint, redirect, render_template, request, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Notes
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/')
@auth.route('/home')
def home():
    return render_template('base.html' ,text="Dip Shit")

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.form
    print('this')
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')

        user =  User.query.filter_by(email=email).first()
        print('user - ', user)
        if user:
            if check_password_hash(user.password, password=password1):  # type: ignore
                print('Logged in !')
                login_user(user=user, remember=True)
                return redirect(url_for("home.html"))
            else:
                print('password incorrect!')
        else:
            print('email doesn\'t exists, signup first')
    print(data)
    return render_template('login.html', boo=True)
    # return render_template('login.html', user=current_user)

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        print(email,name, password1, password2)
        
        if len(str(email))<4:
            flash('email is too short', category='error')
            print("flash('email is too short', category='error')")
        elif len(str(name)) < 2:
            flash('name is too short', category='error')
            print("flash('name is too short', category='error')")
        elif password1 != password2:
            flash('passwords don\'t match', category='error')
            print("flash('passwords don\'t match', category='error')")
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password1))  # type: ignore
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('account created successfully', category='success')
            # print("flash('account created successfully', category='success')")
            return redirect(url_for('auth.home'))

    return render_template('sign_up.html')

@auth.route("/table")
def table():
    items = [
        {"id":"001", "Name":"omkar", "Notes":"Suck it!",},
        {"id":"002", "Name":"pabu", "Notes":"jastit jasta kay kartil?",},
        {"id":"003", "Name":"wagya", "Notes":"Leave it!",}
    ]
    return render_template('table.html', items=items)