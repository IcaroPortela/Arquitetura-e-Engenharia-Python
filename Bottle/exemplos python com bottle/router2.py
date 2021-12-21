from unicodedata import category, name
import os
from bottle import route, debug, template, request, run

@route('/')
def formulario():
    return '''<style> form{text-align: center; background-color: #000; color: #fff; margin-top: 20%;}</style>
        <form action="/" method="post" enctype="multipart/form-data">
            nome: <input name="Nome" type="text" /><br><br>
            e-mail: <input name="E-mail" type="text" /><br><br>
            telefone: <input name="Telefone" type="text" /><br><br>
            usuario: <input name="username" type="text" /><br><br>
            senha: <input name="password" type="password" /><br><br>
            <!--selecione o arquivo: <input type="file" name="upload" />-->
            <input value="Enviar" type="submit" />
        </form>
    '''

@route('/', method='POST')
def gerarform():
    try:
        nome = request.forms.get('nome completo')
        email = request.forms.get('e-mail')
        telefone = request.forms.get('telefone')
        usuario = request.forms.get('usuario')
        senha =  request.forms.get('senha')
        arq = 'cadastro.txt'
        file = open(arq,'wt+')
        file.close()
        file = open(arq, 'at')
        file.write(f'{nome}; {email}; {telefone}; {usuario}; {senha}; \n')

        """ upload = request.files.get('upload')
        ext = os.path.splitext(upload.filename)
        if ext not in( '.png' ,'.jpg' , '.jpeg', '.py','.html', '.txt' ): 
            return  'Extensão de arquivo não permitida.'

        save_path = "/temp/{category}".format(category=category)
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
        upload.save(file_path)
        return "File successfully saved to '{0}'.".format(save_path) """
    except:
        return template('b')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)