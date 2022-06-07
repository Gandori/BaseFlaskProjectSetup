from flask import Flask
from .app_routes import *
from .app_config import *
from .blueprints.auth.signin import signin
from .blueprints.auth.signup import signup

class app:
    def __init__(self):
        self = Flask(__name__)
        self.config.from_object(dev_config)
        self.before_first_request(before_first_request)
        self.before_request(before_request)
        self.after_request(after_request)
        self.add_url_rule('/', 'index', index)
        self.errorhandler(code_or_exception=404)(errorhandler_404)
        self.register_blueprint(signin, url_prefix='/signin')
        self.register_blueprint(signup, url_prefix='/signup')
        self.run(host='localhost', port=5000)