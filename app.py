# importar librerias a usar 

from markupsafe import escape

#Importamos librerias Falsk 
from flask import Flask, abort, render_template

#variable de instancia app
app=Flask(__name__, template_folder='templates')

#Ruta raíz
@app.route('/')

#función que retorna la página
def principal():
    return render_template('login.html')

#Ruta página de zapatos html
@app.route('/principal.html')

#función que retorna la página
def contactos():
    return render_template('principal.html')    


if __name__=='__main__':
    app.run(debug=True)
    
