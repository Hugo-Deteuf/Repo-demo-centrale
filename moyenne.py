"""Ce module fournit une fonction pour calculer une moyenne de valeurs"""

# NB: Ce fichier contient du code à compléter


def moyenne(valeurs):
    sum = 0
    if valeurs == []:
        raise ValueError
    else:
        for i in valeurs:
            sum = sum + i
        return sum / len(valeurs)


print("moyenne([10, 20, 15]) :", end=" ")
print(moyenne([10, 20, 15]))
