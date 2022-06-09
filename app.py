# importar librerias a usar 

from urllib import request
from markupsafe import escape

#Importamos librerias Falsk 
from flask import Flask, abort, render_template

#variable de instancia app
app=Flask(__name__, template_folder='templates')

#Ruta raíz
@app.route('/')

#función que retorna la página
def principal():
    return render_template('principal.html')

#-----------------------------------------

#Ruta página de inicio html
@app.route('/donaciones.html')

#función que retorna la página
def donaciones():
    return render_template('donaciones.html')  
#----------------------------
#Ruta página de inicio html
@app.route('/donaciones.html')
 
    
@app.route('/login.html')

#función que retorna la página
def login():
    return render_template('login.html')     

@app.route('/contactos.html')

#función que retorna la página
def donaciones1():
    return render_template('contactos.html')       
          
#----------------------------------------------

#Ruta página de inicio html
@app.route('/pagotarjeta.html')

#función que retorna la página
def pagotarjeta():
    return render_template('pagotarjeta.html') 




if __name__=='__main__':
    app.run(debug=True)
    
