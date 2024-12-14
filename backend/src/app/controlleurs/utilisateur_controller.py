from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token
import backend.src.app.services.utilisateur_service as us

utilisateur_bp = Blueprint('utilisateurs', __name__)

@utilisateur_bp.get('/all_user')
def find_all_utilisateur():
    try:
        utilisateurs = us.get_all_user()
        return jsonify(utilisateurs), 200
    except Exception as e:
        return jsonify({"message": f"Erreur : {str(e)}"}), 500

@utilisateur_bp.get('/<int:user_id>')
def get_user_by_id(user_id):
    try:
        utilisateur = us.get_user_by_id(user_id)
        if utilisateur:
            return jsonify(utilisateur), 200
        return jsonify({"message": "Utilisateur non trouvé"}), 404
    except Exception as e:
        return jsonify({"message": f"Erreur : {str(e)}"}), 500

@utilisateur_bp.post('/create_user')
def create_utilisateur():
    data = request.get_json()
    required_fields = ['first_name', 'last_name', 'email', 'password']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"message": f"Champs manquants : {', '.join(missing_fields)}"}), 400
    try:
        us.add_user(**data)
        return jsonify({"message": "Utilisateur créé avec succès"}), 201
    except Exception as e:
        return jsonify({"message": f"Erreur : {str(e)}"}), 500

@utilisateur_bp.put('/modif/<int:user_id>')
def update_user(user_id):
    data = request.get_json()
    try:
        us.update_user(user_id, **data)
        return jsonify({"message": "Utilisateur mis à jour avec succès"}), 200
    except Exception as e:
        return jsonify({"message": f"Erreur : {str(e)}"}), 500

@utilisateur_bp.delete('/delete_user/<int:user_id>')
def delete_user(user_id):
    try:
        us.delete_user(user_id)
        return jsonify({"message": "Utilisateur supprimé avec succès"}), 200
    except Exception as e:
        return jsonify({"message": f"Erreur : {str(e)}"}), 500

@utilisateur_bp.post('/login')
def login():
    data = request.get_json()
    try:
        utilisateur = us.get_user_by_email(data['email'])
        if utilisateur and us.check_password_hash(utilisateur['password'], data['password']):
            access_token = create_access_token(identity=utilisateur['id'])
            refresh_token = create_refresh_token(identity=utilisateur['id'])
            return jsonify({
                "access_token": access_token,
                "refresh_token": refresh_token
            }), 200
        return jsonify({"message": "Identifiants incorrects"}), 401
    except Exception as e:
        return jsonify({"message": f"Erreur : {str(e)}"}), 500
