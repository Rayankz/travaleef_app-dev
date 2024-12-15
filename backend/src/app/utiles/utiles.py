from backend.src.app.database import PostgresSingleton
import re

from backend.src.app.services.utilisateur_service import regex_email, regex_password


# Utilitaires de validation
def validate_email(email):
    return bool(re.match(regex_email, email))

def validate_password(password):
    return bool(re.match(regex_password, password))



