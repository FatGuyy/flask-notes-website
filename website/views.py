'''
This is same to the auth. I.E sets routes
'''
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/home')
def home():
    return render_template('base.html')
