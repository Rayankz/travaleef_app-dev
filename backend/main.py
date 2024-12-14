import os
from flask import Flask
from flask_cors import CORS
from src.app.controlleurs.utilisateur_controller import utilisateur_bp
from flask_jwt_extended import JWTManager
import configparser

# Charger la configuration
config = configparser.ConfigParser()
config_file = 'config.ini'
if not os.path.exists(config_file):
    raise FileNotFoundError(f"Le fichier de configuration '{config_file}' est introuvable.")

config.read(config_file)

# Validation des sections et clés nécessaires
if 'JWT' not in config or 'secret' not in config['JWT']:
    raise KeyError("La section [JWT] ou la clé 'secret' est absente dans le fichier config.ini")

# Initialisation de l'application Flask
app = Flask(__name__)
CORS(app, supports_credentials=True, origins=['http://localhost:4200'])

app.register_blueprint(utilisateur_bp, url_prefix="/user")

# Configuration JWT
app.config['JWT_SECRET_KEY'] = config['JWT']['secret']
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/user/refresh'
app.config['JWT_COOKIE_HTTPONLY'] = False
app.config['CORS_SUPPORTS_CREDENTIALS'] = True

jwt = JWTManager(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000)