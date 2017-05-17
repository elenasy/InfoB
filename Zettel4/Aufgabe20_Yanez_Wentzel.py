# Zettel 4, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 20

######################################################################################################################
#                               Aufgabe 20a: Regressives Programmieren der Kochkurve                                 #
######################################################################################################################
from turtle import *

# Rekursive Funktion zum Zecihen der Kochkurve
def Kochkurve(t,k,Schrittweite):
    '''Konstruktion der Kochkurve der k-ten Iteration mit einer variablen Schrittweite,
    t ist hierbei eine Instanz der Klasse Turtle'''
    if k==0:        # Eiegentlich nicht existent
        return

    if k==1:
        t.forward(Schrittweite)
        return

    else:

        Kochkurve(t, k - 1, Schrittweite/3)
        t.left(60)

        Kochkurve(t, k - 1, Schrittweite/3)
        t.right(120)

        Kochkurve(t, k - 1, Schrittweite/3)
        t.left(60)

        Kochkurve(t,k-1,Schrittweite/3)

#Ausprobieren
print("##### Aufgabe 20a #####")
print("Zeichnen der Kochkurve der 5. Ordnund.")
print("Entschuldigung, wenn das zu lange dauert, aber es sieht viel schöner aus :)")
turtle=Turtle()
turtle.up()
turtle.setposition(-380,0)
turtle.down()
Kochkurve(turtle,4,310)
done()

######################################################################################################################
#                                    Aufgabe 20b: Länge und Abstand der Kochkurve                                    #
######################################################################################################################
# Der Abstand zwischen Anfangspunkt und Endpunkt der Kochkurve beträgt, egal bei welchem Iterationsschritt,
# genau Schrittweite. Die sliegt daran, dass bei jedem höheren Iterationsschritt, die Schrittweite gedrittelt wird.

# Die Länge der Kochkurve beträgt (4/3)^k, wobei k der Ordnung entspricht und die erste Ordnung per Definition der
# Schrittweite enstpricht. Die Länge der Kurve strebt für k -> unendlich gegen unendlich.