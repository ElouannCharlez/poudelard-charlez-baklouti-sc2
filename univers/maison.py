from utils.input_utils import demander_choix


def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] += points
        if points > 0:
            print(nom_maison + " a gagné " + str(points) + " point" + 's'*(points>1)) # affiche un s à la fin seulement s'il y a plusieurs points
            print("Son score est passé a " + str((maisons[nom_maison])) + " !")
        elif points == 0 :
            print(nom_maison +" n'a pas gagné de points ")
            print("Son score reste a "+str((maisons[nom_maison])))
        else:
            print(nom_maison + " a perdu " + str(-points) + " point" + 's'*(-points>1)) # affiche un s à la fin seulement s'il y a plusieurs points
            print("Son score est passé a " + str((maisons[nom_maison])) + " !")
    else:
        print(nom_maison+" est introuvable")

# if __name__ == '__main__':
    # maisons = {
    #  "Gryffondor": 22,
    #  "Serpentard": 22,
    #  "Poufsouffle": 1,
    #  "Serdaigle": 22
    # }
    # actualiser_points_maison(maisons, "Gryffondo", -12)
    # actualiser_points_maison(maisons, "Gryffondor", -12)

def afficher_maison_gagnante(maisons):
    maxi=None
    for val in maisons:
        if maxi == None: # si le maximum est vide on lui attribue comme maximum la première valeur que l'on rencontre
            maxi = maisons[val]
        elif maisons[val] > maxi:
            maxi = maisons[val]
    liste_gagnantes=[]
    for x in maisons:
        if maisons[x]==maxi:
            liste_gagnantes.append(x)
    if len(liste_gagnantes)==1:
        print("La maison gagnante est :")
        print("- ",liste_gagnantes[0])
    else:
        print("Les maisons gagnantes sont : ")
        for val in liste_gagnantes:
            print("- ",val)

# if __name__ == '__main__':
    # maisons = {
    #  "Gryffondor": 22,
    #  "Serpentard": 22,
    #  "Poufsouffle": 1,
    #  "Serdaigle": 22
    # }
    # afficher_maison_gagnante(maisons)

def repartition_maison(joueur, questions):
    equipes = ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    i_equipes = 0
    attributs = {}
    for val in joueur["Attributs"]:
        attributs[equipes[i_equipes]] = joueur["Attributs"][val]*2
        i_equipes += 1

    for i in range (len(questions)):
        choix = demander_choix(questions[i][0], questions[i][1])
        attributs[questions[i][2][choix]] += 3
    print("\nRésumé des scores :")
    for val in attributs:
        print("- ", val, " : ", attributs[val], " points")
    maxi = None
    for val in attributs:
        if maxi == None: # si le maximum est vide on lui attribue comme maximum la première valeur qu'on rencontre
            maxi = attributs[val]
        elif attributs[val] > maxi:
            maxi = attributs[val]
    liste_maisons = []
    for x in attributs:
        if attributs[x] == maxi:
            liste_maisons.append(x)
    if len(liste_maisons) > 1:
        return liste_maisons[demander_choix("Quel maison voulez-vous choisir ?", liste_maisons)] # renvoie la maison choisie
    return liste_maisons[0]

# if __name__ == "__main__":
#     questions = [
#             (
#                 "Tu vois un ami en danger. Que fais-tu ?",
#                 ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
#             ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
#             ),
#             (
#                 "Quel trait te décrit le mieux ?",
#                 ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
#                  ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
#             ),
#             (
#                 "Face à un défi difficile, tu...",
#                 ["Fonces sans hésiter", "Cherches la meilleure stratégie",
#                  "Comptes sur tes amis", "Analyses le problème"],
#                 ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
#             )
#         ]
#     perso = {'Nom': 'Baklouti', 'Prenom': 'Youssef', 'Argent': 100, 'Inventaire': [], 'Sortilèges': [], 'Attributs': {'courage': 7, 'intelligence': 9, 'loyauté': 8, 'ambition': 3}}
#     print(repartition_maison(perso, questions))