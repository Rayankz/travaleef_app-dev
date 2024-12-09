from werkzeug.security import generate_password_hash, check_password_hash
from src.app.utiles.database import Database
import re


# Regex pour valider les emails et les mots de passe
regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
regex_password = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

class Utilisateur:
    def __init__(self, id, first_name, last_name, email, password, favorite_transport=None, favorite_destination=None, average_co2_impact=0.0, total_ecological_travel_time=0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.favorite_transport = favorite_transport
        self.favorite_destination = favorite_destination
        self.average_co2_impact = average_co2_impact
        self.total_ecological_travel_time = total_ecological_travel_time

def validate_email(email):
    """Valide le format d'un email."""
    return bool(re.match(regex_email, email))

def validate_password(password):
    """Valide le format d'un mot de passe."""
    return bool(re.match(regex_password, password))

def add_user(first_name, last_name, email, password, favorite_transport=None, favorite_destination=None):
    """Ajoute un utilisateur dans la base de données."""
    if not validate_email(email):
        raise ValueError("Email invalide.")
    if not validate_password(password):
        raise ValueError("Mot de passe invalide.")

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    query = """
        INSERT INTO travel_comparator.users 
        (first_name, last_name, email, password, favorite_transport, favorite_destination)
        VALUES (%s, %s, %s, %s, %s, %s);
    """
    args = (first_name, last_name, email, hashed_password, favorite_transport, favorite_destination)
    Database.execute_query(query, args)

def get_all_user():
    """Récupère tous les utilisateurs de la base de données."""
    query = "SELECT * FROM travel_comparator.users;"
    result = Database.execute_query(query, fetch_all=True)
    return result

def get_user_by_id(user_id):
    """Récupère un utilisateur par son ID."""
    query = "SELECT * FROM travel_comparator.users WHERE id = %s;"
    result = Database.execute_query(query, (user_id,), fetch_one=True)
    return result

def get_user_by_email(email):
    """Récupère un utilisateur par son email."""
    query = "SELECT * FROM travel_comparator.users WHERE email = %s;"
    result = Database.execute_query(query, (email,), fetch_one=True)
    return result

def update_user(user_id, first_name=None, last_name=None, email=None, password=None, favorite_transport=None, favorite_destination=None, average_co2_impact=None, total_ecological_travel_time=None):
    """Met à jour les informations d'un utilisateur."""
    fields = []
    args = []

    if first_name:
        fields.append("first_name = %s")
        args.append(first_name)
    if last_name:
        fields.append("last_name = %s")
        args.append(last_name)
    if email:
        if not validate_email(email):
            raise ValueError("Email invalide.")
        fields.append("email = %s")
        args.append(email)
    if password:
        if not validate_password(password):
            raise ValueError("Mot de passe invalide.")
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        fields.append("password = %s")
        args.append(hashed_password)
    if favorite_transport:
        fields.append("favorite_transport = %s")
        args.append(favorite_transport)
    if favorite_destination:
        fields.append("favorite_destination = %s")
        args.append(favorite_destination)
    if average_co2_impact is not None:
        fields.append("average_co2_impact = %s")
        args.append(average_co2_impact)
    if total_ecological_travel_time is not None:
        fields.append("total_ecological_travel_time = %s")
        args.append(total_ecological_travel_time)

    if not fields:
        raise ValueError("Aucune donnée à mettre à jour.")

    args.append(user_id)
    query = f"UPDATE travel_comparator.users SET {', '.join(fields)} WHERE id = %s;"
    Database.execute_query(query, args)

def delete_user(user_id):
    """Supprime un utilisateur de la base de données."""
    query = "DELETE FROM travel_comparator.users WHERE id = %s;"
    Database.execute_query(query, (user_id,))
