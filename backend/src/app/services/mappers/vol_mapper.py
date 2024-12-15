import requests
from flask import current_app

def fetch_vols_data(params):
    """
    Mapper pour interagir avec l'API SerpAPI et récupérer les vols.
    """
    # Ajoutez la clé API à vos paramètres
    params['engine'] = 'google_flights'
    params['api_key'] = current_app.config['SERPAPI_API_KEY']

    # Effectuer la requête à SerpAPI
    response = requests.get(current_app.config['SERPAPI_BASE_URL'], params=params)

    # Vérifiez si la requête a échoué
    if response.status_code != 200:
        raise Exception(f"Erreur API SerpAPI: {response.json().get('error')}")

    # Retourner les résultats
    return response.json()