def demander_texte(message):
    saisie = input(message)
    while saisie.strip() == "":
        saisie = input(message)
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
