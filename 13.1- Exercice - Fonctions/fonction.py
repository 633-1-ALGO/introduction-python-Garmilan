# Problème : Créer une fonction affichant la fréquence des lettres d'une chaine de caractère.
# Données : Un texte d'essai et un tableau de caractère et leur fréquences.
texte = "ceci est un texte que vous pouvez modifier mais gare aux caracteres speciaux et aux majuscules"
tab_lettres = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', ' '], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



def calcul_frequence(txt, tab):
    alphabets = tab[0]
    chiffres = tab[1]
    cpt = 0
    for a in alphabets:
        nbFois = 0
        for l in txt:
            if a == l:
                nbFois = nbFois +1
                chiffres[cpt] = nbFois
        cpt = cpt +1
    tab = [alphabets, chiffres]
    print("La fréquence des lettres est\n", alphabets, "\n", chiffres)


calcul_frequence(texte, tab_lettres)

