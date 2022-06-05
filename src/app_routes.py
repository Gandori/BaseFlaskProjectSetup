def errorhandler_404(*args):
    return 'Page not Found'

def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Cache-control', 'no-cache, no-store, must-revalidate')
    return response

def before_first_request():
    pass

def before_request():
    pass