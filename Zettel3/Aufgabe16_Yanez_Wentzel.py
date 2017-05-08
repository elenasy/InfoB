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
        return (self.ausgangsufer == other.ausgangsufer and self.floss == other.floss and self.endufer == other.endufer)

    # Finden der Folgezustände des gegebenen Zustandes
    def findeFolgezustaende(self):
        folgezustaende=[]

        # Transport nach rechts
        for wesen in range(len(self.endufer)):
            if self.floss:
                platzhalterFloss=(self.floss,)
            else:
                platzhalterFloss=()
            folgeZustandEndufer=self.endufer[wesen+1:]+platzhalterFloss+self.endufer[:wesen]
            folgeZustandFloss=self.endufer[wesen]
            folgezustaende.append((self.ausgangsufer,folgeZustandFloss,folgeZustandEndufer))

        # Nur rechts abladen
        folgezustaende.append((self.ausgangsufer,(),self.endufer+(self.floss,)))

    # Transport nach links
        for wesen in range(len(self.ausgangsufer)):
            if self.floss:
                platzhalterFloss=(self.floss,)
            else:
                platzhalterFloss=()
            folgeZustandAusgangsufer=self.ausgangsufer[wesen+1:]+platzhalterFloss+self.ausgangsufer[:wesen]
            folgeZustandFloss=self.ausgangsufer[wesen]
            folgezustaende.append((folgeZustandAusgangsufer,folgeZustandFloss,self.endufer))

        # Nur links abladen
        folgezustaende.append((self.ausgangsufer + (self.floss,), (), self.ausgangsufer))

        return [Zustand(einzelzustand) for einzelzustand in folgezustaende]

# Erzeugen des Graph-Wörterbuches
def graphWoerterbuch(startzustand):
    # Erzeugen des ersten Zustandes (Keys) und den dazugehörigen Folgezuständen (Value)
    ersterZustand = Zustand(startzustand)
    folgezustaendeErsterZustand = ersterZustand.findeFolgezustaende()

    # Eröffnen des Graph-Wörterbuches
    wzkGraph={ersterZustand: folgezustaendeErsterZustand}
    warteschlange=folgezustaendeErsterZustand

    # Breitensuche zur Belegung des Wörterbuchs
    while warteschlange:
        aktuellerZustand=warteschlange[0]
        del warteschlange[0]
        if aktuellerZustand not in wzkGraph:
            folgezustaendeNeuerZustand=aktuellerZustand.findeFolgezustaende()
            #print(type(folgezustaendeNeuerZustand))
            wzkGraph[aktuellerZustand]=folgezustaendeNeuerZustand

            warteschlange+=folgezustaendeNeuerZustand
            #print(folgeZustand,":", folgezustaendeNeuerZustand)
            #print()

    return wzkGraph


graphWoerterbuch((('W','K'),'',('S',)))



#versuch=Zustand((('W','K'),'',('S',)))
#print(versuch.findeFolgezustaende())


