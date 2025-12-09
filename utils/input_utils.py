import json


def demander_texte(message):
    print(message)
    saisie = input()
    while saisie.strip() == "":
        print(message)
        saisie = input()
    print()
    return saisie.strip()

#print(demander_texte("saisie un nom : "))
#test avec " abcd " renvoie abcd

def demander_nombre(message, min_val=None, max_val=None):
    val=int(input(message))
    while (min_val!=None and min_val>val) or (max_val!=None and max_val<val):
        val = int(input(message))
    return val

# print(demander_nombre("nb entre 1-9 : ",1,9))
# entrée(0) : sortie(redemande); entrée(1) : sortie(renvoie 1)

def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print(str(i+1)+". ",options[i])
    choix=demander_nombre("Votre choix : ",1,len(options))
    return choix-1

#print(demander_choix("Voulez-vous continuer ?",['oui','non']))
#entrée(78) sortie(redemande); entrée(1) : sortie(oui)


def load_fichier(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        donnees = json.load(f)
    return donnees
