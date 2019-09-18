# Problème : Réaliser une table de multiplication de taile 10x10 en utilisant la liste fournie.
# Résultat attendu : un affichage comme ceci :   1  2  3  4  5  6  7  8  9  10
#                                             1  1  2  3  4  5  6  7  8  9  10
#                                             2  2  4  6  8  10 12 14 16 18 20
#                                             3  3  6  9  12 15 18 21 24 27 30
# Indication :   L'alignement rectiligne n'est pas une contrainte, tant que la table est visible ligne par ligne c'est ok.
#               Si vous êtes perfectionnistes faites vous plaisir.
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def multiplication(*tab):
    tabA = []
    tabA.insert(0, "")
    for ind in range (1, len(tab)+1):
        tabA.insert(ind, ind)
    print(*tabA)

    for i in range (1, len(tab)+1):
        tabB = []
        tabB.insert(i, i)
        for cpt in range (1, len(tab)+1):
            nb = i * cpt
            tabB.insert(cpt, nb)
        print(*tabB)


multiplication(*liste)
