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
    while not (1 <= courage <= 10):
        courage = int(input("Niveau de courage (1-10) : "))
    intel = 0
    while not (1 <= intel <= 10):
        intel = int(input("Niveau d’intelligence (1-10) : "))
    loyaute=0
    while not (1 <= loyaute <= 10):
        loyaute = int(input("Niveau de loyauté (1-10) : "))
    ambition = 0
    while not (1 <= ambition <= 10):
        ambition = int(input("Niveau d'ambition (1-10) : "))
    print()
    attributs = {"courage":courage,"intelligence":intel,"loyauté":loyaute,"ambition":ambition}
    joueur = initialiser_personnage(nom,prenom,attributs)
    afficher_personnage(joueur)
    return joueur

# creer_personnage()

from utils.input_utils import demander_choix
def recevoir_lettre():
    print("Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...")
    print("« Cher élève,")
    print("Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »")
    choix=demander_choix("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?",["Oui, bien sûr !", "Non, je préfère rester avec l’oncle Vernon..."])
    if choix=="Oui, bien sûr !":
        return 1 # pour dire que ça continue
    print("\nVous déchirez la lettre, l’oncle Vernon pousse un cri de joie:")
    print("« EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! »")
    print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
    return 0 # pour dire qu'il a refusé

# recevoir_lettre()

def rencontrer_hagrid(personnage):
    print("Hagrid : 'Salut ", personnage["Prenom"]," ! Je suis venu t’aider à faire tes achats surle Chemin de Traverse.'")
    choix = demander_choix("Voulez-vous suivre Hagrid ?", ["Oui", "Non"])
    if choix == "Non":
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui!")
    return None

perso = {'Nom': 'Baklouti', 'Prenom': 'Youssef', 'Argent': 100, 'Inventaire': [], 'Sortilèges': [], 'Attributs': {'courage : 8'}}
rencontrer_hagrid(perso)