# Zettel 4, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 18

######################################################################################################################
#                                           Aufgabe 18a Zufallszahlen                                                #
######################################################################################################################
from random import randint

def einzelExperiment(n):
    '''Erzeugt so lange Zufallszahlen, bis jede Zahl von 1 bis n einmal vorgekommen ist'''
    gewuerfelteZahlen={}
    anzahlDerWuerfe=0
    while len(gewuerfelteZahlen) != n:
        zufallszahl=randint(1,n)
        if zufallszahl not in gewuerfelteZahlen:
            gewuerfelteZahlen[zufallszahl]=1
        else:
            gewuerfelteZahlen[zufallszahl]+=1

        anzahlDerWuerfe+=1
    return gewuerfelteZahlen,anzahlDerWuerfe

######################################################################################################################
#                                         Einschub :Aufgabe 18b Zufallszahlen                                        #
######################################################################################################################
def findeHoechsteHaeufigkeit(wuerfeDict):
    '''Finden der höchstes Häufigkeit '''
    haeufigkeiten=wuerfeDict.values()
    groessteHaeufigkeit=max(haeufigkeiten)
    return groessteHaeufigkeit

# Durchführen der Experimente
print("##### Aufgabe 18 #####")
for n in [10,100,1000]:
    listeAnzahlDerWuerfe = []
    listeHaeufigkeiten=[]
    for versuchszahl in range(100):
        wuerfeDict,anzahlDerWuerfe=einzelExperiment(n)
        listeAnzahlDerWuerfe.append(anzahlDerWuerfe)
        listeHaeufigkeiten.append(findeHoechsteHaeufigkeit(wuerfeDict))

    print("##### Aufgabenteil 18a #####")
    print("Um jede Zahl zwischen 1 und {} einmal zu erzeugen, brauchte das Experiment mindestens {} , maximal {}"
          " und im Durchschnitt {} Würfe \n"
          .format(n, min(listeAnzahlDerWuerfe),max(listeAnzahlDerWuerfe), sum(listeAnzahlDerWuerfe)/len(listeAnzahlDerWuerfe)))

    print("##### Aufgabenteil 18b #####")
    print("Die Häufigkeit der häufigsten Zahl zwischen 1 und {} ist mindestens {} , höchstens {}"" und im Durchschnitt"
          " {} \n".format(n, min(listeHaeufigkeiten), max(listeHaeufigkeiten),sum(listeHaeufigkeiten) / len(listeHaeufigkeiten)))






