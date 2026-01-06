from utils.input_utils import *
from univers.maison import *
from univers.personnage import *
import random

def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):
    print("\nTu commences tes cours de magie à Poudlard...")
    dico_sorts = load_fichier(chemin_fichier)
    offensif, defensif, utilitaire = [], [], []
    for sort in dico_sorts:
        if sort['type']=="Offensif":
            offensif.append(sort)
        elif sort['type']=="Défensif":
            defensif.append(sort)
        else:
            utilitaire.append(sort)
    ajoute_sort_alea(joueur, offensif)
    ajoute_sort_alea(joueur, defensif)
    for i in range(3):
        del utilitaire[ajoute_sort_alea(joueur, utilitaire)]
    print("\nTu as terminé ton apprentissage de base à Poudelard !\nVoici les sortilèges que tu maîtrises désormais :\n")
    for sort in joueur["Sortilèges"]:
        print("- ", sort['nom'], " (", sort['type'], ") : ", sort['description'])



def ajoute_sort_alea(joueur, tab):
    aleatoire = random.randint(0, len(tab) - 1)
    ajouter_objet(joueur, "Sortilèges", tab[aleatoire])
    print("Tu viens d'apprendre le sortilège : ", tab[aleatoire]['nom'], " (", tab[aleatoire]['type'], ")")
    input("Appuie sur entrée pour continuer...")
    return aleatoire

def quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json"):
    print("\nBienvenue au quiz de magie de Poudlard !\nRéponds correctement aux 4 questions pour faire gagner des points à ta maison.\n")
    quiz = load_fichier(chemin_fichier)
    questions = []
    points = 0
    while len(questions)<4:
        aleatoire = random.choice(quiz)
        if aleatoire not in questions:
            questions.append(aleatoire)
    for i in range(4):
        if demander_texte(questions[i]["question"]) == questions[i]["reponse"]:
            print("Bonne réponse ! +25 points pour ta maison.")
            points += 25
        else:
            print("Mauvaise réponse. La bonne réponse était : ", questions[i]["reponse"])
    print("Score obtenu : ", points, " points\n")
    return points


def lancer_chapitre_3(personnage, maisons):
    apprendre_sorts(personnage)
    actualiser_points_maison(maisons, personnage["Maison"], quiz_magie(personnage))
    afficher_maison_gagnante(maisons)
    print()
    afficher_personnage(personnage)

