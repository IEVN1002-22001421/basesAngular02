from flask import Flask, render_template, request
import forms



app = Flask(__name__)

@app.route('/index')
def index():
   titulo = "pagina de Inicio"
   listado = ['Python', 'Flask', 'pa']
   return render_template('index.html', titulo = titulo, listado = listado) 

@app.route('/calculos', methods = ['GET', 'POST'])
def about():
   if request.method == 'POST':
      numero1 = request.form['numero1']
      numero2 = request.form['numero2']
      suma = int(numero1) + int(numero2)
      return render_template('calculos.html', suma = suma, numero1 = numero1, numero2 = numero2)
   return render_template('calculos.html')

@app.route('/distancia')
def distancia():
   return render_template('distancia.html')

@app.route('/numero/<int:num>')
def funcs(num):
   return f"el numero es, {num}"

@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
   return f"el numero es, {num1 + num2}"

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
   return "ID: {} Nombre: {}".format(id,username)

@app.route('/suma/<float:n1>/<float:n2>')
def suma2(n1, n2):
   return "el numero es, {}".format(n1 + n2)

@app.route('/default/')
@app.route('/default/<string:dft>')
def func2(dft="sss"):
   return f"el valor de dft es: " + dft

@app.route("/Alumnos",methods=['GET','POST']   ) 
def alumnos():
   mat:0
   nom:""
   ape:""
   email:""
   alumno_clas=forms.userform(request.form)
   if request.method == 'POST' and alumno_clas.validate():
      mat=alumno_clas.matricula.data
      nom=alumno_clas.nombre.data
      ape=alumno_clas.apellido.data
      email=alumno_clas.correo.data
   return render_template('Alumnos.html',form=alumno_clas,
                          mat=mat,nom=nom,ape=ape,email=email)
@app.route('/prueba')
def func():
   return '''
      <html lang="en">
      <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>HTML 5 Boilerplate</title>
      <link rel="stylesheet" href="style.css">
      </head>
         <body>
            <script src="index.js"></script>
         </body>
      </html>
      '''
      

if __name__== '__main__':
   app.run(debug = True)