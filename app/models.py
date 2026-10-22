from werkzeug.security import generate_password_hash, check_password_hash
from .extensions import db

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(20), nullable=False, default="vendedor")

    def set_password(self, plano):
        self.password = generate_password_hash(plano)

    def check_password(self, plano):
        return check_password_hash(self.password, plano)

    def __repr__(self):
        return f"<Usuario {self.username}>"

class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True)
    telefono = db.Column(db.String(20))

    def __repr__(self):
        return f"<Cliente {self.nombre}>"

class Producto(db.Model):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Producto {self.descripcion}>"
