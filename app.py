from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def buttons():  # put application's code here
    return render_template('buttons.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    total = None
    descuento = 0
    total_final = 0
    nombre = ""
    edad = 0
    total_sin_descuento = 0

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario

        if edad >= 18:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0

        total_final = total_sin_descuento - descuento

    return render_template(
        'ejercicio1.html',
        nombre=nombre,
        edad=edad,
        total_sin_descuento=total_sin_descuento,
        descuento=descuento,
        total_final=total_final
    )

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""
    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']

        if nombre == "juan" and contraseña == "admin":
            mensaje = f"Bienvenido Administrador {nombre}"
        elif nombre == "pepe" and contraseña == "user":
            mensaje = f"Bienvenido Usuario {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run()
