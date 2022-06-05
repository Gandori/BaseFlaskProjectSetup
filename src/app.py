from flask import Flask
from .app_routes import *
from .app_config import *
from .blueprints.form.form import form
from .blueprints.home.home import home
from .blueprints.admin.admin import admin

class app:
    def __init__(self):
        self = Flask(__name__)
        self.config.from_object(dev_config)
        self.before_first_request(before_first_request)
        self.before_request(before_request)
        self.after_request(after_request)
        self.errorhandler(code_or_exception=404)(errorhandler_404)
        self.register_blueprint(blueprint=form, url_prefix='/sign')
        self.register_blueprint(blueprint=home, url_prefix='/home')
        self.register_blueprint(blueprint=admin, url_prefix='/admin')

        self.run(host='localhost', port=5000)