from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return render_template('base.html' ,text="Dip Shit")

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html', boo=True)

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
        # print(email,name, password1, password2)
        
        if len(str(email))<4:
            flash('email is too short', category='error')
        elif len(str(name)) < 2:
            flash('name is too short', category='error')
        elif password1 != password2:
            flash('passwords don\'t match', category='error')
        else:
            flash('account created successfully', category='success')
    return render_template('sign_up.html')