from univers.personnage import *
from utils.input_utils import *
from chapitres.chapitre_1 import creer_personnage
import random

def preparation_persos(personnage, hermione, ron):
    ajouter_objet(personnage, 'Inventaire', "vif d’or fendu")
    ajouter_objet(personnage, 'Inventaire', "plume de phenix")
    ajouter_objet(hermione, 'Inventaire', "petit grimoire")
    ajouter_objet(hermione, 'Inventaire', "polynectar")
    ajouter_objet(ron, 'Inventaire', "crapaud en chocolat")
    ajouter_objet(ron, 'Inventaire', "pierre luisante")
    ajouter_objet(ron, 'Inventaire', "écharpe de Gryffondor")
    groupe = [personnage, hermione, ron]
    for pers in groupe:
        ajouter_objet(pers, 'Sortilèges', {"nom": "Stupefy", "description": "Assomme temporairement un adversaire.", "type": "Offensif"})
        ajouter_objet(pers, 'Sortilèges', {"nom": "Confringo", "description": "Crée une explosion.", "type": "Offensif"})
        if pers != ron : # Pour donner certains sorts à certains et pas à d'autres
            ajouter_objet(pers, 'Sortilèges', {"nom": "Confundo", "description": "Rend confus son adversaire.", "type": "Offensif"})
        ajouter_objet(pers, 'Sortilèges', {"nom": "Protego", "description": "Crée un bouclier magique pour bloquer les attaques.", "type": "Défensif"})
        if pers != personnage and pers != ron:
            ajouter_objet(pers, 'Sortilèges', {"nom": "Finite Incantatem", "description": "Met fin aux sorts ou effets en cours.", "type": "Défensif"})
        ajouter_objet(pers, 'Sortilèges', {"nom": "Reparo", "description": "Répare les objets cassés.", "type": "Utilitaire"})
        ajouter_objet(pers, 'Sortilèges', {"nom": "Lumos", "description": "Fait briller de la lumière à l'extrémité de la baguette.", "type": "Utilitaire"})
        ajouter_objet(pers, 'Sortilèges', {"nom": "Nox", "description": "Éteint la lumière produite par Lumos.", "type": "Utilitaire"})
        ajouter_objet(pers, 'Sortilèges', {"nom": "Wingardium Leviosa", "description": "Fait léviter des objets.", "type": "Utilitaire"})

#################################################################################################
#################################################################################################
# Partie 1
#################################################################################################
#################################################################################################

def infiltration(personnage):
    plan_ministere(personnage)
    intro_polynectar(personnage)
    objectifs=["récupérer un cheveu de trois personnes différentes"]
    choix = ["entrer dans la cabine", "se remémorer les objectifs", "observer les arrivants"]
    phase2 = False
    pret_cabine = False
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
            cabine(pret_cabine)
            phase2 = True
        elif entree == 1:
            objectif_restant(objectifs)
        elif entree == 2:
            cheveux_restants -= observer()
        else:
            fouiller_corps(personnage, cheveux_restants)
            choix = choix[:-1]
        if objectifs != ["entrer dans la cabine"] and objectifs != ["voler le médaillon"] and cheveux_restants <= 0:
            choix.append("fouiller les corps")
            objectifs = ["entrer dans la cabine"]
            pret_cabine = True
    intro_hall(personnage)
    pret_sortir = False
    pret_attraper = False
    objectifs = ["voler le médaillon"]
    choix = ["sortir", "se remémorer les objectifs", "se jetter sur Dolores", "créer une diversion"]
    while objectifs!=["fin partie 1"]:
        entree = demander_choix("Qu'est ce qu'on fait maintenant ?", choix)
        print()
        if entree == 0:
            sortir_ministere(pret_sortir)
            if pret_sortir:
                objectifs = ["fin partie 1"]
        elif entree == 1:
            objectif_restant(objectifs)
        elif entree == 2:
            attraper_medaillon(personnage, pret_attraper)
            if pret_attraper:
                pret_sortir = True
                objectifs=["s'échapper"]
                choix = choix[:-1]
        else:
            creer_diversion()
            pret_attraper = True
            choix= choix[:-1]
    return None

def plan_ministere(personnage):
    print("\nDans un Londres magique tombé aux mains de Voldemort, le trio n’a qu’une option :")
    print("infiltrer le Ministère et récupérer le médaillon de Dolores Ombrage avant que tout ne s’effondre.\n")
    print("Hermione : « On n'a pas dix mille solutions, on entre par polynectar ! ")
    print("Et ensuite, on rejoint le ministère par la cabine téléphonique juste devant. »\n")
    print(str(personnage['Prenom']) + " : « On reste discrets et on se retrouve dans l’atrium dès qu’on l’a. » \n")
    print("Ron : « Et si on se fait repérer ? »\n")
    print(str(personnage['Prenom']) + " : « Alors on transplane tout de suite. Pas de seconde chance... »\n ")

def intro_polynectar(personnage):
    if demander_choix("Par quoi on commence ?", ["entrer dans la cabine", "demander plus de détail sur le polynectar"]) == 0:
        print()
        cabine(False)
    print('\n' + str(personnage['Prenom']), " : « Euhh... Une dernière chose... C'est quoi déjà du polynectar ? »\n")
    print("Hermione : « Tu suits vraiment rien en cours ! C'est une potion pour prendre l'apparence de quelqu'un d'autre.")
    print("Pour la concocter, il ne nous reste plus qu'un ingrédient : un cheveu des personnes dont l'on souhaite prendre l'apparence.")
    print("Pour ça, il nous faut au moins trois cibles »\n")
    print("Ron (chuchote à " + str(personnage['Prenom']) + ") : « J'aurai bien demandé mais j'ai pas osé... »\n")

def cabine(pret):
    print("Vous entrez dans la cabine un par un, donnez votre nom " + "de couverture "*pret + "et êtes chacun téléportés dans le Ministère")
    if not pret:
        print("Tous les sbires de Voldemort se retournent et vous fixent")
        print("Ron : « On aurrait peut-être dû suivre le plan... » Fin")
        exit()
    print("Hermione (chuchote) : « Personne n'a l'air de nous avoir reconnu. On passe à la suite. »")
    input("Appuie sur entrée pour continuer...")
    print()

def objectif_restant(objectifs):
    if objectifs==[]:
        print("On peut passer à la suite ! ")
    else:
        print("Il nous reste : ")
        for obj in objectifs:
            print("- "+ obj)
    print()
    return None

def observer():
    nb = random.randint(1,3)
    if demander_choix(str(nb) + " personnes apparaissent",["Attendre", "Prendre par surprise"])==1:
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

def fouiller_corps(personnage, cheveux_restants):
    if cheveux_restants < -1:
        print("Hermione : « laissons ces malfrats ici, on a déjà les 3 malfrats qu'il nous faut »\n")
    elif cheveux_restants == -1:
        print("Hermione : « laissons ce malfrat ici, on a déjà les 3 malfrats qu'il nous faut »\n")
    print("Vous récupérez les portefeuilles des victimes, vous connaissez maintenant leurs noms et êtes prêts à les dire dans la cabine téléphonique.")
    print("Après la finalisation de la potion, vous la buvez et devenez parfaitement méconnaissables\n")
    ajouter_objet(personnage, "Inventaire", "portefeuille")

def intro_hall(personnage):
    print("Reg Cattermole (Ron) : « On a un problème… L’apparence que j’ai prise est recherchée. Ils ont mis son portrait dans tout le hall ! »\n")
    print("Mafalda Hopkirk (Hermione) : « Alors va-t’en ! Fais semblant d’être pressé, trouve un couloir discret et rejoins-nous plus tard. »\n")
    print("Albert Runcorn (" + personnage['Nom'] + ") : « On se charge de Dolores Ombrage. Vas-y, file ! »\n")
    print("Hermione : « Ombrage dirige les interrogatoires aujourd’hui. Elle portera le médaillon sur elle. ")
    print("Pas besoin d’aller fouiller quoi que ce soit. »\n")
    print("Vous entrez dans la salle d'audience et apercevez Dolores présider la séance, son médaillon autour du cou\n")

def sortir_ministere(pret_sortir):
    if not pret_sortir:
        print("Hermione : « C'est pas le moment de se défiler ! »\n")
    else:
        print("Vous rejoignez Ron dans l’entrée et transplanez immédiatement.")
        print("Vous réapparaissez dans un sous-bois sombre, personne dans les environs.")
        print("Le médaillon en votre possession, vous le détruisez en combinant vos pouvoirs, rendant alors Voldemort plus faible.")

def creer_diversion():
    print("Hermione (s'exclame) : « Présidente Ombrage ! Ce dossier est remplit d’incohérences majeures !")
    print("Il n'y a qu'une possibilité : un espion s'est infiltré chez nous ! »\n")
    print("L'auditorium de lève troublé et se précipite vers Ombrage pour essayer d'avoir des réponses.\n")

def attraper_medaillon(personnage, pret_attraper):
    if not pret_attraper:
        print(str(personnage['Prenom']) + " : « Tout le monde regarde Ombrage, aucune chance de lui prendre son médaillon sans être intercepté »\n")
    else:
        print("Vous réagissez dans le brouhaha, vous extirpez de la foule et vous jetez sur elle.")
        print("Une fois devant elle, vous lancez un Expelliarmus discret, recouvert par le son de la foule et récupérez son médaillon")
        print("Ombrage comprend qu'elle est visée par une attaque et se débat violemment")
        print("Vous êtes déjà éloignés qu'Ombrage parvient enfin à s'écrier :\n")
        print("Ombrage : « Mon médaillon ! »\n")
    return None

#################################################################################################
#################################################################################################
# Partie 2
#################################################################################################
#################################################################################################




def gringotts(personnage, hermione, ron):
    personnage, hermione, ron = aide(personnage, hermione, ron)
    narration(personnage)
    groupe = [personnage, hermione, ron]
    avancer = 0
    pieges = 0
    for i in range(12):
        perso_en_tete = groupe[random.randint(0,2)]
        numero = random.randint(1,11)
        if numero - 3 <= 0:
            adv = ["gardes", "trésorier", "renforts"][random.randint(0, 2)]
            print("ATTENTION ! Le" + " " * (adv == "trésorier") + "s " * (adv != "trésorier") + adv + " arrive" + "nt" * (adv != "trésorier"), end="")
            input("...")
            if pieges != 0:
                pieges -= 1
                avancer += 1
                print("\nVos poursuivants devaient vous rattraper mais ils sont tombés dans votre piège, c'est déjà ça de moins !\n")
            else:
                avancer += rattraper_gobelins(perso_en_tete, adv)
        elif numero - 6 <= 0:
            avancer += piege_declenche(perso_en_tete)
        elif numero - 9 <= 0:
            avancer += choisir_chemin(perso_en_tete)
        else:
            res_dragon = (dragon(perso_en_tete))
            avancer += res_dragon[0]
            pieges += res_dragon[1]
    sortir_banque(avancer)
    return None

def aide(personnage, hermione, ron):
    print("Avant de vous laissez, Hagrid vous propose de vous acheter des objets pouvant vous être utiles pour la suite")
    input("Vous entrez maintenant dans L’Oeil du Gobelin...")
    print("\nHagrid : « Choisissez un objet chacun ! C'est moi qui me charge du reste ! »\n")
    stock = ["clé gobeline", "potion de vie", "livre de sort", "anneau aquatique", "baguette d'ordre supérieure", "planche miniature", "carte", "fumigène gobeline", "sablier de suspension"]
    print("Bonjour !")
    print("Voici nos articles :")
    for i_art in range(len(stock)):
        print(str(i_art+1) + "- " + stock[i_art])
    groupe_prenom = [personnage["Prenom"], hermione["Prenom"], ron["Prenom"]]
    groupe = [personnage, hermione, ron]
    for i_pers in range(3):
        i_objet = demander_nombre("\n" + groupe_prenom[i_pers] + " qu'est ce qui peut t'intéresse ? ", 1, 10) - 1
        ajouter_objet(groupe[i_pers], "Inventaire", stock[i_objet])
    print("\nHagrid : « Bon courage pour la suite, je vous laisse vous occupez du reste ! »\n")
    return personnage, hermione, ron

def narration(personnage):
    print("Vous entrez dans Gringotts, une banque immense dirigé uniquement par des gobelins")
    print("Sous couverture, vous réussissez à persuader un des trésorier pour voir le dernier artefact qui se dresse au travers de votre route :")
    print("La coupe de Poufsouffle")
    input("...")
    print("Gobelin : « Ils ont touchés la coupe ! ALERTE ! »")
    print("Alors que vous cherchez un moyen pour fuir, dans la pénombre, vous apercevez un dragon")
    print("Malgré vos efforts pour le réveiller, il ne bouge pas d'un pouce...")
    print("C'est alors que vous entendez un sifflet strident, d'un quart de tour, vous essayez de sortir par là où vous êtes entrés :")
    print("Les escaliers", end="")
    input("...")
    print()
    return None

def rappel_capacite(personnage):
    print("C'est " + personnage["Prenom"] + " qui mène le groupe !\n")
    print("Rappel des capacités de " + personnage["Prenom"] + " :")
    print("Voici votre inventaire :")
    for objet in personnage["Inventaire"]:
        print("- " + objet)
    print("Voici vos sortilèges :")
    for sort in personnage["Sortilèges"]:
        print("- " + sort["nom"] + " : " + sort["description"])
    return None

def rattraper_gobelins(personnage, adv):
    print()
    rappel_capacite(personnage)
    print()
    if adv == "gardes":
        return combat_gardes(personnage)
    elif adv == "trésorier":
        return combat_tresorier(personnage)
    return combat_renforts(personnage)

def combat_gardes(personnage):
    print("Des gardes postés devant une porte vous remarque...")
    print("Préparés, ils possèdent un casque enchanté les empèchant d'être confus")
    print("Il faudrait trouver un moyen de les immobiliser")
    if demander_choix("\nC'est le moment d'attaquer !", ["utiliser un objet", "utiliser un sort"]) == 0:
        i_objet = demander_choix("\nQuel objet utiliser ?", personnage["Inventaire"])
        if personnage["Inventaire"][i_objet] == "fumigène gobeline":
            print("\nVous utilisez votre fumigène et vous frayez un chemin\n")
            del personnage["Inventaire"][i_objet]
            return 1
        print("\nCela ne semble pas être idéal")
    else:
        sort_choisi = demander_choix("\nQuel sort utiliser ?", personnage["Sortilèges"])
        if personnage["Sortilèges"][sort_choisi]["nom"] == "Stupefy":
            print("\nVous passez sans problèmes pendant que vos adversaires sont immobiles\n")
            return 1
        print("\nCela n'a eu aucun effet")
    print("Vous êtes ralentis mais parvenez quand même à passer\n")
    return 0

def combat_tresorier(personnage):
    print("Le trésorier vous rattrape...")
    print("Grâce à son intellect et à son abilleté avec sa baguette, il sera difficile de le gêner avec quoi que ce soit")
    print("Il faudrait couper le chemin en deux pour qu'il ne puisse plus monter et vous rejoindre")
    if demander_choix("\nC'est le moment d'attaquer !", ["utiliser un objet", "utiliser un sort"]) == 0:
        i_objet = demander_choix("\nQuel objet utiliser ?", personnage["Inventaire"])
        if personnage["Inventaire"][i_objet] == "fumigène gobeline":
            print("\nVous utilisez votre fumigène et vous frayez un chemin\n")
            del personnage["Inventaire"][i_objet]
            return 1
        print("\nCela ne semble pas être idéal")
    else:
        sort_choisi = demander_choix("\nQuel sort utiliser ?", personnage["Sortilèges"])
        if personnage["Sortilèges"][sort_choisi]["nom"] == "Confringo":
            print("\nVous lancez votre sort sur le sol pour empècher le trésorier de passer et reprenez votre montée\n")
            return 1
        print("\nCela n'a eu aucun effet")
    print("Vous êtes ralentis mais parvenez quand même à passer\n")
    return 0


def combat_renforts(personnage):
    print("Des renforts débarquent devant vous un peu plus haut dans les escaliers...")
    print("Trop nombreux, il n'est pas possible de les immobiliser")
    print("Il faudrait trouver un moyen de les désorienter")
    if demander_choix("\nC'est le moment d'attaquer !", ["utiliser un objet", "utiliser un sort"]) == 0:
        i_objet = demander_choix("\nQuel objet utiliser ?", personnage["Inventaire"])
        if personnage["Inventaire"][i_objet] == "fumigène gobeline":
            print("\nVous utilisez votre fumigène et vous frayez un chemin\n")
            del personnage["Inventaire"][i_objet]
            return 1
        print("\nCela ne semble pas être idéal")
    else:
        sort_choisi = demander_choix("\nQuel sort utiliser ?", personnage["Sortilèges"])
        if personnage["Sortilèges"][sort_choisi]["nom"] == "Confundo":
            print("\nVous passez sans problèmes pendant que vos adversaires sont étourdis\n")
            return 1
        print("\nCela n'a eu aucun effet")
    print("Vous êtes ralentis mais parvenez quand même à passer\n")
    return 0

def piege_declenche(personnage):
    faiblesses = ["Finite Incantatem", "sablier de suspension"]
    print("Vous êtes en train de monter quand soudainement un piège se déclenche sous vos pieds", end="")
    input("...")
    print()
    rappel_capacite(personnage)
    choix = demander_choix("\nQue souhaitez vous faire ?", ["utiliser un objet", "utiliser un sort", "esquiver"])
    if choix == 0:
        obj_choisi = demander_choix("\nQuel objet utiliser ?", personnage["Inventaire"])
        if personnage["Inventaire"][obj_choisi] in faiblesses:
            print("\nVous utilisisez le sablier pour immobiliser le piège l'espace d'un instant vous permettant alors de l'esquiver")
            print("Cependant, la durée trop brève et l'activation du piège un peu retardée ne vous a pas permit de récupérer votre sablier\n")
            del personnage['Inventaire'][obj_choisi]
            return 1
        print("\nVous essayez de désamorcer le piège avec " + personnage['Inventaire'][obj_choisi] + " mais cela ne semble pas être une bonne idée")
    elif choix == 1:
        sort_choisi = demander_choix("\nQuel sort utiliser ?", personnage["Sortilèges"])
        if personnage["Sortilèges"][sort_choisi]["nom"] in faiblesses:
            print("\nBingo !")
            print("Vos connaissances vous ont permit de désamorcer le piège efficacement\n")
            return 1
        print("\nVous essayez de désamorcer le piège avec " + personnage["Sortilèges"][sort_choisi]["nom"] + " mais cela ne fonctionne pas")
    else:
        print("\nLe piège se déclenche trop rapidement, vous êtes prit dedans mais parvenez à vous en défaire")
    print("Vous êtes ralentis l'espace d'un instant\n")
    return 0

def choisir_chemin(personnage):
    possibilites = []
    nb_chemins = random.randint(2,3)
    print("Vous avez maintenant devant vous différentes voies à emprunter", end="")
    input("...")
    print()
    rappel_capacite(personnage)
    for i in range(nb_chemins):
        numero = random.randint(1,10)
        if numero - 4 <= 0:
            possibilites.append("chemin sûr")
        elif numero - 7 <= 0:
            possibilites.append("raccourci cassé")
        else:
            possibilites.append("porte")
    choix = demander_choix("\nQuelle route emprunter", possibilites)
    if possibilites[choix] == "chemin sûr":
        print("\nVous continuez à avancer dans la banque\n")
        return 1
    elif possibilites[choix] == "porte":
        return porte(personnage)
    return raccourci_casse(personnage)

def porte(personnage):
    faiblesses_porte = ["clé gobeline"]
    choix = demander_choix("\nQue souhaitez vous faire ?", ["utiliser un objet", "forcer la porte"])
    if choix == 0:
        choisi = demander_choix("\nQuel objet utiliser ?", personnage["Inventaire"])
        if personnage["Inventaire"][choisi] in faiblesses_porte:
            print("\nVous utilisez votre clé gobeline et débouchez sur un raccourci !")
            print("Dommage que votre passepartout se soit désagrégé dans la serrure... il sera maintenant difficile d'ouvrir les portes\n")
            del personnage['Inventaire'][choisi]
            return 2
        print("\nVous essayez d'ouvrir la porte avec " + personnage["Inventaire"][choisi] + " mais la porte reste de marbre")
    else:
        print("\nLa porte est blindée, impossible de lui faire le moindre dommage ni de l'ouvrir")
    print("Vous faites un détours et perdez du temps\n")
    return 0

def raccourci_casse(personnage):
    faiblesses_chemin_casse = ["Reparo", "planche miniature"]
    choix = demander_choix("\nQue souhaitez vous faire ?", ["utiliser un objet", "utiliser un sort", "passer par dessus"])
    if choix == 0:
        obj_choisi = demander_choix("\nQuel objet utiliser ?", personnage["Inventaire"])
        if personnage["Inventaire"][obj_choisi] in faiblesses_chemin_casse:
            print("\nVous frapper votre planche sur le sol pour qu'elle retrouve sa taille originelle.")
            print("Vous la placez par dessus l'énorme trou et réussissez à vous créez un raccourci !")
            print("Maintenant que votre planche a retrouvé sa taille normale, il sera difficile de la transporter...")
            print("Et c'est pour cela que vous la laissez derrière\n")
            del personnage['Inventaire'][obj_choisi]
            return 2
        print("\nVous essayez de trouver un moyen de passer avec " + personnage['Inventaire'][obj_choisi] + " mais cela ne semble pas être une bonne idée")
    elif choix == 1:
        sort_choisi = demander_choix("\nQuel sort utiliser ?", personnage["Sortilèges"])
        if personnage["Sortilèges"][sort_choisi]["nom"] in faiblesses_chemin_casse:
            print("\nBonne idée !")
            print("Vous réussissez à réparer le chemin grâce aux débrits qui vous crée alors un raccourci\n")
            return 2
        print("\nVous essayez de trouver un moyen de passer avec " + personnage["Sortilèges"][sort_choisi]["nom"] + " mais cela ne fonctionne pas")
    else:
        print("\nLe trou est bien trop grand, impossible de traverser")
    print("Vous faites un détours et perdez du temps\n")
    return 0

def dragon(personnage):
    print("Le dragon s'élance dans les airs et s'apprête à vous confronter pour défendre son trésor", end="")
    input("...")
    print()
    rappel_capacite(personnage)
    if random.randint(1,10) <= 6: # proba de 60%
        return dragon_attaque(personnage)
    return dragon_lave(personnage)

def dragon_attaque(personnage):
    print("\nSa gueule s'illumine, le dragon lance alors une bourasque de feu droit sur vous !\n")
    choix = demander_choix("Comment réagissez-vous ?", ["utiliser un objet", "utiliser un sort", "esquiver par le côté"])
    faiblesses_dragon = ["Protego", "anneau aquatique"]
    if choix == 0:
        obj_choisi = demander_choix("\nQuel objet utiliser ?", personnage["Inventaire"])
        if personnage["Inventaire"][obj_choisi] in faiblesses_dragon:
            print("\nVous utilisez votre anneau et brisez ces flammes sans le moindre problème")
            print("Cependant, à cause de la trop grande puissances de ses flammes l'anneau ne sera plus d'aucune utilité\n")
            del personnage['Inventaire'][obj_choisi]
            return 1, 0
        print("\nVous envisager de contrer les flammes avec " + personnage['Inventaire'][obj_choisi] + " mais cela ne semble pas être une bonne idée")
    elif choix == 1:
        sort_choisi = demander_choix("\nQuel sort utiliser ?", personnage["Sortilèges"])
        if personnage["Sortilèges"][sort_choisi]["nom"] in faiblesses_dragon:
            print("\nVous vous protégez sans aucun problème et continuez votre montée\n")
            return 1, 0
        print("\nVous essayez de contrer les flammes avec " + personnage["Sortilèges"][sort_choisi]["nom"] + " mais cela ne fonctionne pas")
    else:
        print("\nLa bourasque englobe une zone trop large, vous n'avez plus le temps pour réagir")
    print("Vous vous soignez avant de reprendre votre montée\n")
    return 0, 0

def dragon_lave(personnage):
    print("\nSa gueule s'illumine, le dragon prend comme une grande inspiration et fait jaillir une trainée de feu devant vous !\n")
    if "anneau aquatique" in personnage["Inventaire"]:
        print("L'anneau aquatique réagit de lui même et fait disparaître ces flammes sur le champs")
        print("Vous continuez votre montée\n")
        return 2, 0
    print("Impossible de passer ou d'éteindre ses flammes")
    print("Pendant qu'elles s'éteignent, vous parvenez à fabriquer un piège pour esquiver un assaut futur de la part des gobelins")
    print("Vous êtes retardés mais mieux préparés\n")
    return 0, 1

def sortir_banque(avancer):
    if avancer > 8:
        print("Vous réussissez à vous enfuir le médaillon en main !")
        print("Vous retrouvez Hagrid un peu plus loin et lui remettez le médaillon pour qu'il le détruise")
        print("Il ne vous reste plus qu'à rejoindre Voldemort et le vaincre", end="")
        input(...)
        print()
        return None
    print("Vous avez été trop retardés... Les sbires de Voldemort vous capturent et replacent la coupe... Fin")
    exit()

#################################################################################################
#################################################################################################
# Partie 3
#################################################################################################
#################################################################################################

def detraqueurs(personnage, hermione, ron, chemin_fichier = "../data/map_détraqueurs.json"):
    narration_detra(personnage, hermione, ron)
    map = load_fichier(chemin_fichier)
    terminer = False
    pos_j = [15, 9]
    pos_d = {"d1": {"pos": [3, 11], "furie": False, "stun": False}, "d2": {"pos": [5, 6], "furie": False, "stun": False}, "d3": {"pos": [7, 11], "furie": False, "stun": False}, "d4": {"pos": [9, 8], "furie": False, "stun": False}}
    sort = 1
    while terminer == False:
        print("\n\n\n\n\n\n")
        afficher_carte(map, pos_j)
        terminer, pos_j, pos_d, sort = deplacer(map, pos_j, pos_d, personnage, sort)
    return None

def narration_detra(personnage, hermione, ron):
    print("Pour rejoindre Voldemort, il va falloir passer par le biais d'un labyrinthe !")
    print("Hagrid ne peut pas tous vous emmener directement à son repère car c'est un sort très coûteux en énergie")
    print("Pour t'y rendre, il faudra donc que tu esquives les détraqueurs (D)")
    print("Quand à toi, tu représentes un '@', le chemin un '.', et les murs des '#'")
    print("Enfin, les détraqueurs fonctionnent de deux manières :")
    print("- S'ils ne te voient pas ils èrent aléatoirement")
    print("- Si tu es à au plus 5 cases d'eux, ils se metterons en mode furie")
    print("C'est un mode où ils te pourchassent pendant 4 tours jusqu'à être fatigué (stun) pendant 2 tours avant de reprendre la chasse ")
    print("S'ils t'attrapent... Soit tu essayes de fuir qui peut marcher, soit tu utilises le sort 'Expecto Patronum' !")
    print("C'est un sort qui étourdis le détraqueur mais n'est utilisable qu'une fois ( trop d'énergie )")
    input("\nBonne Chance...")
    ajouter_objet(personnage,"Sortilèges",{"nom": "Expecto Patronum", "description": "Convoque un Patronus pour repousser les Détraqueurs.", "type": "Défensif"})

def afficher_carte(map, pos_j):
    for ligne in map:
        print(ligne)

def deplacer(map, pos_j, pos_d, personnage, sort):
    fini, pos_j = deplacer_j(map, pos_j)
    if fini:
        return True, pos_j, pos_d, sort
    for detra in pos_d:
        pos_d[detra], sort = deplacer_d(map, pos_d[detra], pos_j, personnage, sort)
    return False, pos_j, pos_d, sort

def deplacer_j(map, pos_j):
    cases_deplacement = []
    directions = []
    if map[pos_j[0] - 1][pos_j[1]] not in '#D':
        cases_deplacement.append([pos_j[0] - 1, pos_j[1]])
        directions.append('haut')
    if map[pos_j[0]][pos_j[1] + 1] not in '#D':
        cases_deplacement.append([pos_j[0], pos_j[1] + 1])
        directions.append('droite')
    if map[pos_j[0] + 1][pos_j[1]] not in '#D':
        cases_deplacement.append([pos_j[0] + 1, pos_j[1]])
        directions.append('bas')
    if map[pos_j[0]][pos_j[1] - 1] not in '#D':
        cases_deplacement.append([pos_j[0], pos_j[1] - 1])
        directions.append('gauche')
    if directions == []:
        return False, pos_j
    choix = demander_choix("\nQuelle direction prendre ?", directions)
    new_pos = cases_deplacement[choix]
    if map[new_pos[0]][new_pos[1]] == 'S':
        return True, new_pos
    map[pos_j[0]] = map[pos_j[0]][:pos_j[1]] + '.' + map[pos_j[0]][pos_j[1]+1:]
    map[new_pos[0]] = map[new_pos[0]][:new_pos[1]] + '@' + map[new_pos[0]][new_pos[1]+1:]
    return False, new_pos

def deplacer_d(map, detra, pos_j, personnage, sort):
    new_pos = None
    if abs(pos_j[0] - detra["pos"][0]) + abs(pos_j[1] - detra["pos"][1]) <= 5 and detra["furie"] == 0 and detra["stun"] == 0:
        detra["furie"] = 4
    if detra["stun"] != 0:
        new_pos = detra["pos"]
        detra["stun"] -= 1
    elif detra["furie"] == 0:
        new_pos = deplacer_aleatoirement(map, detra)
        map[detra["pos"][0]] = map[detra["pos"][0]][:detra["pos"][1]] + '.' + map[detra["pos"][0]][detra["pos"][1] + 1:]
        map[new_pos[0]] = map[new_pos[0]][:new_pos[1]] + 'D' + map[new_pos[0]][new_pos[1] + 1:]
        detra["pos"] = new_pos
    else:
        dico_pos = {"("+str(detra["pos"][0])+", "+str(detra["pos"][1])+")" : [detra["pos"], 0, []]}
        for i in range(5):
            ajout=[]
            for possibilite in dico_pos:
                possi = dico_pos[possibilite][0]
                if ( "("+str(possi[0] - 1)+", "+str(possi[1])+")" not in dico_pos ) and map[possi[0] - 1][possi[1]] not in "#D":
                    ajout.append(("("+str(possi[0] - 1)+", "+str(possi[1])+")", [(possi[0] - 1, possi[1]), i, dico_pos[possibilite][2]+[0]]))

                if ( "("+str(possi[0])+", "+str(possi[1] + 1)+")" not in dico_pos ) and map[possi[0]][possi[1] + 1] not in "#D":
                    ajout.append(("("+str(possi[0])+", "+str(possi[1] + 1)+")", [(possi[0], possi[1] + 1), i, dico_pos[possibilite][2]+[1]]))

                if ( "("+str(possi[0] + 1)+", "+str(possi[1])+")" not in dico_pos ) and map[possi[0] + 1][possi[1]] not in "#D":
                    ajout.append(("("+str(possi[0] + 1)+", "+str(possi[1])+")", [(possi[0] + 1, possi[1]), i, dico_pos[possibilite][2]+[2]]))

                if ( "("+str(possi[0])+", "+str(possi[1] - 1)+")" not in dico_pos ) and map[possi[0]][possi[1] - 1] not in "#D":
                    ajout.append(("("+str(possi[0])+", "+str(possi[1] - 1)+")", [(possi[0], possi[1] - 1), i, dico_pos[possibilite][2]+[3]]))
            for j in range(len(ajout)):
                    dico_pos[ajout[j][0]] = ajout[j][1]
        for cle in dico_pos:
            if cle == "("+str(pos_j[0])+", "+str(pos_j[1])+")":
                ou_aller = dico_pos[cle][2][0]
                if ou_aller == 0:
                    new_pos = [detra["pos"][0] - 1, detra["pos"][1]]
                elif ou_aller == 1:
                    new_pos = [detra["pos"][0], detra["pos"][1] + 1]
                elif ou_aller == 2:
                    new_pos = [detra["pos"][0] + 1, detra["pos"][1]]
                else:
                    new_pos = [detra["pos"][0], detra["pos"][1] - 1]
        if new_pos == None:
            new_pos = deplacer_aleatoirement(map, detra)
        if map[new_pos[0]][new_pos[1]] == '@':
            print()
            res = se_defendre(personnage, sort)
            if res == False:
                print("\nVous vous êtes fait attrapé par un détraqueur... Fin")
                exit()
            elif res == "sort":
                sort -= 1
        else:
            map[detra["pos"][0]] = map[detra["pos"][0]][:detra["pos"][1]] + '.' + map[detra["pos"][0]][detra["pos"][1] + 1:]
            map[new_pos[0]] = map[new_pos[0]][:new_pos[1]] + 'D' + map[new_pos[0]][new_pos[1] + 1:]
        detra["pos"] = new_pos
        detra["furie"] -= 1
        if detra["furie"] == 0:
            detra["stun"] = 2
    return detra, sort

def deplacer_aleatoirement(map, detra):
    cases_deplacement = []
    if map[detra["pos"][0] - 1][detra["pos"][1]] not in '#D':
        cases_deplacement.append([detra["pos"][0] - 1, detra["pos"][1]])
    if map[detra["pos"][0]][detra["pos"][1] - 1] not in '#D':
        cases_deplacement.append([detra["pos"][0], detra["pos"][1] - 1])
    if map[detra["pos"][0] + 1][detra["pos"][1]] not in '#D':
        cases_deplacement.append([detra["pos"][0] + 1, detra["pos"][1]])
    if map[detra["pos"][0]][detra["pos"][1] + 1] not in '#D':
        cases_deplacement.append([detra["pos"][0], detra["pos"][1] + 1])
    if cases_deplacement == []:
        return detra["pos"]
    return cases_deplacement[random.randint(0, len(cases_deplacement) - 1)]

def se_defendre(personnage, sort):
    rappel_capacite(personnage)
    choix = demander_choix("\nDéfendez-vous !", ["Utiliser un objet", "Utiliser un sort", "Fuir"])
    if choix == 0:
        demander_choix("\nQuel objet utiliser ?", personnage["Inventaire"])
        print("\nVous essayer mais impossible de vous défendre avec cet objet")
        return False
    elif choix == 1:
        if personnage["Sortilèges"][demander_choix("\nQuel sort utiliser ?", personnage["Sortilèges"])]["nom"] == "Expecto Patronum":
            if sort > 0:
                print("\n" + personnage["Prenom"] + " : « Expecto Patronum ! »")
                print("Lancer ce sort vous a épuisé ! Vous n'avez pas l'air d'être en capacité de le relancer...\n")
                return "sort"
            else:
                return False
    fuite_reussi = random.randint(1,4) == 1 # 25%
    if not fuite_reussi:
        print("\nVotre fuite n'a pas aboutie...")
        return False
    print("Vous vous êtes échappé !")
    return "fuite"


def lancer_chapitre5(personnage):
    hermione = {'Nom': 'Granger', 'Prenom': 'Hermione', 'Argent': 250, 'Inventaire': [], 'Sortilèges': [], 'Attributs': {'courage': 7, 'intelligence': 10, 'loyauté': 9, 'ambition': 6}}
    ron = {'Nom': 'Weasley', 'Prenom': 'Ron', 'Argent': 40, 'Inventaire': [], 'Sortilèges': [], 'Attributs': {'courage': 7, 'intelligence': 5, 'loyauté': 10, 'ambition': 8}}
    preparation_persos(personnage, hermione, ron)
    infiltration(personnage)
    gringotts(personnage, hermione, ron)
    detraqueurs(personnage, hermione, ron)
    print("\n Bravo mais Voldemort est en vacance... Il n'y aura pas de combat...")


lancer_chapitre5(creer_personnage())