import configparser
import os

# Génération automatique de config.ini
def generate_config():
    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, 'config.ini')

    config = configparser.ConfigParser()
    config['database'] = {
        'user': 'postgres',
        'password': 'Ttt458800',
        'host': 'localhost',
        'port': '5432',
        'name': 'traveleef'
    }
    config['serpapi'] = {
        'API_KEY': '090bef042216971af43307a560f6441c71c2fab3af2b314a3d0141e0bb750870',
        'BASE_URL': 'https://serpapi.com/search/',
    }

    with open(config_path, 'w') as configfile:
        config.write(configfile)
    print(f"Fichier config.ini généré à : {config_path}")

generate_config()
