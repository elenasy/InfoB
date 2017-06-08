# -*- coding: utf-8 -*-
# Zettel 7, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 35

######################################################################################################################
#                                   Aufgabe 35: Geld wechseln durch Backtracking                                     #
######################################################################################################################
def munzeIstZulaessig(munze,betrag):
    if munze<=betrag:
        return True
    else:
        return False

def wechseln(muenztypen,betrag):
    muenzindex=0
    maxIndexMuenztypen=len(muenztypen)-1
    loesung=[]
    gesamtloesung=[]
    lange = float("inf")

    while True:
        while True:
            # wenn aktuelle Münze die letzte in Liste
            if muenzindex > maxIndexMuenztypen:
                indexloesung=0
                for index,teilloesung in enumerate(gesamtloesung):
                    if len(teilloesung)<lange:
                        lange=len(teilloesung)
                        indexloesung=index
                return gesamtloesung[indexloesung]

            if muenzindex==maxIndexMuenztypen:
                # wenn Münze zulässig
                if munzeIstZulaessig(muenztypen[muenzindex], betrag):
                    # wenn Lösung erreicht wäre
                    if betrag - muenztypen[muenzindex]==0:
                        betrag += sum(loesung)
                        loesung.append(muenztypen[muenzindex])
                        gesamtloesung.append(list(loesung))
                        del loesung[:]
                    else:
                        loesung.append(muenztypen[muenzindex])
                        betrag -= muenztypen[muenzindex]
                        muenzindex = 0
                # Münze ist nicht zulässig und letzte in Liste
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



# Ausprobieren der Funktion
kleingeld=[50,10,5,2,20,30,1]

print(wechseln(kleingeld,55))


