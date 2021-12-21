from bottle import request, route, template, run

@route ('/index/cadastro')
def cadastro():
    return template('cadastro')
@route('index/cadastro', method='POST')
def registrar():
    username: request.forms.get('nome_cad')
    password: request.forms.get('senha_cad')
    email: request.forms.get('email_cad')
    return template('index')

if __name__ == '__main__':
    run(host="localhost", port="8080", debug=True, reloader=True)