def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] += points
        if points>0:
            print(nom_maison+" a gagné "+str(points) + " point" + 's'*(points>1))
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