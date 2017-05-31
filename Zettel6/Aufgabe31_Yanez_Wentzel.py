# Zettel 6, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 31

######################################################################################################################
#                                                   Aufgabe 31a: Münzen                                              #
######################################################################################################################
# Zum Wechseln des angegebenen Betrags benötigt man eine Liste der möglichen Münzwerte und den zu wechselnden Betrag
# Man benötigt weiterhin eine Liste mit den Münzen. die kleiner gleich dem Betrag sind und eine Liste, in der das
# Wechselgeld gespeichert wird

# Abfangen ungültiger Eingaben
# Wenn der übergebene Betrag keine ganze Zahl ist, wird ein Fehler ausgegeben

# Sortiere die Liste der Münzen (aufsteigend)

# Solange der Betrag größer als 0 ist

    # für jede Münze m beginnend mit der Letzten

        # wenn der aktuelle Münzwert m kleiner gleich dem Betrag ist

            # Schreibe Münzwert m in Liste (Wechselgeld)

            # aktualisiere Betrag durch Subtraktion mit Münzwert

            # Beende Ietration über Münzewerte

# Rückgabe der Wechselgeldliste

######################################################################################################################
#                                           Aufgabe 31b: Wechseln des Betrages                                       #
######################################################################################################################

def wechseln(munze, betrag):
    moeglichemuenzen=[]
    wechselgeld=[]

    # Abfangen ungültiger Betrageingaben
    if type(betrag) != int:
        raise TypeError("Der Betrag muss eine ganze Zahl sein!")

    # Abfangen ungültiger Übergaben der Münzwerte
    if type(munze) != list:
        raise TypeError("Es muss eine Liste mit ganzzahligen Münzwerten übergeben werden!")

    for element in munze:
        if type(element) != int:
            raise TypeError("Die Liste der Münzwerte darf nur ganze Zahlen enthalten!")

    # Sortieren der Münzbeträge
    munze.sort()

    while betrag > 0:
        for x in munze[::-1]:
            if x <= betrag:
                wechselgeld.append(x)
                betrag-=x
                break

    return wechselgeld

print("##### Aufgabe 31b #####")
print("Münzwerte=[1,2,5,10,20,50,100,200]")
munze = [1, 2, 5, 10, 20, 50, 100, 200]
print()
print("Es soll folgender Betrag gewechselt werden: 261 Cent")
print("Der Betrag wurde folgendermaßen gewechselt:")
print(wechseln(munze, 261))
print()

######################################################################################################################
#                                           Aufgabe 31c: Greedy Algorithmus                                          #
######################################################################################################################

# Die Münze 25 Cent funktioniert mit dem Greedy Algorithmus nicht, da bspw. bei einem Betrag
# von 41 Cent und Münzen inklusiver der 25 Cent-Münze, der Greedy Algorithmus vorerst die Münze mit dem großten Betrag
# wählen würde, welche sich innerhalb der 41 Cent befindet. Das ist die 25 Cent Münze. Der Greedy Algorithmmus würde
# sich für folgende Münzen entscheiden: 25 Cent + 10 Cent + 5 Cent + 2 Cent + 2 Cent
# Allerdings ist eine andere Kombination von Münzen sinnvoller. Um die kleinstmögliche Anzahl von Münzen zu verwenden,
# sollte das Ergebnis 20 Cent + 20 Cent + 1 Cent lauten. Wir würden drei anstelle von 5 Münzen wechseln.