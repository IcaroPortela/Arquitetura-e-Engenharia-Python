from classes import Server
from bottle import Bottle, template

""" class Server:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._app = Bottle()
        self._route()

    def _route(self):
        try:
            self._app.route('/', method='GET', callback= self._index)
        except:
            print('Não foi possível entrar no site')
    
    def start(self):
        try:
            self._app.run(host=self._host, port=self._port)
        except:
            print('ERRO: não foipossível iniciar!')
    
    def _index(self):
        try:
            return template('license')
        except:
            print('ERRO: site não encontrado!')

servidor = Server(host='localhost', port=8080)
servidor.start() """

class Sever(Bottle):
    def __init__(self, name):
        super(Server, self).__init__()
        self._name = name
        self.route('/', callback= self.index)

    def index(self):
        return template('license')

servidor = Server('Bottle')
servidor.run(host='localhost', port=8080)