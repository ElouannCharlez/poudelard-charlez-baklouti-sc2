from univers.personnage import initialiser_personnage, afficher_personnage


def introduction():
    print("Bienvenue ! Prépare-toi : le premier chapitre de ton voyage vers Poudlard commence maintenant.")
    input()

def creer_personnage():
    nom = input("Entrez le nom de votre personnage : ")
    prenom = input("Entrez le prénom de votre personnage : ")
    print()
    print("Choisissez vos attributs : ")
    courage = 0
    # while not (1 <= courage <= 10):
    #     courage = int(input("Niveau de courage (1-10) : "))
    # intel = 0
    # while not (1 <= intel <= 10):
    #     intel = int(input("Niveau d’intelligence (1-10) : "))
    # loyaute=0
    # while not (1 <= loyaute <= 10):
    #     loyaute = int(input("Niveau de loyauté (1-10) : "))
    # ambition = 0
    # while not (1 <= ambition <= 10):
    #     ambition = int(input("Niveau d'ambition (1-10) : "))
    print()
    attributs = {"courage":courage,"intelligence":intel,"loyauté":loyaute,"ambition":ambition}
    joueur = initialiser_personnage(nom,prenom,attributs)
    afficher_personnage(joueur)
    return joueur

# creer_personnage()
huhu
from utils.input_utils import *
from univers.personnage import *
def recevoir_lettre():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...")
    print("« Cher élève,")
    print("Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »")
    choix = demander_choix("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?",["Oui, bien sûr !", "Non, je préfère rester avec l’oncle Vernon..."])
    if choix == 0:
        return 1 # pour dire que ça continue
    print("\nVous déchirez la lettre, l’oncle Vernon pousse un cri de joie:")
    print("« EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! »")
    print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
    return 0 # pour dire qu'il a refusé

# recevoir_lettre()

def rencontrer_hagrid(personnage):
    print("Hagrid : 'Salut ", personnage["Prenom"]," ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse.'")
    choix = demander_choix("Voulez-vous suivre Hagrid ?", ["Oui", "Non"])
    if choix == 1:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui!\n")
    return None

# perso = {'Nom': 'Baklouti', 'Prenom': 'Youssef', 'Argent': 100, 'Inventaire': [], 'Sortilèges': [], 'Attributs': {'courage : 8'}}
# rencontrer_hagrid(perso)


import json

def acheter_fournitures(personnage):
    with open('../data/inventaire.json', 'r', encoding='utf-8') as f:
        inventaire = json.load(f)
    objets_obli = [["Baguette magique", 35], ["Robe de sorcier", 20], ["Manuel de potions", 25]]
    objets_obli_achete = []
    print("Bienvenue sur le Chemin de Traverse ! \n")
    print("Catalogue des objets disponibles : \n")
    for cle in inventaire:
        print(cle + ". " + inventaire[cle][0] + " - " + str(inventaire[cle][1]) + " galions \n")
    while len(objets_obli_achete) != 3:
        print("Vous avez " + str(personnage["Argent"]) + " galions. \n")
        print("Objets obligatoires restant à acheter : ", end="")
        vu=0
        for i in range(len(objets_obli)):
            if objets_obli[i][0] not in objets_obli_achete:
                print(objets_obli[i][0] + ", "*(i-vu != 2-len(objets_obli_achete)), end="")
            else:
                vu+=1
        numero = demander_nombre("\n\nEntrez le numéro de l'objet à acheter : ", 1, 8)
        if inventaire[str(numero)] in personnage["Inventaire"]:
            print("\nObjet déjà acheté ! \n")
        else:
            if personnage["Argent"] - inventaire[str(numero)][1] < 0:
                print("\nVous n'avez pas assez d'argent...\n")
            else:
                for k in range(len(objets_obli)):
                    if inventaire[str(numero)][0] in objets_obli[k]:
                        objets_obli_achete.append(inventaire[str(numero)][0])
                modifier_argent(personnage, -inventaire[str(numero)][1])
                print("\nVous avez acheté : " + inventaire[str(numero)][0] + " (-" + str(inventaire[str(numero)][1]) + " galions).\n")
        somme=0
        for item in objets_obli:
            if item[0] not in objets_obli_achete:
                somme += item[1]
        if personnage["Argent"] - somme < 0:
            print("Vous avez mal gérez votre argent...\n")
            exit()
    print("Tous les objets obligatoires ont été achetés !\n")
    print("Il est temps de choisir votre animal de compagnie pour Poudlard !")





perso=initialiser_personnage("Baklouti","Youssef",{'courage : 8'})
acheter_fournitures(perso)