def initialiser_personnage(nom, prenom, attributs):
    return {"Nom": nom, "Prenom": prenom, "Argent": 100, "Inventaire": [], "Sortilèges": [], "Attributs": attributs}

# print(initialiser_personnage("Baklouti","Youssef",{'courage : 8'}))
# renvoie : {'Nom': 'Baklouti', 'Prenom': 'Youssef', 'Argent': 100, 'Inventaire': [], 'Sortilèges': [], 'Attributs': {'courage : 8'}}

def afficher_personnage(joueur) :
    print("Profil du personnage : ")
    print("Nom : ",joueur["Nom"])
    print("Prenom : ",joueur["Prenom"])
    print("Argent : ",joueur["Argent"])
    print("Inventaire : ")
    for val in joueur["Inventaire"]:
        print("- ",val)
    print("Sortilèges : ")
    for val in joueur["Sortilèges"]:
        print("- ",val)
    print("Attributs : ")
    for val in joueur["Attributs"]:
        print("- ", val, " : ", joueur["Attributs"][val])
    return None

# perso=initialiser_personnage("Baklouti","Youssef",{'courage : 8'})
# afficher_personnage(perso)

def modifier_argent(joueur, montant):
    joueur["Argent"] += montant
    return None

# perso=initialiser_personnage("Baklouti","Youssef",{'courage : 8'})
# modifier_argent(perso,-10)
# afficher_personnage(perso)

def ajouter_objet(joueur, cle, objet):
    joueur[cle].append(objet)
    return None

# perso=initialiser_personnage("Baklouti","Youssef",{'courage : 8'})
# ajouter_objet(perso, "Inventaire", "baguette magique")
# afficher_personnage(perso)