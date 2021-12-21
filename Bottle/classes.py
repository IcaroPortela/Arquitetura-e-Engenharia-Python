from bottle import Bottle, template

class Server:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._app = Bottle()
        self._route()

    def _route(self):
        self._app.route('/', method="GET", callback=self._index)
    
    def start(self):
        self._app.run(host=self._host, port=self._port)
    
    def _index(self):
        return template('cadastro')

server = Server(host="localhost", port=8080)
server.start()