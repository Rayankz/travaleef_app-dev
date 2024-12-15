from werkzeug.security import generate_password_hash

from backend.src.app.database import db_singleton
from backend.src.app.utiles.utiles import validate_password, validate_email

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


# Opérations CRUD
def add_user(first_name, last_name, email, password, favorite_transport=None, favorite_destination=None):
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
    db_singleton.execute_query(query, args)

def get_all_user():
    query = "SELECT * FROM travel_comparator.users;"
    return db_singleton.execute_query(query, fetch_all=True)

def get_user_by_id(user_id):
    query = "SELECT * FROM travel_comparator.users WHERE id = %s;"
    return db_singleton.execute_query(query, (user_id,), fetch_one=True)

def get_user_by_email(email):
    query = "SELECT * FROM travel_comparator.users WHERE email = %s;"
    return db_singleton.execute_query(query, (email,), fetch_one=True)

def update_user(user_id, **kwargs):
    fields = []
    args = []
    for key, value in kwargs.items():
        if key in ["first_name", "last_name", "email", "password", "favorite_transport", "favorite_destination", "average_co2_impact", "total_ecological_travel_time"]:
            fields.append(f"{key} = %s")
            args.append(value)
    if not fields:
        raise ValueError("Aucune donnée à mettre à jour.")
    query = f"UPDATE travel_comparator.users SET {', '.join(fields)} WHERE id = %s;"
    args.append(user_id)
    db_singleton.execute_query(query, args)

def delete_user(user_id):
    query = "DELETE FROM travel_comparator.users WHERE id = %s;"
    db_singleton.execute_query(query, (user_id,))
