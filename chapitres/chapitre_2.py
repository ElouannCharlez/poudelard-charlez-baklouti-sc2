from utils.input_utils import demander_choix
from univers.maison import repartition_maison

def  rencontrer_amis(joueur):
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord...")
    print("Un garçon roux entre dans votre compartiment, l’air amical.")
    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ?")
    choix_1 = demander_choix("Que répondez-vous ?",['Bien sûr, assieds-toi !','Désolé, je préfère voyager seul.'])
    if choix_1==0:
        joueur['Attributs']['loyauté']+=1
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable !")
    else:
        joueur['Attributs']['ambition'] += 1
    print("Une fille entre ensuite, portant déjà une pile de livres.")
    print("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?")
    choix_2 = demander_choix("Que répondez-vous ?",['Oui, j’adore apprendre de nouvelles choses !','Euh… non, je préfère les aventures aux bouquins.'])
    if choix_2==0:
        joueur['Attributs']['intelligence'] += 1
    else:
        joueur['Attributs']['courage'] += 1
        print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un jour !")
    print("Puis un garçon blond entre avec un air arrogant.")
    print("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    choix_3 = demander_choix("Comment réagissez-vous ?",['Je lui serre la main poliment.','Je l’ignore complètement.','Je lui réponds avec arrogance.'])
    if choix_3==0:
        joueur['Attributs']['ambition'] += 1
    elif choix_3==1:
        joueur['Attributs']['loyauté'] += 1
        print("Drago fronce les sourcils, vexé. — Tu le regretteras !")
    else:
        joueur['Attributs']['courage'] += 1
    print("Le train continue sa route. Le château de Poudlard se profile à l’horizon...")
    print("Tes choix semblent déjà en dire long sur ta personnalité !")
    print("Tes attributs mis à jour : ",joueur['Attributs'])

from chapitres.chapitre_1 import *
joueur=creer_personnage()
# rencontrer_amis(joueur)

def mot_de_bienvenue():
    print("Bienvenue à Poudlard ! Que cette année vous apporte de belles découvertes et beaucoup de magie.")
    input()

def ceremonie_repartition(joueur):
    print("La cérémonie de répartition commence dans la Grande Salle...")
    print("Le Choixpeau magique t’observe longuement avant de poser ses questions : ")
    questions = [
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
        ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te décrit le mieux ?",
            ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
             ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, tu...",
            ["Fonces sans hésiter", "Cherches la meilleure stratégie",
             "Comptes sur tes amis", "Analyses le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]
    choix_peau = repartition_maison(joueur, questions)
    joueur['Maison']=choix_peau
    print("Le Choixpeau s’exclame :",choix_peau,"!!!")
    print("Tu rejoins les élèves de",choix_peau,"sous les acclamations !")
    return choix_peau

#ceremonie_repartition(joueur)
from utils.input_utils import load_fichier


def installation_salle_commune(joueur):
    info_communes= load_fichier('')
    maison = ceremonie_repartition(joueur)
    print("Vous suivez les préfets à travers les couloirs du château...")
    print(info_communes['maison']['emoji'],info_communes['maison']['description'])
    print(info_communes['maison']['message_installation'])
    print("Les couleurs de votre maison :",end="")
    rses=""
    for val in info_communes['maison']['couleurs'] :
        res=res+val
    print(res[:len(res)-1])

installation_salle_commune(joueur)