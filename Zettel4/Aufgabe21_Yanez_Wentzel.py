# Zettel 4, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 21

######################################################################################################################
#                                           Aufgabe 21) Definitionen                                                 #
######################################################################################################################
#(a) Objekt (Exemplar) einer Klasse
# Objekte sind in einer Entität eingekapselte Variablen und Funktionen.
# Objekte sind eine konkrete Ausrägung einer Klasse und erhalten dessen Variablen und Funktionen.

# Definition einer Klasse:
class Saeugetier:
    def __init__(self):
        self.beine=4
        self.ohren=2

    def hoere(self):
        print("Ich höre mit ",self.ohren," Ohren.")

# Kreation einer Instanz des Objekts Sauugetier
affe=Saeugetier()

# Aufruf einer Variable des Objektes
print(affe.ohren)

#######################

# (b) Vererbung
# Vererbung bedeutet, dass eine Klasse alle Methoden und Variablen der Superklasse übernimmt.
# Die Subklasse erweitert oder konkretisiert die Superklasse.

# Reh erbt alles von Säugetier.
class Reh(Saeugetier):
    def __init__(self):
        super().__init__()
        self.geweih=2

# Erzeuge Reh
Bambi=Reh()
# Das Reh hat die hoere-Methode der Klasse Saeugetier geerbt. Weiterhin hat es auch die Instanzvariablen ohren
# und beine geerbt, besitzt jedoch zusätzlich ein Geweih. Instanzen der Klasse Saeugetier besitzen jedoch kein Geweih.
Bambi.hoere()

########################

# (c) Überschreibung von Attributen und Methoden

# Eine Subklasse erbt alle Methoden und Varibalen der Superklasse, kann jedoch durch Überschreiben bestimmte Methoden
# und Variablen der Superklasse ersetzen.
# Um das Attribut oder die Methode zu überschreiben, wird der gleiche Name in der Subklasse erneut definiert

class Mutantenreh(Reh):
    def __init__(self):
        self.ohren=4

# Überschreiben einer Methode funktioniert ähnlich unter der Wiederverwendung des Methodennamen aus der Superklasse

BambUran=Mutantenreh()
BambUran.hoere()

########################

# (d) Aufruf einer Methode

# Eine Methode ist eine Funktion eines Objektes. Die Methoden definieren das Verhalten eines Objektes und verwenden
# dabei typischerweise Instanzvariablen.
# Aufruf der Methode hoehre des Objektes BambUran
BambUran.hoere()

########################

# (e) Unterklasse und Oberklasse

# Eine Unterklasse oder Subklasse ist ein Klasse, die alle Methoden und Variablen ihrer Superklasse oder auch Oberklasse
# erbt und diese überschreiben und eigene Methoden und Variablen besitzen kann.
# Die Subklasse erweitert oder konkretisiert die Superklasse.

# Superklasse: Saeugetier
# Subklasse: Reh
# Obermufti-Superklasse: Object
