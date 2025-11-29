def demander_texte(message):
    saisie = input(message)
    while saisie.strip() == "":
        saisie = input(message)
    return saisie.strip()
#print(demander_texte("saisie un nom : "))
#test avec " abcd " renvoie abcd
