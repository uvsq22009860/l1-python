#temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    sec = 0
    sec += temps[0] * 24 * 60 * 60
    sec += temps[1] * 60 * 60
    sec += temps[2] * 60
    sec += temps[3]
    return sec

temps = (3,23,1,34)
#print(type(temps))
#print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour = seconde // (24 * 60 * 60)
    seconde %= (24 * 60 * 60)
    heure = seconde // (60 * 60)
    seconde %= (60 * 60)
    minute = seconde // 60
    seconde %= 60
    return jour, heure, minute, seconde
temps = secondeEnTemps(342094)
#print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

def afficheplur(valeur, unite):
    """Fonction qui affiche le nombre d'unités (heure, jours...) avec le pluriel ou 0 prit en compte"""
    if valeur > 1:
        print(valeur, unite + "s", end=" ")
    elif valeur == 1:
            print(valeur, unite, end=" ")

def afficheTemps(temps):
    afficheplur(temps[0], "jour")
    afficheplur(temps[1], "heure")
    afficheplur(temps[2], "minute")
    afficheplur(temps[3], "seconde")
    print()

#affichetemps((2 ,0, 1, 23))

def verifieTemps(temps):
    """
    Vérifie que le temps entré par l'utilisateur est correct.
    """

    _, heures, minutes, secondes = temps

    if(heures >= 24) or (minutes >= 60) or (secondes >= 60):
        return False
    else:
        return True

def demandeTemps():

    jour, heure, minute, seconde = 0, 0, 0, 9999

    while not verifieTemps((jour, heure, minute, seconde)):
        jour = int(input("Nombre de jours"))
        heure = int(input("Nombre d'heures"))
        minute = int(input("Nombre de minutes"))
        seconde = int(input("Nombre de de secondes"))
        sec = (jour * 24 * 60 * 60) + (heure * 60 * 60) + (minute * 60) + seconde
    print(sec)
    return jour, heure, minute, seconde, sec

#temps = demandeTemps()
#afficheTemps(temps)

def sommeTemps(temps1, temps2):
    secondes = tempsEnSeconde(temps1) + tempsEnSeconde(temps2)
    return secondeEnTemps(secondes)

#print(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)))

def proportionTemps(temps,proportion):
    secondes = tempsEnSeconde(temps) * proportion
    return secondeEnTemps(secondes)

#afficheTemps(proportionTemps((2,0,36,0),0.2))

def bissextile(année):
    if (année % 400 == 0):
        return True
    elif (année % 4 == 0) and (année % 100 == 0):
        return False
    elif (année % 4 == 0):
        return True
    else:
        return False

def tempsEnDate(temps):

    print(temps)
    jour, heure, minute, seconde = temps

    année = jour // 365
    jour %= 365
    
    moisAnnée = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if bissextile(année + 1970):
        moisAnnée[1] = 29
    
    mois = 0
    while jour >= moisAnnée[mois]:
        jour -= moisAnnée[mois]
        mois += 1
    mois += 1

    #print(année, "ans", mois, "mois", jour, "jours", heure, "heures", minute, "minutes", seconde, "secondes")

    return (année, jour, heure, minute, seconde)

def afficheDate(date = -1):
    afficheplur(date[0], "année")
    print(date[1], "mois", end=" ")
    afficheTemps((date[2], date[3], date[4], date[5]))
    
temps = secondeEnTemps(1000000000)
date = tempsEnDate(temps)
afficheTemps(temps)
afficheDate(date)

###Calcul année bissextile
années = 100000 // 365

année_bissextile = []
for année in range(2020, 2020 + années + 1):
    if bissextile(année):
        année_bissextile.append(année)

print(années_bissextile)