from backend.src.app.services.mappers.vol_mapper import fetch_vols_data

def rechercher_vols_service(departure_id, arrival_id, outbound_date, return_date=None, adults=1, children=0, travel_class=1):
    """
    Service pour gérer la logique métier autour de la recherche de vols.
    """
    # Préparer les paramètres pour le mapper
    params = {
        'departure_id': departure_id,
        'arrival_id': arrival_id,
        'outbound_date': outbound_date,
        'return_date': return_date,
        'adults': adults,
        'children': children,
        'travel_class': travel_class
    }

    # Appeler le mapper pour récupérer les données
    return fetch_vols_data(params)