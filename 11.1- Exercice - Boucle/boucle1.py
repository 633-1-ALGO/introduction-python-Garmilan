# Problème : Etant donné un tableau A de "n" nombres réels, on demande la moyenne des nombres du tableau
# Données : un tableau A de n nombre réels
# Résultat attendu : Moyenne des nombres réels du tableau A
A = [1, 5, 15, 25, 10, 55, 50, 35]


cpt = 0
nb = 0
moy = 0

for i in A:
   nb = nb + i
   cpt = cpt + 1

moy = nb / cpt
print("La moyenne est", moy)



