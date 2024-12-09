import src.app.services.utilisateur_service as utilisateur_service

def mapper(utilisateur_tuple):
    utilisateur_list = []
    for i in range(len(utilisateur_tuple)):
        utilisateur = utilisateur_service.Utilisateur(utilisateur_tuple[i][0], utilisateur_tuple[i][1], utilisateur_tuple[i][2])
        utilisateur_list.append(utilisateur.__dict__)

    return utilisateur_list