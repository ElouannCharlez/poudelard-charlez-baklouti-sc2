from utils.input_utils import *
from univers.maison import *
import random

def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):
    print("\nTu commences tes cours de magie à Poudlard...")
    dico_sorts=load_fichier(chemin_fichier)
    offensif, defensif, utilitaire = [], [], []
    for sort in dico_sorts:
        if sort['type']=="Offensif":
            offensif.append(sort)
        elif sort['type']=="Défensif":
            defensif.append(sort)
        else:
            utilitaire.append(sort)
    ajoute_sort_alea(joueur, offensif)
    input("Appuie sur entrée pour continuer...")
    ajoute_sort_alea(joueur, defensif)
    input("Appuie sur entrée pour continuer...")
    for i in range(3):
        del utilitaire[ajoute_sort_alea(joueur, utilitaire)]
        input("Appuie sur entrée pour continuer...")
    print("\nTu as terminé ton apprentissage de base à Poudelard !\nVoici les sortilèges que tu maîtrises désormais :\n")
    for sort in joueur["Sortilèges"]:
        print("- ", sort['nom'], " (", sort['type'], ") : ", sort['description'])

def ajoute_sort_alea(joueur, tab):
    aleatoire = random.randint(0, len(tab) - 1)
    joueur["Sortilèges"].append(tab[aleatoire])
    print("Tu viens d'apprendre le sortilège : ", tab[aleatoire]['nom'], " (", tab[aleatoire]['type'], ")")
    return aleatoire

# if __name__ == "__main__":
#     joueur={'Nom': 'Baklouti', 'Prenom': 'Youssef', 'Argent': 100, 'Inventaire': [], 'Sortilèges': [], 'Attributs': {}}
#     apprendre_sorts(joueur)

def quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json"):
    print("\nBienvenue au quiz de magie de Poudlard !\nRéponds correctement aux 4 questions pour faire gagner des points à ta maison.\n")
    questions=[]
    points=0
    while len(questions)<4:
        aleatoire = random.choice(joueur["Sortilèges"])
        if aleatoire not in questions:
            questions.append(aleatoire)
    for i in range(4):
        if demander_texte(str(i-1) + ". Quel sort " + chr(ord(questions[i]["description"][0])+32) + questions[i]["description"][1:-1] + " ?") == questions[i]["nom"]:
            print("Bonne réponse ! +25 points pour ta maison.")
            actualiser_points_maison({"Gryffondor": 0,"Serpentard": 0,"Poufsouffle": 0,"Serdaigle": 0}, joueur["Maison"], 25)
            points+=25
        else:
            print("Mauvaise réponse. La bonne réponse était : ", questions[i]["nom"])
    return points

if __name__ == "__main__":
    joueur={'Nom': 'Baklouti', 'Prenom': 'Youssef', 'Argent': 100, 'Inventaire': [], 'Sortilèges': [], 'Attributs': {}, 'Maison':'Gryffondor'}
    apprendre_sorts(joueur)
    print(quiz_magie(joueur))