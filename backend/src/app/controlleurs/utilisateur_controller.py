from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, unset_jwt_cookies
import src.app.services.utilisateur_service as us
import src.app.services.mappers.utilisateur_mapper as um
import base64

utilisateur_bp = Blueprint('utilisateurs', __name__)
not_found_error = {"message": "Utilisateur non trouvé"}, 404


@utilisateur_bp.post('/secure/test_secure')
@jwt_required()
def test_secure():
    return jsonify({"message": "Route sécurisée"}), 200


@utilisateur_bp.get('/all_user')
def find_all_utilisateur():
    try:
        utilisateurs = us.get_all_user()
        return jsonify(utilisateurs), 200
    except Exception as e:
        return jsonify({"message": f"Erreur lors de la récupération des utilisateurs : {str(e)}"}), 500


@utilisateur_bp.get('/<int:user_id>')
def get_user_by_id(user_id):
    try:
        utilisateur = us.get_user_by_id(user_id)
        if utilisateur:
            return jsonify(utilisateur), 200
        return not_found_error
    except Exception as e:
        return jsonify({"message": f"Erreur lors de la récupération de l'utilisateur : {str(e)}"}), 500


@utilisateur_bp.post('/create_user')
def create_utilisateur():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Les données sont requises"}), 400

    required_fields = ['first_name', 'last_name', 'email', 'password']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"message": f"Champs manquants : {', '.join(missing_fields)}"}), 400

    email = data['email']
    password = data['password']
    first_name = data['first_name']
    last_name = data['last_name']
    favorite_transport = data.get('favorite_transport', None)
    favorite_destination = data.get('favorite_destination', None)

    if not us.validate_email(email):
        return jsonify({"message": "Adresse email invalide"}), 400

    if not us.validate_password(password):
        return jsonify({"message": "Le mot de passe doit contenir au moins 8 caractères, une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial"}), 400

    try:
        us.add_user(first_name, last_name, email, password, favorite_transport, favorite_destination)
        return jsonify({"message": "Utilisateur créé avec succès"}), 201
    except Exception as e:
        return jsonify({"message": f"Erreur lors de la création de l'utilisateur : {str(e)}"}), 500


@utilisateur_bp.put('/modif/<int:user_id>')
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"message": "Les données sont requises"}), 400

    try:
        us.update_user(
            user_id=user_id,
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            password=data.get('password'),
            favorite_transport=data.get('favorite_transport'),
            favorite_destination=data.get('favorite_destination'),
            average_co2_impact=data.get('average_co2_impact'),
            total_ecological_travel_time=data.get('total_ecological_travel_time')
        )
        return jsonify({"message": "Utilisateur mis à jour avec succès"}), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": f"Erreur lors de la mise à jour de l'utilisateur : {str(e)}"}), 500


@utilisateur_bp.delete('/delete_user/<int:user_id>')
def delete_user(user_id):
    try:
        us.delete_user(user_id)
        return jsonify({"message": "Utilisateur supprimé avec succès"}), 200
    except Exception as e:
        return jsonify({"message": f"Erreur lors de la suppression de l'utilisateur : {str(e)}"}), 500


@utilisateur_bp.post('/connexion')
def login():
    auth_header = request.headers.get('Authorization')
    if auth_header is None:
        return jsonify({"message": "Le header Authorization est requis"}), 400

    try:
        auth = base64.b64decode(auth_header.split(" ")[1]).decode("utf-8").split(":")
        email, password = auth
    except Exception:
        return jsonify({"message": "Format du header Authorization incorrect"}), 401

    if not us.validate_email(email) or not password:
        return jsonify({"message": "Identifiants invalides"}), 400

    utilisateur = us.get_user_by_email(email)
    if not utilisateur:
        return jsonify({"message": "Identifiants incorrects"}), 400

    if not check_password_hash(utilisateur['password'], password):
        return jsonify({"message": "Mot de passe incorrect"}), 400

    access_token = create_access_token(identity=str(utilisateur['id']))
    refresh_token = create_refresh_token(identity=str(utilisateur['id']))

    resp = jsonify({"message": "Connexion réussie"})
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
    return resp, 200


@utilisateur_bp.post('/refresh')
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    resp = jsonify({"message": "Token rafraîchi"})
    set_access_cookies(resp, access_token)
    return resp, 200


@utilisateur_bp.post('/deconnexion')
def logout():
    resp = jsonify({"message": "Déconnexion réussie"})
    unset_jwt_cookies(resp)
    return resp, 200


@utilisateur_bp.post('/changer_mot_de_passe')
def changer_mot_de_passe():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Les données sont requises"}), 400

    email = data.get('email')
    ancien_password = data.get('ancien_password')
    nouveau_password = data.get('nouveau_password')

    if not email or not ancien_password or not nouveau_password:
        return jsonify({"message": "Tous les champs sont requis"}), 400

    if not us.validate_password(nouveau_password):
        return jsonify({"message": "Mot de passe invalide"}), 400

    utilisateur = us.get_user_by_email(email)
    if not utilisateur:
        return not_found_error

    if not check_password_hash(utilisateur['password'], ancien_password):
        return jsonify({"message": "L'ancien mot de passe est incorrect"}), 400

    try:
        us.update_user(user_id=utilisateur['id'], password=nouveau_password)
        return jsonify({"message": "Mot de passe modifié avec succès"}), 200
    except Exception as e:
        return jsonify({"message": f"Erreur lors de la mise à jour du mot de passe : {str(e)}"}), 500
