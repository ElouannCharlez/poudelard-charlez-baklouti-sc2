def initialiser_personnage(nom, prenom, attributs):
    return {"Nom": nom, "Prenom": prenom, "Argent": 100, "Inventaire": [], "Sortilèges": [], "Attributs": attributs, "Maison": "aucune"}



def afficher_personnage(joueur):
    print("Profil du personnage : ")
    print("Nom : ", joueur["Nom"])
    print("Prenom : ", joueur["Prenom"])
    print("Argent : ", joueur["Argent"])
    print("Inventaire : ")
    for val in joueur["Inventaire"]:
        print("- ", val)
    print("Sortilèges : ")
    for val in joueur["Sortilèges"]:
        print("- ", val)
    print("Attributs : ")
    for val in joueur["Attributs"]:
        print("- ", val, " : ", joueur["Attributs"][val])
    print("Maison : ", joueur["Maison"])
    return None


def modifier_argent(joueur, montant):
    joueur["Argent"] += montant
    return None


def ajouter_objet(joueur, cle, objet):
    joueur[cle].append(objet)
    return None

