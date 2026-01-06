from utils.input_utils import demander_choix


def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] += points
        if points > 0:
            print(nom_maison + " a gagné " + str(points) + " point" + 's'*(points>1))
            print("Son score est passé a " + str((maisons[nom_maison])) + " !")
        elif points == 0 :
            print(nom_maison +" n'a pas gagné de points ")
            print("Son score reste a "+str((maisons[nom_maison])))
        else:
            print(nom_maison + " a perdu " + str(-points) + " point" + 's'*(-points>1))
            print("Son score est passé a " + str((maisons[nom_maison])) + " !")
    else:
        print(nom_maison+" est introuvable")



def afficher_maison_gagnante(maisons):
    maxi=None
    for val in maisons:
        if maxi == None:
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
        if maxi == None:
            maxi = attributs[val]
        elif attributs[val] > maxi:
            maxi = attributs[val]
    liste_maisons = []
    for x in attributs:
        if attributs[x] == maxi:
            liste_maisons.append(x)
    if len(liste_maisons) > 1:
        return liste_maisons[demander_choix("Quel maison voulez-vous choisir ?", liste_maisons)]
    return liste_maisons[0]

