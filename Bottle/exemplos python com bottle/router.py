from bottle import route, debug, template, request, run

@route('/')
def index():
    return template('index')

@route('/b')
def login():
    return template('b')

@route('/b', method='POST')
def aftLogin():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if password == '1234':
        return template('b')
    elif username == 'icaro':
        return template('b')
    else:
        return template('index')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=False, reloader=True)