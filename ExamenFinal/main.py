from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        cant_pintura = int(request.form['cant_pintura'])

        if 18 <= edad <= 30:
            desc = 0.15
        elif edad > 30:
            desc = 0.25
        else:
            desc = 0

        sin_desc = cant_pintura * 9000
        con_desc = sin_desc * desc
        total = sin_desc - con_desc

        return render_template('ejercicio1.html', nombre=nombre, sin_desc=sin_desc, con_desc=con_desc, total=total)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        password = str(request.form['password'])

        if nombre == "juan" and password == "admin":
            mensaje = "Bienvenido administrador juan"
        elif nombre == "pepe" and password == "user":
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2.html', mensaje=mensaje)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)