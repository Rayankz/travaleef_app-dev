from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='flaskr.sqlite',
    )

    # Charger la configuration de l'instance si disponible
    app.config.from_pyfile('config.py', silent=True)

    # Exemple de route
    @app.route('/hello')
    def hello():
        return "Hello, Flaskr!"

    # Importer les routes depuis flaskr/routes.py
    from . import routes
    app.register_blueprint(routes.bp)

    return app
