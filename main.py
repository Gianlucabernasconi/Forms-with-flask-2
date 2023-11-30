from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def mostrar_pagina_principal():
    return render_template('pagina_principal.html')

# Función para calcular el descuento
def calcular_descuento(edad, nombre, cantidad_de_tarros):
    tarro = 9000
    porcentaje_descuento = 0
    descuento_total = 0

    if 18 <= edad <= 30:
        porcentaje_descuento = tarro * 0.15 * cantidad_de_tarros
    elif edad > 30:
        porcentaje_descuento = tarro * 0.25 * cantidad_de_tarros
    
    descuento_total = tarro * cantidad_de_tarros - porcentaje_descuento
    mensaje = (
        f"Nombre del cliente: {nombre}\n"
        f"Total sin descuento: {tarro * cantidad_de_tarros}\n"
        f"El descuento es: {porcentaje_descuento}\n"
        f"El total a pagar es de: {descuento_total}"
    )
    return mensaje

# Ruta para procesar el formulario
@app.route("/calcular_descuento", methods=['POST'])
def procesar_formulario():
    nombre = request.form.get('nombre')
    edad_str = request.form.get('edad')
    cantidad_de_tarros_str = request.form.get('cantidad_de_tarros')
    
    
    if edad_str is not None and cantidad_de_tarros_str is not None:
        edad = int(edad_str)
        cantidad_de_tarros = int(cantidad_de_tarros_str)
        
        mensaje = calcular_descuento(edad, nombre, cantidad_de_tarros)
        print(mensaje)
        return render_template("pagina_calculo_de_compras.html", mensaje=mensaje)
    else:
        mensaje = "Los campos de edad y cantidad de tarros son obligatorios."
        return render_template("pagina_calculo_de_compras.html", mensaje=mensaje)















#Funcion y ruta 2
def login(nombre, password):
    user_1 = "juan"
    user_2 = "pepe"
    password_user_1 = "admin"
    password_user_2 = "user"
     
    mensaje =""
     
    if nombre == user_1 and password == password_user_1:
        mensaje = (
            f"Bienvenido Administrador: Juan"
        )
        return mensaje
    
    elif nombre == user_2 and password == password_user_2:
        mensaje = (
            f"Bienvenido Usuario: Pepe"
        )
        return mensaje
    else: 
        mensaje = ""
        return mensaje

    




@app.route("/login", methods=['GET', 'POST'])
def procesar_login():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        contraseña_str = request.form.get('contraseña')

        if not nombre or not contraseña_str:
            mensaje = ""
        else:
            resultado_login = login(nombre, contraseña_str)
            if not resultado_login:
                mensaje = "Usuario o contraseña incorrectos."
            else:
                mensaje = resultado_login
        return render_template("pagina_de_inicio_de_sesion.html", mensaje=mensaje)

    return render_template("pagina_de_inicio_de_sesion.html")






        
    









if __name__ == '__main__':
      app.run(port=5000, debug=True)
