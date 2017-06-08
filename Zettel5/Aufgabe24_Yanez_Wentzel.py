# Zettel 5, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 24

######################################################################################################################
#                                           Aufgabe 24a: Nachbarn                                                    #
######################################################################################################################
def diffNumbersLE10(liste):
    '''Prüfen, ob der Betrag der Differenz zwei verschiedener Elemente der Liste kleiner gleich 10 ist'''

    # Abfangen von einer leeren Liste und einer Liste mit nur einem Element
    if len(liste) < 2:
        return False

    try:
        liste.sort()
    except TypeError:
        print("ERROR: Die Liste enthält nichtnumerische Elemente!")

    for i in range(0,len(liste)-1):

        if liste[i] != liste[i+1]:

            if abs(liste[i]-liste[i+1]) <= 10:
                return True

    return False

# Testen unseres Algorithmus
print("##### Aufgabe 24a #####")
print("Liste, die die Bedingung erfüllt: L1 = [1,2,5,17,25,39,57]")
print("L1 erfüllt die Bedingung: ",diffNumbersLE10([1,2,5,17,25,39,57]))
print()
print("Liste, die die Bedingung nicht erfüllt: L2 = [25,67,200]")
print("L2 erfüllt die Bedingung: ",diffNumbersLE10([25,67,200]))

######################################################################################################################
#                                           Aufgabe 24b: Nullsumme                                                   #
######################################################################################################################
def Nullsumme(liste1,liste2,liste3):
    '''Prüfen, ob es Kombinationen aus den drei gegebenen Listen gibt, die die Nullsumme ergeben'''
    if len(liste1) == 0 and len(liste2) == 0 and len(liste3) == 0:
        return False

    try:
        liste1.sort()
        liste2.sort()
        liste3.sort()
    except TypeError:
        print("ERROR: Eine oder mehrere Listen enthalten nichtnumerische Elemente!")

    for indexliste1 in range(0,len(liste1)):
        indexliste2=0
        indexliste3=(len(liste3))-1

        while indexliste2 < len(liste2) and indexliste3 >= 0:
            summe = liste1[indexliste1]+liste2[indexliste2]+liste3[indexliste3]

            if summe < 0:
                indexliste2 += 1
            elif summe > 0:
                indexliste3 -= 1
            else:
                return True

    return False

# Testen des Algorithmus
print()
print("##### Aufgabe 24b #####")
print("Listen, die Nullsummen enthalten: L1 = [1,2,5], L2=[2,5,3], L3=[-7,8,3]")
print("L1, L2 und L3 enthalten mindestens eine Nullsumme: ",Nullsumme([1,2,-5],[2,5,3],[-7,8,3]))
print()
print("Listen, die keine Nullsummen enthalten: L1 = [25,67,200], L2=[3,2,1], L3=[1,1]")
print("L1, L2 und L3 enthalten mindestens eine Nullsumme: ",Nullsumme([25,67,200],[3,2,1],[1,1]))

# Die Lösung der Aufgabe orientiert sich sehr stark an einem Programmiervorschlag von stackoverflow
# https://stackoverflow.com/questions/11575866/find-all-combinations-of-records-which-sums-to-zero-in-three-array-lists
