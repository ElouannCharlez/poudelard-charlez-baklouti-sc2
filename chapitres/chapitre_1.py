from utils.input_utils import *
from univers.personnage import *
import json

def introduction():
    print("Bienvenue ! Prépare-toi : le premier chapitre de ton voyage vers Poudlard commence maintenant.")
    input()

# if __name__ == '__main__':
    # introduction()

def creer_personnage():
    nom = input("Entrez le nom de votre personnage : ")
    prenom = input("Entrez le prénom de votre personnage : ")
    print()
    print("Choisissez vos attributs : ")
    courage = demander_nombre("Niveau de courage (1-10) : ", 1, 10)
    intel = demander_nombre("Niveau d’intelligence (1-10) : ", 1, 10)
    loyaute = demander_nombre("Niveau de loyauté (1-10) : ", 1, 10)
    ambition = demander_nombre("Niveau d'ambition (1-10) : ", 1, 10)
    print()
    attributs = {"courage":courage,"intelligence":intel,"loyauté":loyaute,"ambition":ambition}
    joueur = initialiser_personnage(nom,prenom,attributs)
    afficher_personnage(joueur)
    return joueur

# if __name__ == '__main__':
    # creer_personnage()

def recevoir_lettre():
    print("\nUne chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...")
    print("« Cher élève,")
    print("Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »\n")
    choix = demander_choix("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?",["Oui, bien sûr !", "Non, je préfère rester avec l’oncle Vernon..."])
    if choix == 0:
        return 1 # pour dire que ça continue
    print("\nVous déchirez la lettre, l’oncle Vernon pousse un cri de joie:")
    print("« EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! »")
    print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
    return 0 # pour dire qu'il a refusé

# if __name__ == '__main__':
    #recevoir_lettre()

def rencontrer_hagrid(personnage):
    print("\nHagrid : 'Salut ", personnage["Prenom"]," ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse.'")
    choix = demander_choix("Voulez-vous suivre Hagrid ?", ["Oui", "Non"])
    if choix == 1:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui!\n")
    else:
        print("Super, on y va !")
    return None

# if __name__ == '__main__':
    # perso = {'Nom': 'Baklouti', 'Prenom': 'Youssef', 'Argent': 100, 'Inventaire': [], 'Sortilèges': [], 'Attributs': {'courage : 8'}}
    # rencontrer_hagrid(perso)


def acheter_fournitures(personnage):
    inventaire=load_fichier('../data/inventaire.json')
    objets_obli = [["Baguette magique", 35], ["Robe de sorcier", 20], ["Manuel de potions", 25]]
    objets_obli_achete = []
    print("\nBienvenue sur le Chemin de Traverse ! \n")
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
               ajouter_objet(personnage, "Inventaire", inventaire[str(numero)][0])
               modifier_argent(personnage, -inventaire[str(numero)][1])
               print("\nVous avez acheté : " + inventaire[str(numero)][0] + " (-" + str(inventaire[str(numero)][1]) + " galions).\n")
       somme=0
       for item in objets_obli:
           if item[0] not in objets_obli_achete:
               somme += item[1]
       if personnage["Argent"] - somme < 5: #5 et pes 0 car il faut un animal et le moins chère est le crapaud(5)
           print("Vous avez mal gérez votre argent...\n")
           exit()
    print("Tous les objets obligatoires ont été achetés !\n")
    print("Il est temps de choisir votre animal de compagnie pour Poudlard !\n")
    print("Vous avez " + str(personnage["Argent"]) + " galions. \n")
    print("Voici les animaux disponibles :\n")
    animaux={"1":["Chouette", 20], "2":["Chat", 15], "3":["Rat", 10], "4":["Crapaud", 5]}
    for cle in animaux:
        print(cle + ". " + animaux[cle][0] + " - " + str(animaux[cle][1]) + " galions \n")
    numero = demander_nombre("Entrez le numéro de l'objet à acheter :", 1, 4)
    prix = personnage["Argent"] - animaux[str(numero)][1]
    while prix<0:
        print("Il serait bien de savoir lire les étiquettes... Prend un animal que tu peux te permettre !\n")
        numero = demander_nombre("Entrez le numéro de l'objet à acheter : ", 1, 4)
        prix = personnage["Argent"]-animaux[str(numero)][1]
    ajouter_objet(personnage, "Inventaire", animaux[str(numero)][0])
    modifier_argent(personnage, -animaux[str(numero)][1])
    print("\nTous les objets obligatoires ont été achetés avec succès ! Voici votre inventaire final :\n")
    afficher_personnage(personnage)

# if __name__ == '__main__':
#     perso=initialiser_personnage("Baklouti","Youssef",{})
#     acheter_fournitures(perso)

def lancer_chapitre1():
    introduction()
    perso=creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(perso)
    acheter_fournitures(perso)
    print("\nFin du chapitre 1 ! Votre aventure commence à Poudelard...\n")
    return perso

if __name__== '__main__':
    lancer_chapitre1()
