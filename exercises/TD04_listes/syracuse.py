def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    listeN = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
            listeN.append(n)
        else:
            n= n * 3 + 1
            listeN.append(n)
    return listeN

print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    

print(testeConjecture(10000))