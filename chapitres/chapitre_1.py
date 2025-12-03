def introduction():
    print("Bienvenue ! Prépare-toi : le premier chapitre de ton voyage vers Poudlard commence maintenant.")
    input()

def creer_personnage():
    nom = input("Entrez le nom de votre personnage : ")
    prenom = input("Entrez le prénom de votre personnage : ")
    print("Choisissez vos attributs : ")
    courage=0
    while not (1<=courage<=10):
        courage = int(input("Niveau de courage (1-10) : "))
    intel=0
    while not (1<=intel<=10):
        intel = int(input("Niveau d’intelligence (1-10) : "))
    loyauté=0
    while not (1<=loyauté<=10):
        loyauté = int(input("Niveau de loyauté (1-10) : "))
    ambition=0
    while not (1<=ambition<=10):
        ambition = int(input("Niveau d'ambition (1-10) : "))
    attributs={"courage":courage,"intelligence":intel,"loyauté":loyauté,"ambition":ambition}
    perso=initialiser_personnage(nom, prenom, attributs)
    print("Profil du personnage : ")
    print("Nom :",nom)
    print("Prenom :",prenom)
    print("Argent : 100")
    print("Inventaire : ")
    print("Sortilèges : ")
    print("Attributs : ")
    for a,b in attributs.items():
        print("- {} : {}".format(a,b))
    return perso
#a=creer_personnage()