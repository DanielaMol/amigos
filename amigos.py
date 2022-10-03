from flask import render_template, request, redirect
from amigos_app import app

# importar la clase de Amigos de la carpeta models del archivo amigo.py
from amigos_app.models.amigo import Amigos


#OPERACION READ(LEER)
@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    friends = Amigos.get_all()
    print(friends)
    return render_template("index.html", todos_amigos=friends)

@app.route("/<int:id>")
def get_un_usuario(id):
    data = {
        "identificador":id
    }
    amigo = Amigos.get_un_amigo(data)
    print(amigo)
    return amigo

@app.route('/create_friend', methods=["POST"])
def create_friend():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    Amigos.save(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/')