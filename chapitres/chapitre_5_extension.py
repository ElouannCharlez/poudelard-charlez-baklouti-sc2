from univers.personnage import *
from utils.input_utils import *
from chapitres.chapitre_1 import creer_personnage
import random

def infiltration(personnage):
    pret=False
    choix=["entrer dans la cabine", "demander plus de détail sur le polynectar"]
    if demander_choix("Par quoi on commence ?", choix)==0:
        print()
        cabine(pret)
    explication(personnage)
    objectifs=["récupérer un cheveu de trois personnes différentes"]
    choix = choix[:1] + ["observer les arrivants"] + ["se remémorer les objectifs"]
    phase2 = False
    cheveux_restants=3
    while not phase2 :
        entree = demander_choix("Qu'est ce qu'on fait maintenant ?", choix)
        print()
        if entree == 0:
            if objectifs == ["entrer dans la cabine"]:
                if "portefeuille" not in personnage["Inventaire"]:
                    print("Vous entrez dans la cabine mais Ron vous arrête")
                    print("Ron : « Attends ! N'oublie pas le portefeuille de celui dont tu as pris l'apparence.")
                    print("Il te servira sûrement pour la suite. »")
                    print("Hermione : « Et boit cette potion ! ")
                    print("Oublie pas non plus de dire ton nom dans la cabine ! »")
                    print("Hermione : « Et dit son nom dans la cabine ! »")
            cabine(pret)
            phase2 = True
            objectifs=["voler le médaillon"]
            choix=["sortir", "créer une diversion", "se jetter sur Dolores", "se remémorer les objectifs"]
        elif entree == 1:
            cheveux_restants -= observer()
        elif entree == 2:
            objectif_restant(objectifs)
        else:
            if cheveux_restants < -1:
                print("Hermione : « laissons ces malfrats ici, on a déjà les 3 malfrats qu'il nous faut »\n")
            elif cheveux_restants == -1:
                print("Hermione : « laissons ce malfrat ici, on a déjà les 3 malfrats qu'il nous faut »\n")
            print("Vous récupérez les portefeuilles des victimes, vous connaissez maintenant leurs noms et êtes prêts à les dire dans la cabine téléphonique.")
            print("Après la finalisation de la potion, vous la buvez et devenez parfaitement méconnaissables\n")
            ajouter_objet(personnage, "Inventaire", "portefeuille")
            choix = choix[:-1]
        if objectifs != ["entrer dans la cabine"] and objectifs != ["voler le médaillon"] and cheveux_restants <= 0:
            choix.append("fouiller les corps")
            objectifs = ["entrer dans la cabine"]
            pret = True
    print("Reg Cattermole (Ron) : « On a un problème… L’apparence que j’ai prise est recherchée. Ils ont mis son portrait dans tout le hall ! \n»")
    print("Mafalda Hopkirk (Hermione) : « Alors va-t’en ! Fais semblant d’être pressé, trouve un couloir discret et rejoins-nous plus tard. »\n")
    print("Albert Runcorn (" + personnage['Nom'] + ") : « On se charge de Dolores Ombrage. Vas-y, file ! »\n")
    print("Hermione : « Ombrage dirige les interrogatoires aujourd’hui. Elle portera le médaillon sur elle. ")
    print("Pas besoin d’aller fouiller quoi que ce soit. »\n")
    print("Vous entrez dans la salle d'audience et apercevez Dolores présider la séance, son médaillon autour du cou")
    pret_sortir = False
    pret_attraper = False
    while objectifs!=["sortir"]:
        entree = demander_choix("Qu'est ce qu'on fait maintenant ?", choix)
        if entree==0:
            sortir(pret_sortir)
        elif entree==1:
            creer_diversion()
            pret_attraper = True
        elif entree==2:
            attraper_medaillon(pret_attraper)
            pret_sortir = True
            objectifs=["sortir"]
        else:
            objectif_restant()
    return None

def sortir(pret_sortir):
    pass

def creer_diversion():
    pass

def attraper_medaillon(pret_attraper):
    pass

def plan(personnage):
    print("\nDans un Londres magique tombé aux mains de Voldemort, le trio n’a qu’une option :")
    print("infiltrer le Ministère et récupérer le médaillon de Dolores Ombrage avant que tout ne s’effondre.\n")
    print("Hermione : « On n'a pas dix mille solutions, on entre par polynectar ! ")
    print("Et ensuite, on rejoint le ministère par la cabine téléphonique juste devant. »\n")
    print(str(personnage['Prenom']) + " : « On reste discrets et on se retrouve dans l’atrium dès qu’on l’a. » \n")
    print("Ron : « Et si on se fait repérer ? »\n")
    print(str(personnage['Prenom']) + " : « Alors on transplane tout de suite. Pas de seconde chance... »\n ")

def intro_polynectar():
    pass

def intro_hall():
    pass

def cabine(pret):
    print("Vous entrez dans la cabine un par un, donnez votre nom " + "de couverture "*pret + "et êtes chacun téléportés dans le Ministère")
    if not pret:
        print("Tous les sbires de Voldemort se retournent et vous fixent")
        print("Ron : « On aurrait peut-être dû suivre le plan... » Fin")
        exit()
    print("Hermione (chuchote) : Personne n'a l'air de nous avoir reconnu. On passe à la suite.\n")
def explication(personnage):
    print('\n'+ str(personnage['Prenom']), " : « Euhh... Une dernière chose... C'est quoi déjà du polynectar ? »\n")
    print("Hermione : « Tu suits vraiment rien en cours ! C'est une potion pour prendre l'apparence de quelqu'un d'autre.")
    print("Pour la concocter, il ne nous reste plus qu'un ingrédient : un cheveu des personnes dont l'on souhaite prendre l'apparence.")
    print("Pour ça, il nous faut au moins trois cibles »\n")
    print("Ron (chuchote à " + str(personnage['Prenom']) + ") : « J'aurai bien demandé mais j'ai pas osé... »\n")

def objectif_restant(objectifs):
    if objectifs==[]:
        print("On peut passer à la suite ! ")
    else:
        print("Il nous reste : ")
        for obj in objectifs:
            print("- "+ obj)
    print()
    return None
# if __name__ == '__main__':
#     perso = {'Nom': 'Baklouti', 'Prenom': 'Youssef', 'Argent': 100, 'Inventaire': [], 'Sortilèges': [], 'Attributs': {}, 'Maison': 'Gryffondor'}
#     plan(perso)

def observer():
    nb = random.randint(1,3)
    if demander_choix(str(nb) + " personnes apparaissent",["Attendre", "Attaquer par surprise"])==1:
        if nb == 3:
            print("\nVous passez derrière eux et lancez Hermione et toi le sort Incarcerous pour les ligoter.")
            print("Ron, un peu à la traîne, s'empresse de lancer le sien à son tour.")
            print("Cependant les liens, mal exécutés, furent assez lâches pour qu’un malfrat parvienne s'en défaire.\n")
            print("Ron : « J'ai besoin d'un coup de main ! Il se débat plus que prévu ! »\n")
            print("Malfrat : « Pé..Périculum ! »\n")
            print("Une étincelle rouge jaillit de la baguette du malfrat pour s'élever en flèche dans les airs.")
            print("Un par un, des renforts apparaissent alors brusquement de tous les côtés pour finalement vous encercler.")
            print("Hermione : On aurait mieux fait d'attendre le moment opportun... Fin")
            exit()
        if nb == 2:
            print("\nVous passez derrière eux et lancez, avec Hermione, le sort Incarcerous pour les ligoter.")
            print("Sans perdre de temps, Ron les endort et les cache un peu plus loin dans la ruelle, près de vous.\n")
            return 2
        if nb == 1:
            print("\nRon prend les devant et lance le sort Incarcerous pour le ligoter.")
            print("Sans perdre de temps, Hermione les endort et les déplace sans un bruit.\n")
            return 1
    elif nb==3:
        print("\nLes sbires prennent la cabine.")
        print("Hermione : « Bonne idée ! Mieux vaut les attaquer moins nombreux... »\n")
    else:
        print("\nLes sbires prennent la cabine.")
        print("Ron : « On a plus le temps d'attendre pour rien, il faut passer à l'action ! »\n")
    return 0

def lancer_chapitre5(personnage):
    plan(personnage)
    infiltration(personnage)

lancer_chapitre5(creer_personnage())