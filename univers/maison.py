from utils.input_utils import demander_choix


def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] += points
        if points>0:
            print(nom_maison+" a gagné "+str(points) + " point" + 's'*(points>1))
            print("Son score est passé a " + str((maisons[nom_maison])) + " !")
        elif points==0 :
            print(nom_maison +" n'a pas gagné de points ")
            print("Son score reste a "+str((maisons[nom_maison])))
        else:
            print(nom_maison + " a perdu " + str(-points) + " point" + 's'*(-points>1))
            print("Son score est passé a " + str((maisons[nom_maison])) + " !")
    else:
        print(nom_maison+" est introuvable")

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
        if maxi==None:
            maxi = maisons[val]
        elif maisons[val]>maxi:
            maxi=maisons[val]
    l=[]
    for x in maisons:
        if maisons[x]==maxi:
            l.append(x)
    if len(l)==1:
        print("La maison gagnante est :")
        print("- ",l[0])
    else:
        print("Les maisons gagnantes sont : ")
        for val in l:
            print("- ",val)


#afficher_maison_gagnante(maisons)
# from chapitres.chapitre_1 import creer_personnage
# joueur = creer_personnage()

def repartition_maison(joueur, questions):
    equipes=["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    i_equipes=0
    attributs = {}
    for val in joueur["Attributs"]:
        attributs[equipes[i_equipes]] = joueur["Attributs"][val]*2
        i_equipes+=1

    for i in range (len(questions)):
        choix = demander_choix(questions[i][0], questions[i][1])
        attributs[questions[i][2][choix]] += 3
    print("\nRésumé des scores :")
    for val in attributs:
        print("- ",val," : ",attributs[val]," points")
    maxi = None
    for val in attributs:
        if maxi == None:
            maxi = attributs[val]
        elif attributs[val] > maxi:
            maxi = attributs[val]
    l = []
    for x in attributs:
        if attributs[x] == maxi:
            l.append(x)
    if len(l)>1:
        choix=demander_choix("Quel maison voulez-vous choisir ?", l)
        l[0]=l[choix]
    return l[0]

# questions = [
#         (
#             "Tu vois un ami en danger. Que fais-tu ?",
#             ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
#         ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
#         ),
#         (
#             "Quel trait te décrit le mieux ?",
#             ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
#              ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
#         ),
#         (
#             "Face à un défi difficile, tu...",
#             ["Fonces sans hésiter", "Cherches la meilleure stratégie",
#              "Comptes sur tes amis", "Analyses le problème"],
#             ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
#         )
#     ]
# repartition_maison(joueur, questions)