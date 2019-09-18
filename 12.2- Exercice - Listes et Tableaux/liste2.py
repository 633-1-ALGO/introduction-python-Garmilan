# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]


def valeur_max(*liste):
    max = 0
    n = 0
    for sousTab in liste:
        m = 0
        for sousNb in sousTab:
            if sousNb > max:
                max = sousNb
                res = [max, n, m]
            m = m +1
        n = n +1
    print("La valeur maximum est :", res[0], "et elle se trouve à l'indice [", res[1], "][", res[2], "]")



valeur_max(*tab)
