from bottle import route, run, template, request, post

#@route('/')
#def index():
#    return '<center><h1>Olá Mundo!</h1></center>'
""" 
@route('/ola/<name>')
def index(name='desconhecido'):
    return '<center><h1>Olá '+ name +'!</h1></center>'

@route ('/artigo/<id>')
def pagina(id):
    return '<h1>Artigo com id ' + id + '</h1>' """

@route('/login')
def login():
    return template('base')
"""  <form action="/login" method="post">
              usarname: <input name="username" type="text" />
              password: <input name="password" type="password" />
             <input value="Login" type="submit" />
          </form> """

@route('/login')
def login():
    return template('login')

@route('/login', method='POST')
def after_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if password == '1234':
        if username == 'icaro':
            return template('after_login', username=username)
    else:
        return template('login')
""" @route('/cadastro', method='POST')
def cadastro():
    return template('cadastro') """
#@route('/cadastro')
#def after_cad():
#    username = request.forms.get('username')
#    password = request.forms.get('password')
#    return template('after-cad', username=username)

if __name__=='__main__':
    run(host='localhost', port=8080, debug=True, reload=True)
