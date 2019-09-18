# Problème : Déterminer si une année est bissextile ou non. Pour cela, il faut avoir ces règles en tête :
#                   Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
#                   Si elle est multiple de 4, on regarde si elle est multiple de 100.
#                       Si c'est le cas, on regarde si elle est multiple de 400.
#                           Si c'est le cas, l'année est bissextile.
#                           Sinon, elle n'est pas bissextile.
#                       Sinon, elle est bissextile.
#
# Résultat attendu : Un message affichant "Année bissextile" ou "Année non bissextile"

def calcul(annee):
    if (annee % 4) != 0:
        print("Elle n'est pas bissextile")
    else:
        if (annee % 100) != 0:
            if (annee % 400) != 0:
                print("Elle est bissextile")
            else:
                print("Elle n'est pas bissextile")
        else:
            print("Elle n'est pas bissextile")


calcul(2013)
