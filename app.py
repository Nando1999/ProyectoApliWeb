# importar librerias a usar 

from markupsafe import escape

#Importamos librerias Falsk 
from flask import Flask, abort, render_template

#variable de instancia app
app=Flask(__name__, template_folder='templates')

#Ruta raíz
@app.route('/')

#Ruta página de inicio html
@app.route('/principal')

#función que retorna la página
def inicio():
    return render_template('principal.html')


if __name__=='__main__':
    app.run(debug=True)
    
