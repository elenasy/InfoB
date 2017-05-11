# Zettel 3, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 16

######################################################################################################################
#                                   Aufgabe 16) Das Ziege-Kohlkopf-Wolf-Problem                                      #
######################################################################################################################
# Der Zustand soll unveränderlich sein und besteht aus drei unterschiedlichen Bestandteilen:
# 1. Bestandteil: das linke Ufer, also das Asugangsufer (Liste mit maximal 3 Elementen)
# 2. Bestandteil: das Floß, dass den Fluss überquert (Variable)
# 3. Bestandteil: das rechte Ufer, also das Endufer (Liste mit maximal 3 Elemeneten)

# Allemöglichen Zustände werden in ein Wörterbuch geschrieben und ihnen werden die für den Zustand möglichen
# Folgezustände zugeordnet (Zustand: mögliche Folgezustände) und anhand des Wörterbuches wird eine BFS durchgeführt,
# bis der Weg gefunden wurde, der zum Ergebnis führt, dass alle am Endufer angelangt sind.

class Zustand():
    # Konstruktion einer Instanz mit den Attributen des Ausgangsufers, Des Floßes, des Endufers und der Folgezustände
    def __init__(self,wzkzustand):
        self.ausgangsufer=wzkzustand[0]
        self.floss=wzkzustand[1]
        self.endufer=wzkzustand[2]

    # Überschreiben der hash-Methode der obersten Klasse Object
    # Es wird ein hash aus den Werte des Objektes erzeugt und dieser wird zur Indexierung im Wörterbuch verwendet
    # Vergleich der Hashes der Keys
    def __hash__(self):
        return hash((self.ausgangsufer, self.floss, self.endufer))

    # Überschreiben der eual-Methode der Oberklasse Object
    # Vergleich der Keys anhand ihrer Elemente
    def __eq__(self, other):
        return (set(self.ausgangsufer) == set(other.ausgangsufer) and set(self.floss) == set(other.floss) and set(self.endufer) == set(other.endufer))

    # Zur Verbesserung der Ausgabe
    def __str__(self):
        return str(self.ausgangsufer) + str(self.floss) + str(self.endufer)

    def __repr__(self):
        return self.__str__()

    # Abfangen der unmöglichen/ tötlichen Kombinationen aus Kohlkopf und Schaf und Wolf und Schaf
    def istUfermoeglich(self,uferZustand):
        if set(uferZustand) == set(('W','S')) or set(uferZustand) == set(('S','K')):
            return False
        else:
            return True

    # Finden der Folgezustände des gegebenen Zustandes
    def findeFolgezustaende(self):
        folgezustaende=[]

        # Transport nach rechts
        if self.floss:
            platzhalterFloss = (self.floss,)
        else:
            platzhalterFloss = ()

        for wesen in range(len(self.endufer)):
            folgeZustandEndufer=self.endufer[:wesen]+platzhalterFloss+self.endufer[wesen+1:]
            folgeZustandFloss=self.endufer[wesen]
            if self.istUfermoeglich(folgeZustandEndufer):
                folgezustaende.append((self.ausgangsufer,folgeZustandFloss,folgeZustandEndufer))

        # Nur rechts abladen
        if self.floss and self.istUfermoeglich(self.endufer+platzhalterFloss):
            folgezustaende.append((self.ausgangsufer,(),self.endufer+platzhalterFloss))

    # Transport nach links
        for wesen in range(len(self.ausgangsufer)):
            folgeZustandAusgangsufer=self.ausgangsufer[:wesen]+platzhalterFloss+self.ausgangsufer[wesen+1:]
            folgeZustandFloss=self.ausgangsufer[wesen]
            if self.istUfermoeglich(folgeZustandAusgangsufer):
                folgezustaende.append((folgeZustandAusgangsufer,folgeZustandFloss,self.endufer))

        # Nur links abladen
        if self.floss and self.istUfermoeglich(self.ausgangsufer + platzhalterFloss):
            folgezustaende.append((self.ausgangsufer + platzhalterFloss, (), self.endufer))

        return [Zustand(einzelzustand) for einzelzustand in folgezustaende]

# Erzeugen des Graph-Wörterbuches
def graphWoerterbuch(startzustand):
    # Erzeugen des ersten Zustandes (Keys) und den dazugehörigen Folgezuständen (Value)
    ersterZustand = Zustand(startzustand)
    folgezustaendeErsterZustand = ersterZustand.findeFolgezustaende()

    # Eröffnen des Graph-Wörterbuches
    #wzkGraph={ersterZustand: folgezustaendeErsterZustand}
    wzkGraph = {}
    #warteschlange=folgezustaendeErsterZustand
    warteschlange = [ersterZustand]

    # Breitensuche zur Belegung des Wörterbuchs
    while warteschlange:
        aktuellerZustand=warteschlange[0]
        del warteschlange[0]
        if aktuellerZustand not in wzkGraph:
            folgezustaendeNeuerZustand=aktuellerZustand.findeFolgezustaende()
            wzkGraph[aktuellerZustand]=folgezustaendeNeuerZustand
            warteschlange+=[zustand for zustand in folgezustaendeNeuerZustand if zustand not in warteschlange]


    return wzkGraph

# Ausprobieren
print("##### Aufgabe 16 #####")
derGraph=graphWoerterbuch((('W','K','S'),(),()))
print("Der Graph:")
for x in derGraph:
    print(x," : ", derGraph[x])

print("Ausprobieren des Wegfindens ... leider nicht erfolgreich :(")
def sucheWeg(Vorgänger, ziel):
    z = ziel
    weg = []
    while z is not None:
        weg.append(z)
        z = Vorgänger[z]
    weg.reverse()
    return weg

# Funktion zum Finden des kürzesten Wegs vom Start- zum Zielknoten
def findeWeg(G,Startzustand,Zielzustand):

    vorgaenger={}
    liste=[Startzustand]

    while liste:
        aktuellerZustand=liste[0]
        #weg.append(aktuellerZustand)
        del liste[0]
        if aktuellerZustand == Zielzustand:
            return sucheWeg(vorgaenger,Zielzustand)

        for nachbarKnoten in G[aktuellerZustand]:
            if not nachbarKnoten in vorgaenger[aktuellerZustand]:
                vorgaenger[nachbarKnoten]=aktuellerZustand

            if nachbarKnoten not in liste:
                liste.append(nachbarKnoten)

gefundenerWeg=findeWeg(derGraph,Zustand((("W","K","S"),(),())),Zustand(((),(),("W","K","S"))))
print(gefundenerWeg)
print()





