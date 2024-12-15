import os
from flask import Flask
from src.app.utiles.database import ConfigApi
from src.app.controlleurs.vol_controller import vol_bp
from src.app.controlleurs.utilisateur_controller import utilisateur_bp
import configparser

def create_app():
    # Initialisation de l'application Flask
    app = Flask(__name__)

    app.config.from_object(ConfigApi)

    app.register_blueprint(utilisateur_bp, url_prefix="/user")
    app.register_blueprint(vol_bp, url_prefix="/api")

    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)