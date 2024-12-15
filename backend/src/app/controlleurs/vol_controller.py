from flask import Blueprint, request, jsonify
from backend.src.app.services.vol_service import rechercher_vols_service

# Création d'un blueprint pour les routes liées aux vols
vol_bp = Blueprint('vol', __name__)

@vol_bp.route('/recherche_vols', methods=['GET'])
def rechercher_vols_controller():
    """
    Endpoint pour rechercher des vols via l'API Google de SerpAPI.
    """
    try:
        # Récupération des paramètres de la requête
        departure_id = request.args.get('departure_id')
        arrival_id = request.args.get('arrival_id')
        outbound_date = request.args.get('outbound_date')
        return_date = request.args.get('return_date', None)
        adults = request.args.get('adults', 1, type=int)
        children = request.args.get('children', 0, type=int)
        travel_class = request.args.get('travel_class', 1, type=int)

        # Appel du service pour rechercher des vols
        result = rechercher_vols_service(
            departure_id, arrival_id, outbound_date, return_date, adults, children, travel_class
        )

        # Retour des résultats
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500