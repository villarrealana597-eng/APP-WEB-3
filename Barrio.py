from db import db

class Barrio(db.Model):

    # Nombre de la tabla
    __tablename__ = "barrio"

    # Campos de la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70))
    localidad = db.Column(db.String(70))
    poblacion = db.Column(db.String(100))

    # Constructor
    def __init__(self, nombre, localidad, poblacion):
        self.nombre = nombre
        self.localidad = localidad
        self.poblacion = poblacion
        