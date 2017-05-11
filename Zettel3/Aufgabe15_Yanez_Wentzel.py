# Elena Schmidt Yanez, Bianca Wentzel
# 3. Aufgabenzettel, Informatik B
# Aufgabe 15

######################################################################################################################
#                                   Aufgabe 15a) Verfolgen der Schildkröte                                           #
######################################################################################################################
from turtle import *

#Definieren einer Verfolgerklasse (Unterklasse der Klasse turtle)
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
# Definieren einer Klasse Rechteck mit der Methode zeichnen
class Rechteck():
    def __init__(self,links,rechts,unten,oben):
        self.xkoordinaten=(links,rechts)
        self.ykoordinaten=(unten,oben)

    # Zeichnen eine Vierecks mit den vorgegebenen Grenzen in x- und y-Richtung
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

#Ausprobieren der Klasse Rechteck
print("##### Aufgabe 15b #####")
print("Zeichnen eines Rechtecks mit den Koordinaten: (links:-200, rechts:300, unten:0, oben:200)")
neuesRechteck=Rechteck(-200,300,0,200)
neuesRechteck.zeichne()
print()
######################################################################################################################
#                                       Aufgabe 15c) Begrenzte Schildkrötenjagd                                      #
######################################################################################################################
from math import *

# Klasse zum Wegrennen innerhalb der optionalen Begrenzung
class Wegläufer(Turtle):
    def __init__(self,wovor,Begrenzung=None):
        super().__init__()
        self.fluchtgrund=wovor
        self.grenzen=Begrenzung

    # Zeichnen der optionalen Begrenzung
    def zeichneBegrenzung(self):
        grenzen=Rechteck(self.grenzen[0],self.grenzen[1],self.grenzen[2],self.grenzen[3])
        grenzen.zeichne()

    def berechneNeuePosition(self,fliehwinkel,schrittweite):
        # Umrechnung des Fliehwinkels in Radiant
        fliehwinkelRad = fliehwinkel * (pi / 180)

        # Berechnung der Länge der Ankathete(x) und Gegenkathete(y)
        ankathete = schrittweite * cos(fliehwinkelRad)
        gegenkathete = schrittweite * sin(fliehwinkelRad)

        # Berechnung der neuen Position der verfolgten Turtle durch Addition der berechneten Längen der
        # Ankathete und der Gegenkathete
        neuePosition = self.position() + (ankathete,gegenkathete)
        return neuePosition

    def istPositionAusserhalbGrenze(self, Position):
        if (Position[0] < self.grenzen[0] or Position[0] > self.grenzen[1]) or \
                (Position[1] < self.grenzen[2] or Position[1] > self.grenzen[3]):
            return True
        else:
            return False

    def berechneFunktionsgleichung(self,aktuellePosition,zukuenftigePosition):
        # Anhand des aktuellen und des zukünftigen Punktes werden die Komponenten einer Funktionsgleichung berechnet
        # Funktion mit y = mx + n, mit m= Steigung und n= aboslutes Glied
        # Berechnung der Steigung: (y1-y2)/(x1-x2)
        steigung=(aktuellePosition[1]-zukuenftigePosition[1])/(aktuellePosition[0]-zukuenftigePosition[0])

        # Berechnung des absoluten Glieds durch Einsetzen eines Punktes in die Funktionsgleichung und umstellen nach n
        absolutesGlied=aktuellePosition[1]-(steigung*aktuellePosition[0])

        return (steigung,absolutesGlied)

    def berechneSchnittpunktMitGrenze(self, funktionsGraph, grenzWert, gesuchteAchse):
        # Es gibt zwei mögliche Schnittereignisse: Schneiden mit den Seitenbegrenzungen links oder rechts
        # oder Schneiden mit der Ober- oder Unterbegrenzung
        # Berechnung durch Umstellen der Funktionsgleichung zur gewünschten Koordinate (y=mx+n)
        if gesuchteAchse == "x":
            # x = ( y - n ) / m
            x=(grenzWert-funktionsGraph[1])/funktionsGraph[0]
            return (x,grenzWert)
        else:
            # y = mx + n
            y=(funktionsGraph[0]*grenzWert)+funktionsGraph[1]
            return (grenzWert,y)

    def berechneDistanzZumSchnittpunkt(self, aktuellePosition, schnittpunkt):
        # Anhand des Satzes von Pythagoras wird der Abstand zwischen dem aktuellen Standpunkt und dem
        # Schnittpunkt mit der begrenzung berechnet
        x=schnittpunkt[0]-aktuellePosition[0]
        y=schnittpunkt[1]-aktuellePosition[1]
        distanz=sqrt((x**2)+(y**2))
        return distanz

    def laufweg(self, schrittweite=30):
        # Wenn eine Begrenzung existiert, dann soll diese eingezeichnet werden
        if self.grenzen:
            # Die verfolte Turtle startet standardmäßig an der Position (0,0), deshalb muss getestet
            # werden, ob die angegebene Begrenzung die Turtle überhaupt beinhaltet
            if self.istPositionAusserhalbGrenze(self.position()):
                raise ValueError("Du befindest dich außerhalb der Begrenzung, bitte ändere die Begrenzung!")
            else:
                self.zeichneBegrenzung()

        # Verfolgte Turtle richtet sich entgegengesetzt zu ihrem Verfolger aus, jedoch ohne, dass der Fliehwinkel die
        # mathematisch vorgegebenen Winkelgrößen überschreitet (also zwischen 0 und 360)
        richtung = self.towards(self.fluchtgrund.position())
        fliehwinkel=0
        if richtung > 180 and richtung <= 360:
            fliehwinkel = richtung -180
        elif richtung < 180 and richtung >=0:
            fliehwinkel = richtung +180

        self.setheading(fliehwinkel)

        if self.grenzen:
            restdistanz = schrittweite

            while restdistanz>0:
                # Die Methode berechneSchnittpunkt benötigt eine Angabe, welche der Begrenzungen geschnitten wird
                # Hierzu wurde der Winkel zwischen der aktuellen Position und den 4 Ecken des Rechtecks berechnet
                # und dieses dann in 4 Quadranten aufgeteilt. Je nach Fliehwinkel liegt der Schnittpunkt in einem der
                # 4 Quadranten und dementsprechend kann die jeweilige Grenze übergeben werden.
                # 1. Quadrant: Winkel zwischen der oberen rechten und der oberen linken Ecke
                # -> Schnitt der oberen Begrenzung
                # 2. Quadrant: Winkel zwischen der oberen linken und der unteren linken Ecke
                # -> Schnitt der linken Begrenzung
                # 3. Quadrant: Winkel zwischen der unteren linken und der unteren rechten Ecke
                # -> Schnitt der unteren Begrenzung
                # 4. Quadrant: Winkel zwischen der unteren rechten Ecke und der oberen rechten Ecke
                # -> Schnitt mit der unteren Begrenzung
                # !! Achtung: Geraden, die genau durch die Ecken verlaufen, werde hier nicht berücksichtigt!!
                winkelobenrechts = self.towards((self.grenzen[1], self.grenzen[3]))
                winkelobenlinks = self.towards((self.grenzen[0], self.grenzen[3]))
                winkeluntenrechts = self.towards((self.grenzen[1], self.grenzen[2]))
                winkeluntenlinks = self.towards((self.grenzen[0], self.grenzen[2]))

                # Bevor die Turtle wegrennt, muss getestet werden, ob sie sich danach noch innerhalb der Begrenzung
                #  befindet. Hierzu wird anhand der Schrittweite und des momentanen Wegrennwinkels die nächste
                # Position berechnet
                zukuenftigePosition = self.berechneNeuePosition(fliehwinkel, restdistanz)

                # Anhand der nächsten Position wird, wenn diese sich außerhalb der Begrenzung befindet,
                # eine Funktionsgleichung berechnet, die die Gerade zwischen der aktuellen Position und der
                # zukünftigen parametrieseirt.
                if self.istPositionAusserhalbGrenze(zukuenftigePosition):
                    funktionsgleichung = self.berechneFunktionsgleichung(self.position(), zukuenftigePosition)
                    schnittpunkt=()
                    if (fliehwinkel > -1 and fliehwinkel < winkelobenrechts) or \
                            (fliehwinkel > winkeluntenrechts and fliehwinkel <= 360):
                        schnittpunkt = self.berechneSchnittpunktMitGrenze(funktionsgleichung, self.grenzen[1], "y")

                    elif fliehwinkel > winkelobenrechts and fliehwinkel < winkelobenlinks:
                        schnittpunkt = self.berechneSchnittpunktMitGrenze(funktionsgleichung, self.grenzen[3], "x")

                    elif fliehwinkel > winkelobenlinks and fliehwinkel < winkeluntenlinks:
                        schnittpunkt = self.berechneSchnittpunktMitGrenze(funktionsgleichung, self.grenzen[0], "y")

                    elif fliehwinkel > winkeluntenlinks and fliehwinkel < winkeluntenrechts:
                        schnittpunkt = self.berechneSchnittpunktMitGrenze(funktionsgleichung, self.grenzen[2], "x")

                    # Daraufhin wird der Schnittpunkt dieser Gerade mit der in Fliehrichtung liegenden Begrenzung und
                    # daraus der Abstand zwischen aktueller Position und Begrenzung berechnet. Dieser Abstand wird
                    # nun überbrückt und der verbleibende Teil der vorgegebenen Schrittweite wird in eine andere
                    # Richtung fortgesetzt (parallel zur Grenze) -> Funktioniert leider nicht wie gedacht
                    schnittpunktdistanz = self.berechneDistanzZumSchnittpunkt(self.position(), schnittpunkt)


                    if schnittpunktdistanz > 10:
                        self.forward(schnittpunktdistanz - 10)
                        einfallswinkel=abs(fliehwinkel-180)
                        reflektionswinkel=abs(180-(2*einfallswinkel))

                        if einfallswinkel <90:
                            self.left(einfallswinkel)
                            fliehwinkel=fliehwinkel+2*einfallswinkel
                        else:
                            self.left(reflektionswinkel)

                    else:
                        if einfallswinkel <90:
                            self.left(einfallswinkel)
                            fliehwinkel=fliehwinkel+2*einfallswinkel
                        else:
                            self.left(reflektionswinkel)

                        self.forward(schnittpunktdistanz)

                    restdistanz = restdistanz - (schnittpunktdistanz - 10)

                else:
                    self.forward(restdistanz)
                    restdistanz=0
        else:
            self.forward(schrittweite)

# Ausprobieren
print("##### Aufgabe 15c #####")
print("Instanziieren einer Ninja-Turtle in grüner Farbe")
Ninja=Turtle()
Ninja.color("green")
print("Setzen der Position der Ninja-Turtle auf (-60,40)")
Ninja.setposition(-60,40)
print("Instanziieren einer Wegläuferturtle mit der Begrenzung (-400, 300, -250, 200)")
Shredder=Wegläufer(Ninja,(-400,300,-250,200))
print("Auf die Plätze, fertig, LOS!")
Shredder.laufweg(400)
done()
print("##### ENDE #####")
