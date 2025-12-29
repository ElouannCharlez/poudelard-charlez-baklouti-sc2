import random
from utils.input_utils import load_fichier
from univers.maison import actualiser_points_maison
from univers.personnage import afficher_personnage



def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    membres = equipe_data
    equipe = {'nom':maison,'score': 0,'a_marque': 0,'a_stoppe': 0,'attrape_vifdor': False,}
    liste_joueur = membres[maison]['joueurs']
    if est_joueur==True:
        liste_joueur = [joueur["Prenom"]+" "+joueur["Nom"]+" (Attrapeur)"] + liste_joueur[1:]
    equipe['joueurs'] = liste_joueur
    return equipe


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = random.randint(1,10)
    butteur = ""
    if proba_but >=6 :
        if joueur_est_joueur==True:
            butteur = equipe_attaque["joueurs"][0]
        else :
            butteur = random.choice(equipe_attaque["joueurs"])
        equipe_attaque["score"] += 10
        equipe_attaque["a_marque"] += 1
        print( butteur +" marque un but pour "+ equipe_attaque['nom']+"! (+10 points) ")
    else :
        equipe_defense["a_stoppe"] += 1
        print(equipe_defense['nom']+" bloque l’attaque !")



def apparition_vifdor():
    return random.randint(1,6)==6

# if __name__ == '__main__':
#     for i in range(10):
#         print(apparition_vifdor())

def attraper_vifdor(e1, e2):
    attrapeur=random.randint(1,2)
    if attrapeur==1:
        #e1['score'] += 150
        e1['attrape_vifdor'] = True
        return e1
    else :
        #e2['score'] += 150
        e2['attrape_vifdor'] = True
        return e2


def afficher_score(e1, e2):
    print("Score actuel :")
    print("- " + e1['nom'] + " : " + str(e1['score']) + " point" + 's'*(e1['score']>1))
    print("- " + e2['nom'] + " : " + str(e2['score']) + " point" + 's'*(e2['score']>1))

def afficher_equipe(maison, equipe):
    print("Equipe de " + maison + " :")
    for i in range (len(equipe['joueurs'])):
        print("- "+equipe['joueurs'][i])

def match_quidditch(joueur, maisons):
    equipe_data = load_fichier('../data/equipes_quidditch.json')
    equipes = ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
    maison = joueur['Maison']
    for i in range (3):
        if equipes[i]==maison:
            del equipes[i]
    maison_adverse = random.choice(equipes)
    print("Match de Quidditch : "+maison+" vs " +maison_adverse+" !")
    equipe = creer_equipe(maison, equipe_data,True, joueur)
    equipe_adverse = creer_equipe(maison_adverse, equipe_data,False)
    afficher_equipe(maison, equipe)
    print()
    afficher_equipe(maison_adverse, equipe_adverse)
    print("Tu joues pour " + maison + " en tant qu’Attrapeur")
    print()
    msg_vifdor = False
    i=0
    while i<20 and msg_vifdor==False:
        print("━━━ Tour" +str(i+1)+" ━━━")
        tentative_marque(equipe, equipe_adverse, i%2==0)
        afficher_score(equipe, equipe_adverse)
        vifdor_existe = apparition_vifdor()
        if vifdor_existe == True:
            msg_vifdor = True
            equipe_gagnante = attraper_vifdor(equipe, equipe_adverse)
        else:
            print("Appuyez sur Entrée pour continuer...")
            input()
        i += 1
    if msg_vifdor == True:
        print("Le Vif d’Or a été attrapé par " + equipe_gagnante['nom'] + " ! (+150 points)")
        equipe_gagnante['score'] += 150
        print("Fin du match !")
        afficher_score(equipe, equipe_adverse)
        print("Résultat final :")
        print("Le Vif d’Or a été attrapé par " + equipe_gagnante['nom'])
        print("+150 points pour " + equipe_gagnante['nom'] + " ! Total : " + str(equipe_gagnante['score']) + " points.")
        print("La maison gagnante est " + equipe_gagnante['nom'] + " avec " + str(equipe_gagnante['score']) + " points !")
        print(equipe_gagnante['nom'] + " remporte le match...")
        actualiser_points_maison(maisons, equipe_gagnante['nom'], 500)
        print("La maison gagnante est " + equipe_gagnante['nom'] + " avec " + str(equipe_gagnante['score'] + 500) + " points !")
    elif equipe['score'] > equipe_adverse['score']:
        print("Fin du match !")
        afficher_score(equipe, equipe_adverse)
        print("Résultat final :")
        print("La maison gagnante est " + equipe['nom'] + " avec " + str(equipe['score']) + " points !")
        print(equipe['nom'] + " remporte le match...")
        actualiser_points_maison(maisons, equipe['nom'], 500)
        print("La maison gagnante est " + equipe['nom'] + " avec " + str(equipe['score'] + 500) + " points !")
    elif equipe['score'] < equipe_adverse['score']:
        print("Fin du match !")
        afficher_score(equipe, equipe_adverse)
        print("Résultat final :")
        print("La maison gagnante est " + equipe_adverse['nom'] + " avec " + str(equipe_adverse['score']) + " points !")
        print(equipe_adverse['nom'] + " remporte le match...")
        actualiser_points_maison(maisons, equipe_adverse['nom'], 500)
        print("La maison gagnante est " + equipe_adverse['nom'] + " avec " + str(equipe_adverse['score'] + 500) + " points !")
    elif equipe['score'] == equipe_adverse['score']:
        print("Fin du match !")
        afficher_score(equipe, equipe_adverse)
        print("Match nul !")
        print("Pas de gagnant :(")


def lancer_chapitre4_quidditch(joueur, maisons):
    print("Le chapitre 4 s’ouvre… et la suite t’attend.")
    input("Appuie sur entrée pour continuer...")
    print()
    match_quidditch(joueur, maisons)
    print("Fin du Chapitre 4 — Quelle performance incroyable sur le terrain ! ")
    gagnante = "Gryffondor"
    for maison in maisons.keys():
        if maisons[maison] > maisons[gagnante]:
            gagnante = maison
    print("La grande gagnante de la Coupe des Quatre Maisons est la Maison " + gagnante + "!")
    afficher_personnage(joueur)

if __name__ == "__main__":
    maisons = {"Gryffondor": 0, "Serpentard": 0, "Poufsouffle": 0, "Serdaigle": 0}
    joueur = {'Nom': 'Baklouti', 'Prenom': 'Youssef', 'Argent': 100, 'Inventaire': [], 'Sortilèges': [], 'Attributs': {'courage': 7, 'intelligence': 9, 'loyauté': 8, 'ambition': 3},'Maison':"Gryffondor"}
    lancer_chapitre4_quidditch(joueur, maisons)