# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]

# parcourt tout le tableau avec une boucle
print("Avant modif",B)
for i in range (1, len(B)):                                                             # i      = 3
    nbActu = B[i] # on part de l'indice 1 et pas 0                                      # nbActu = 5
    # boucle a effectuer sur le tableau sur les nombres se trouvant avec nbActu
    cpt = i-1                                                                           # cpt    = 2
    # tant que l'indice est >= 0 et > nbActu
    while (cpt >= 0) & (B[cpt] > nbActu):                                               # (2 >= 0) & (8 > 5)
        B[cpt+1] = B[cpt]   # lorsque c'est > on décale les nombres à droite cpt+1      # B[3] = B[2]
        cpt = cpt - 1                                                                   # cpt    = 1
    B[cpt+1] = nbActu # on place dans l'espace le nombre nbActu

print("Après modif",B)

#print(tri_par_insertion(B))


# 1) se déplacer dans le tableau avec l'indice
# 2) but: effectuer une boucle sur le tableau pour comparer le nombre en question
# 3) au moment où il trouve l'endroit, faudra décaler vers la droite tous ce qui sont plus grand que nbActu..
