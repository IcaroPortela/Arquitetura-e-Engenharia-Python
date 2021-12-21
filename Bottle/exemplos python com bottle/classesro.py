from bottle import Bottle, template, request, route

class Index(Bottle):
    def __init__(self, name):
        super(Index, self).__init__()
        self.name
        self.route('/', method='GET', callback=self.index, name='bottle')

    def index(self):
        return template('index')
    
server = Index('bottle')
server.run(host='localhost', port=8080)