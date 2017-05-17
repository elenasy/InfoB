# Zettel 4, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 20

######################################################################################################################
#                               Aufgabe 20: Regressives Programmieren der Kochkurve                                  #
######################################################################################################################
from turtle import *

# Rekursive Funktion zum Zecihen der Kochkurve
def Kochkurve(t,k,Schrittweite):
    '''Konstruktion der Kochkurve der k-ten Iteration mit einer variablen Schrittweite
    t ist hierbei eine Instanz der Klasse Turtle'''
    if k==0:
        return
    if k==1:
        t.forward(Schrittweite)
    else:
        Kochkurve(t, k - 1, Schrittweite)
        t.forward(Schrittweite)
        t.left(60)

        Kochkurve(t, k - 1, Schrittweite)
        t.forward(Schrittweite)
        t.right(120)

        Kochkurve(t, k - 1, Schrittweite)
        t.forward(Schrittweite)
        t.left(60)
        Kochkurve(t,k-1,Schrittweite)

#Ausprobieren
turtle=Turtle()
turtle.up()
turtle.setposition(-380,0)
turtle.down()
Kochkurve(turtle,4,10)
done()
