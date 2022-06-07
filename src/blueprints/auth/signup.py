from flask import Blueprint, render_template

signup = Blueprint('signup',__name__)
signup.template_folder = 'templates'
signup.static_folder = 'static'

PAGE = 'signup.html'

@signup.route('/', methods=['GET', 'POST'])
def index():
    return render_template(PAGE)