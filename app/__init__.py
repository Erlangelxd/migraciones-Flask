from flask import Flask
from config import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    @app.shell_context_processor
    def contexto_shell():
        return {
            "db": db,
            "Usuario": models.Usuario,
            "Cliente": models.Cliente,
            "Producto": models.Producto,
            **{
                nombre: getattr(models, nombre)
                for nombre in ("Venta", "DetalleVenta")
                if hasattr(models, nombre)
            },
        }
    return app
