from utils.input_utils import demander_choix,demander_nombre
from chapitres.chapitre_1 import lancer_chapitre1
from chapitres.chapitre_2 import lancer_chapitre_2
from chapitres.chapitre_3 import lancer_chapitre_3
from chapitres.chapitre_4 import lancer_chapitre4_quidditch

def afficher_menu_principal():
    print("1. Lancer le Chapitre 1 – L’arrivée dans le monde magique.")
    print("2. Quitter le jeu.")

def choix_menu():
    tab_chiffre = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    redemande = True  # on l'utilise pour savoir si ce qu'à entrer le joueur est conforme et sans renvoyer d'erreur s'il est entré des lettres
    while redemande :
        redemande = False
        afficher_menu_principal()
        val = input("Votre choix : ")
        for carac in val:
            if carac not in tab_chiffre:
                redemande = True
    return int(val)

def lancer_choix_menu():
    maisons = {"Gryffondor": 0, "Serpentard": 0, "Poufsouffle": 0, "Serdaigle": 0}
    choix = choix_menu()
    if choix == 1:
        perso = lancer_chapitre1()
        lancer_chapitre_2(perso)
        lancer_chapitre_3(perso, maisons)
        lancer_chapitre4_quidditch(perso, maisons)
    elif choix == 2:
        print("Poudlard te dit au revoir, mais sûrement pas adieu ! Bonne route, pleine de magie et de belles aventures.")
        exit()
    else:
        print("Le choix n'est pas valide.")

if __name__ == "__main__":
    lancer_choix_menu()