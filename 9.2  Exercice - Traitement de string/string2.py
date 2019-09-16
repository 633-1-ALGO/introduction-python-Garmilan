# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

nb = texte.count("exemple")
print("Le nombre d'occurences du mot est", nb)

print(texte.replace("est", "représente"))
