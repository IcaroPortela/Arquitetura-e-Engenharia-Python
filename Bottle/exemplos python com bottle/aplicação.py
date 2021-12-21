from bottle import Bottle, request, template

class Server:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._app = Bottle()
        self._route()
    
    def _route(self):
        self._app.route('/', method='GET', callback= self._index)
    
    def start(self):
        self._app.run(host=self._host, port=self._port)
    
    def _index(self):
        return template('index')
    
class Login(Server):
    def __init__(self, host, port, username, password):
        super().__init__(host, port)
        self._username = username
        self._password = password
    
    def _route(self):
        self._app.route('/b', method='GET', callback= self._login)

    def _login(self):
        self._username = request.form.get('username')
        self._password = request.form.get('password')
        return template('b', username = self._username)

sv = Server(host='localhost', port=8080)
lg = Login(host = 'localhost',port=8080, username='', password='')
sv.start()