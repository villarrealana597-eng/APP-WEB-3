from flask import Flask, render_template, request, redirect, url_for
from db import db
from Barrio import Barrio

class Programa:

    def __init__(self):

        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///barrios.sqlite3"

        # Agregar la db a nuestra aplicación
        db.init_app(self.app)

        self.app.add_url_rule('/', view_func=self.buscarTodos)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=["GET", "POST"])

        # Iniciar el servidor
        with self.app.app_context():
            db.create_all()
            self.app.run(debug=True)

    def buscarTodos(self):

        return render_template('mostrarTodos.html', barrios=Barrio.query.all())

    def agregar(self):

        # Verificar si debe enviar el formulario o procesar los datos
        if request.method == "POST":
            # Crear un objeto de la clase Barrio con los datos del formulario
            nombre = request.form['nombre']
            localidad = request.form['localidad']
            poblacion = request.form['poblacion']

            miBarrio = Barrio(nombre, localidad, poblacion)

            # Guardar el objeto en la db
            db.session.add(miBarrio)
            db.session.commit()

            return redirect(url_for('buscarTodos'))

        return render_template('NuevoBarrio.html')


miPrograma = Programa()