#temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    sec = 0
    sec = temps[0] * 24 * 60 * 60 #nb de secondes correspondant au nombre de jours
    sec += temps[1] * 60 * 60 #nb de secondes correspont au nombre d'heures
    sec += temps[2] * 60 #nb de seconde correspondant au nombre de minutes
    sec += temps[3] #nb de secondes
    return sec

#help(tempsEnSeconde)
#temps = (3,23,1,34)
#print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours = seconde // (24 * 60 * 60)
    seconde %= 24 * 60 * 60
    heures = seconde // (60 * 60)
    seconde %= 60 * 60
    minutes = seconde // 60
    seconde %= 60

    return jours, heures, minutes, seconde

    
#temps = secondeEnTemps(100000)
#print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")
#print(tempsEnSeconde(temps))

"""
def afficheTemps(temps):
    if temps[0] < 1:
        print(end=" ")
    elif temps[0] == 1:
        print(temps[0], "jour", end=" ")
    else:
        print(temps[0], "jours", end=" ")

    if temps[1] < 1:
        print(end=" ")
    elif temps[1] == 1:
        print(temps[1], "heure", end=" ")
    else:
        print(temps[1], "heures", end=" ")

    if temps[2] < 1:
        print(end=" ")
    elif temps[2] == 1:
        print(temps[2], "minute", end=" ")
    else:
        print(temps[2], "minutes", end=" ")
   
    if temps[3] < 1:
        print(end=" ")
    elif temps[3] == 1:
        print(temps[3], "seconde", end=" ")
    else:
        print(temps[3], "secondes")
"""

#méthode par création de fonction:

def affichePluriel(valeur, unite):
    """fonction qui affiche le nombre d'unités (heure, jours...) avec le pluriel ou 0 pris en compte"""
    if valeur > 1:
        print(valeur, unite + "s", end=" ")
    elif valeur == 1:
        print(valeur, unite, end=" ")

def afficheTemps(temps):
     affichePluriel(temps[0], "jour")
     affichePluriel(temps[1], "heure")
     affichePluriel(temps[2], "minute")
     affichePluriel(temps[3], "seconde")
     print()

afficheTemps((1,0,14,23))

def demandeTemps():
    jour = int(input("nombre de jours?"))
    heure = int(input("nombre d'heures?"))
    minute = int(input("nombre de minutes?"))
    seconde = int(input("nombre de secondes?"))
    return jour, heure, minute, seconde
#a terminer en prenant les bornes en compte
temps = demandeTemps()
afficheTemps(demandeTemps())