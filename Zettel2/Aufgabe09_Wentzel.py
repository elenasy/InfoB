# Bianca Wentzel
# Übungszettel 2, Informatik B
# Aufgabe 9

###########################################################################################################
#                         Aufgabe 9a) Berechnung des Skalarproduktes zweier Listen                        #
###########################################################################################################
# Definieren einer Funktion zum Prüfen eines Elements auf seinen Type (gültig: int, float)
def istElementZahl(elem):
    return (type(elem) is float) or (type(elem) is int)

# Definieren einer Funktion zur Berechnung des Skalarproduktes aus zwei Listen
def Skalarprodukt(l1,l2):
    '''Berechnugn des Skalarproduktes aus den übergebenen Listen l1 und l2'''
    # Überprüfen der Gleichheit der Dimensionen der Listen
    if len(l1) != len(l2):
        raise IndexError("Die Dimensionen der Listen müssen übereinstimmen!")

    # Überprüfen, ob ungültige Elemente in den Listen enthalten sind
    # Die getrennte Überprüfung, ob leere Listen übergeben wurden, kann weggelassen werden, da die Länge
    # einer leeren Liste 0 ist und so von 0 bis 0 iteriert wird.
    #l1 und l2 haben dieselbe Dimension
    ergebnis=0
    for x in range(len(l1)):
        if istElementZahl(l1[x]) and istElementZahl(l2[x]):
            # Berechnung des Skalarproduktes
            ergebnis += l1[x] * l2[x]

        else:
            raise ValueError("Ungültiger Wert enthalten!")

    return ergebnis

# Ausprobieren der Funktion Skalarprodukt
print("Berechnen des Skalarprodukts von [1,2,5],[2,3,-1]:")
print(Skalarprodukt([1,2,5],[2,3,-1]))

print("Berechnen des Skalarprodukts von [],[]:")
print(Skalarprodukt([],[]))

# Die anderen zwei Fälle werden hier nicht getestet, weil sonst das Programm abbricht und die weiteren
# Aufgaben nicht berabeitet werden.

##########################################################################################################
#                   Aufgabe 9b) Erstellen eines Histogramms einer Zeichenkette                           #
##########################################################################################################
# Definieren einer Funktion, die ein Histogramm einer Zeichenkette erstellt
def Histogramm(zeichenkette):
    '''Aus der gegebenen Zeichenkette wird ein Histogramm erstellt, welches die Auftrittshäufigkeiten
    der einzelnen Elemente der Zeichenkette beinhaltet'''
    # Überprüfen des Types der übergebenen Variable
    if type(zeichenkette) is str:
        woerterbuch={}
        for x in zeichenkette:
            if x in woerterbuch:
                woerterbuch[x]+=1
            else:
                woerterbuch[x]=1
    else:
        raise TypeError("Es muss eine Zeichenkette übergeben werden!")

    return woerterbuch

# Ausprobieren der Funktion Histogramm
print("Erstellen des Histogramms von 'Hanna':")
print(Histogramm('Hanna'))

##########################################################################################################
#                               Aufgabe 9c) Verketten von Listen                                         #
##########################################################################################################
# Definieren einer Funktion zum Verketten von Listen
def Verketten(schachtelliste):
    ergebnisliste=[]
    # Überprüfen, ob eine Liste übergeben wird
    if type(schachtelliste) is not list:
        raise TypeError("Es muss eine Liste übergeben werden!")

    # Überprüfen, ob Listen in der Liste enthalten sind
    for x in schachtelliste:
        if type(x) is not list:
            raise TypeError("Es müssen Listen in der Liste enthalten sein!")

        # Verketten der Listen
        ergebnisliste+=x

    return ergebnisliste

# Ausprobieren der Funktion Verketten
print("Verketten von [[1,2],[2,[1,4]],[True]]:")
print(Verketten([[1,2],[2,[1,4]],[True]]))