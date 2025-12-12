import json


def demander_texte(message):
    print(message)
    saisie = input()
    while saisie.strip() == "":
        print(message)
        saisie = input()
    print()
    return saisie.strip()

# if __name__ == "__main__":
#     print(demander_texte("saisie un nom : "))

def demander_nombre(message, min_val=None, max_val=None):
    tab_chiffre = ["0","1","2","3","4","5","6","7","8","9"]
    redemande = True    # on l'utilise pour savoir si ce qu'à entrer le joueur est conforme et sans renvoyer d'erreur s'il est entré des lettres
    while redemande or ((min_val!=None and min_val>int(val)) or (max_val!=None and max_val<int(val))):
        redemande = False
        val = input(message)
        if val=="":
            redemande = True
        for carac in val:
            if carac not in tab_chiffre:
                redemande = True
    return int(val)

# if __name__ == "__main__":
#     print(demander_nombre("nb entre 1-9 : ",1,9))

def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print(str(i+1)+". ",options[i])
    choix=demander_nombre("Votre choix : ",1,len(options))
    return choix-1

# if __name__ == "__main__":
#     print(demander_choix("Voulez-vous continuer ?",['oui','non']))


def load_fichier(chemin_fichier):
    with open(chemin_fichier[1:], 'r', encoding='utf-8') as f:   # enlever le slice si on souhaite tester hors du menu
        donnees = json.load(f)
    return donnees

# if __name__ == "__main__":
#     print(load_fichier("../data/sorts.json"))