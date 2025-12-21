def initialiser_personnage(nom, prenom, attributs):
    return {"Nom": nom, "Prenom": prenom, "Argent": 100, "Inventaire": [], "Sortilèges": [], "Attributs": attributs, "Maison": "aucune"}

# if __name__ == '__main__':
#     print(initialiser_personnage("Baklouti","Youssef",{}))

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

# if __name__ == "__main__":
#     perso = initialiser_personnage("Baklouti", "Youssef", {})
#     afficher_personnage(perso)

def modifier_argent(joueur, montant):
    joueur["Argent"] += montant
    return None

# if __name__ == "__main__":
#     perso = initialiser_personnage("Baklouti", "Youssef", {})
#     modifier_argent(perso,-10)
#     afficher_personnage(perso)

def ajouter_objet(joueur, cle, objet):
    joueur[cle].append(objet)
    return None

# if __name__ == "__main__":
#     perso=initialiser_personnage("Baklouti", "Youssef", {})
#     ajouter_objet(perso, "Inventaire", "baguette magique")
#     afficher_personnage(perso)