from flask import Blueprint, render_template

form = Blueprint('form',__name__,template_folder='/',static_folder='/')

@form.route('/in')
@form.route('/in')
def signin():
    return render_template('form/signin.html', title='signin')

@form.route('/up')
def signup():
    return render_template('form/signup.html', title='signup')