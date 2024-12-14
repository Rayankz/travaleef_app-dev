-- Création du schéma
CREATE SCHEMA IF NOT EXISTS travel_comparator;



-- Utilisation du schéma travel_comparator
SET search_path TO travel_comparator;



-- Création de la table des utilisateurs
CREATE TABLE travel_comparator.users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    favorite_transport VARCHAR(50),
    favorite_destination VARCHAR(100),
    average_co2_impact FLOAT DEFAULT 0,
    total_ecological_travel_time INTERVAL DEFAULT '0 hours'
);



-- Création de la table pour l'historique des recherches
CREATE TABLE travel_comparator.search_history (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES travel_comparator.users(id) ON DELETE CASCADE,
    departure_city VARCHAR(100) NOT NULL,
    arrival_city VARCHAR(100) NOT NULL,
    departure_date DATE NOT NULL,
    return_date DATE,
    price FLOAT NOT NULL,
    duration INTERVAL,
    co2_emission FLOAT,
    transport_modes TEXT[], -- Liste des moyens de transport utilisés
    created_at TIMESTAMP DEFAULT NOW()
);



-- Création de la table pour les informations d'impact environnemental
CREATE TABLE travel_comparator.environmental_impact (
    id SERIAL PRIMARY KEY,
    transport_mode VARCHAR(50) NOT NULL,
    co2_per_hour FLOAT NOT NULL,
    description TEXT
);



-- Insertion des données d'impact environnemental par défaut
INSERT INTO travel_comparator.environmental_impact (transport_mode, co2_per_hour, description)
VALUES
    ('Avion', 250, 'L’avion est l’un des moyens de transport les plus polluants.'),
    ('Train', 30, 'Le train est l’un des moyens de transport les plus écologiques.'),
    ('Bus', 70, 'Le bus est un moyen de transport relativement économe en énergie.'),
    ('Voiture', 120, 'La voiture individuelle a un impact environnemental important.'),
    ('Covoiturage', 50, 'Le covoiturage réduit l’empreinte carbone par passager.'),
    ('Bateau', 200, 'Le bateau est utilisé pour les longues distances mais reste énergivore.');
