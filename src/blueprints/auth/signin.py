from flask import Blueprint, render_template

signin = Blueprint('signin',__name__)
signin.template_folder = 'templates'
signin.static_folder = 'static'

PAGE = 'signin.html'

@signin.route('/', methods=['GET', 'POST'])
def index():
    return render_template(PAGE)