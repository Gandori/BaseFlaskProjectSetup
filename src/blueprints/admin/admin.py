from flask import Blueprint, render_template

admin = Blueprint('admin',__name__,template_folder='/',static_folder='/')

@admin.route('/')
def index():
    print(admin.static_folder)
    return render_template('admin/admin.html', title='admin')
