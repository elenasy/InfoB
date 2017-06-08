# -*- coding: utf-8 -*-
# Zettel 7, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 35

######################################################################################################################
#                                   Aufgabe 35: Geld wechseln durch Backtracking                                     #
######################################################################################################################
def munzeIstZulaessig(munze,betrag):
    '''Funktion zur Prüfung, ob der Wert der gegebenen Münze kleiner gleich dem gegebenen
    Betrag'''
    if munze<=betrag:
        return True
    else:
        return False

def wechseln(muenztypen,betrag):
    '''Bestimmen aller möglichen Wechselbeträge durch Backtracking und finden des optimalen
    Wechselzustandes aus den gegebenen Münztypen 'muenztypen' für den gegebenen Betrag 'betrag' '''
    # Abfangen ungültiger Betrageingaben
    if type(betrag) != int:
        raise TypeError("Der Betrag muss eine ganze Zahl sein!")

    # Abfangen ungültiger Übergaben der Münzwerte
    if type(muenztypen) != list:
        raise TypeError("Es muss eine Liste mit ganzzahligen Münzwerten übergeben werden!")

    for element in muenztypen:
        if type(element) != int:
            raise TypeError("Die Liste der Münzwerte darf nur ganze Zahlen enthalten!")

    # Initialisieren
    muenzindex=0
    maxIndexMuenztypen=len(muenztypen)-1
    loesung=[]
    gesamtloesung=[]
    lange = float("inf")

    while True:
        while True:
            # Wenn Münzindex größer als Anzahl der Münzen, brich ab und suche die optimale
            # Lösung aus den gespeicherten, möglichen Wechselungen
            if muenzindex > maxIndexMuenztypen:

                indexloesung=0
                for index,teilloesung in enumerate(gesamtloesung):
                    if len(teilloesung)<lange:
                        lange=len(teilloesung)
                        indexloesung=index
                return gesamtloesung[indexloesung]

            # Wenn letzte Münze aus Liste ausgewählt
            if muenzindex==maxIndexMuenztypen:
                if munzeIstZulaessig(muenztypen[muenzindex], betrag):
                    # Münze ist zulässig und würde zur Lösung des Problems führen
                    # Füge Münze zur Teillösung an und speicher die Teillösung,
                    # Setze den Betrag auf Anfangsbetrag zurück und leere Teillösungsliste
                    if betrag - muenztypen[muenzindex]==0:
                        betrag += sum(loesung)
                        loesung.append(muenztypen[muenzindex])
                        gesamtloesung.append(list(loesung))
                        del loesung[:]
                    # Münze ist zulässig aber das Problem ist nicht gelöst
                    # Füge Münze zur Teillösung hinzu und beginne bei der ersten Münze der Liste
                    else:
                        loesung.append(muenztypen[muenzindex])
                        betrag -= muenztypen[muenzindex]
                        muenzindex = 0
                else:
                    break


            if muenzindex < maxIndexMuenztypen:
                # wenn gewählte Münze zulässig ist, dann schreibe diese in die Lösung
                # und aktualisiere den Betrag, dann nimm wieder die erste Münze aus
                # dem Münzstapel
                if munzeIstZulaessig(muenztypen[muenzindex],betrag):
                    if betrag - muenztypen[muenzindex]==0:
                        betrag += sum(loesung)
                        loesung.append(muenztypen[muenzindex])
                        muenzindex = muenztypen.index(loesung[0]) + 1
                        gesamtloesung.append(list(loesung))
                        del loesung[:]
                    else:
                        loesung.append(muenztypen[muenzindex])
                        betrag-=muenztypen[muenzindex]
                        muenzindex=0
                # Wenn die Münze nicht zulässig ist , nimm die nächste Münze
                else:
                    muenzindex+=1


# Leider Funktioniert der Algorithmus nicht so, wie er eigentlich soll. Er findet nicht alle möglichen Lösungen und
# deshalb dann auch nicht die optimale, weil die optimale meistens leider gar nicht gefunden wurde.


# Ausprobieren der Funktion
kleingeld=[50,10,5,2,15,1]
print("##### Aufgabe 35 #####")
print("Wechseln des Betrags 30 Cent durch Backtracking")
print("Die gegebenen Münzen sind: [50,10,5,2,15,1]")
print("Die vom Algorithmus gefundene, optimale Lösung lautet: ")
print(wechseln(kleingeld,30))
print("Leider nicht optimal :(")
print("##### ENDE #####")

# Man hätte vielleicht noch mit einer sortierten Liste der Münzwerte arbeiten können


