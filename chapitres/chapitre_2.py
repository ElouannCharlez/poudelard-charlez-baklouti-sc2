from utils.input_utils import demander_choix


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

# from chapitres.chapitre_1 import *
# joueur=creer_personnage()
# rencontrer_amis(joueur)

