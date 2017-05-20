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

    liste.sort()

    for i in range(0,len(liste)-1):

        if liste[i] != liste[i+1]:

            if abs(liste[i]-liste[i+1]) <= 10:
                return True

    return False

# Testen unseres Algorithmus
print("##### Aufgabe 24a #####")
print("Liste, die die Bedingung erfüllt: L1 = [1,2,5,17,25,39,57]")
print("L1 erfüllt die Bedingung: ",diffNumbersLE10([1,2,5,17,25,39,57]))
print("Liste, die die Bedingung nicht erfüllt: L2 = [25,67,200]")
print("L2 erfüllt die Bedingung: ",diffNumbersLE10([25,67,200]))

######################################################################################################################
#                                           Aufgabe 24b: Nullsumme                                                   #
######################################################################################################################
