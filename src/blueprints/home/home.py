from flask import Blueprint, render_template

home = Blueprint('home',__name__,template_folder='../',static_folder='/')

@home.route('/')
def index():
    return render_template('home/home.html', title='home')
