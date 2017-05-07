# Elena Schmidt Yanez, Bianca Wentzel
# 3. Aufgabenzettel, Informatik B
# Aufgabe 15

######################################################################################################################
#                                   Aufgabe 15a) Verfolgen der Schildkröte                                           #
######################################################################################################################
from turtle import *

# Definieren einer Verfolgerklasse (Unterklasse der Klasse turtle)
class Verfolger(Turtle):
    def __init__(self,ziel):
        super().__init__()  # Aufrufen des init-Konstruktors der Klasse turtle
        self.zielschildkroete=ziel  # Instanzvariable der Verfolgerinstanz

    def verfolge(self,schrittweite):
        # Verändern der Blickrichtung unserer Verfolgerinstanz und Bewegen in die vorgegebene Richtung
        self.setheading(self.towards(self.zielschildkroete.position()))
        self.forward(schrittweite)

# Ausprobieren der Klasse Verfolger
print("##### Aufgabe 15a #####")
print("Erzeugen einer Zielschildkröte Shredder")
shredder=Turtle()
shredder.up()
shredder.setposition(100,200)
print("Position der Zielschildkröte Shredder:",shredder.position())
print()

print("Verfolgen von Shredder mit der Schrittweite 100")
teenageMutantNinjaTurtle=Verfolger(shredder)
print("Anfängliche Position der TMNT:",teenageMutantNinjaTurtle.position())
teenageMutantNinjaTurtle.verfolge(100)
print("Neue Position der TMNT:",teenageMutantNinjaTurtle.position())
print()
######################################################################################################################
#                                           Aufgabe 15b) Rechteck zeichnen                                           #
######################################################################################################################
class Rechteck():
    def __init__(self,links,rechts,unten,oben):
        self.xkoordinaten=(links,rechts)
        self.ykoordinaten=(unten,oben)

    def zeichne(self):
        rechteckturtle=Turtle()
        rechteckturtle.color("red")
        # Position einer neuen Turtelinstanz ist (0,0)
        rechteckturtle.up() # Anheben des Stiftes, damit nicht gezeichnet wird
        rechteckturtle.setposition(self.xkoordinaten[0],self.ykoordinaten[0])
        rechteckturtle.down() # Absenken des Stiftes zum Zeichnen

        rechteckturtle.goto(self.xkoordinaten[1],self.ykoordinaten[0])
        rechteckturtle.setheading(90) # Drehen des Pfeiles nach oben

        rechteckturtle.goto(self.xkoordinaten[1],self.ykoordinaten[1])
        rechteckturtle.setheading(180)  # Drehen des Pfeils nach links

        rechteckturtle.goto(self.xkoordinaten[0],self.ykoordinaten[1])
        rechteckturtle.setheading(270)  # Drehen des Pfeils nach unten
        rechteckturtle.goto(self.xkoordinaten[0],self.ykoordinaten[0])

# Ausprobieren der Klasse Rechteck
print("Zeichnen eines Rechtecks mit den Koordinaten: (links:-200, rechts:300, unten:0, oben:200)")
neuesRechteck=Rechteck(-200,300,0,200)
neuesRechteck.zeichne()
done()

######################################################################################################################
#                                       Aufgabe 15c) Begrenzte Schildkrötenjagd                                      #
######################################################################################################################
class Wegläufer(Turtle):
    def __init__(self,wovor,Begrenzung=None):
        self.fluchtgrund=wovor
        self.grenzen=Begrenzung
        super().__init__()

    def laufweg(self, distanz=30):
        richtung = self.towards(self.flurchtgrund)
        self.setheading(richtung+180)
        self.forward(distanz)
