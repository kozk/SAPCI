from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient

app = Flask(__name__)
cliente = MongoClient("mongodb+srv://itzcui_db_user:8Zu4Fik8n6OmwHCw@cdmx.k0skwr4.mongodb.net/?appName=CDMX")
app.db = cliente.blog

entradas = [entrada for entrada in app.db.contenido.find({})]
usuarios = [usuario for usuario in app.db.usuarios.find({})]
print(entradas)
print(usuarios)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        fecha_formato = datetime.datetime.today().strftime("%d-%m-%Y, %H:%M:%S")
        titulo = request.form.get("tit")
        contenido_entrante = request.form.get("content")
        parametros = {"titulo": titulo, "contenido": contenido_entrante, "fecha": fecha_formato}
        entradas.append(parametros)
        app.db.contenido.insert_one(parametros)

        nombre_usuario = request.form.get("name_u")
        telefono = request.form.get("phone_u")
        parametros_usuario = {"nombre_u": nombre_usuario, "telefono_u": telefono, "fecha": fecha_formato}
        usuarios.append(parametros_usuario)
        app.db.usuarios.insert_one(parametros_usuario)

    return render_template("index.html", entradas = entradas)


if __name__ == "__main__":
    app.run()