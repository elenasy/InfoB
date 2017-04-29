# Bianca Wentzel
# Übungszettel 2, Informatik B
# Aufgabe 7b

#########################################################################################################
#                   Definieren der Funktionen zur Modifikation von a                                    #
#########################################################################################################
def f1(a):
    a = a+[a]

def f2(a):
    b=a
    b.append(7)

def f3(a):
    b = a + ['88']
    a.append([a,b])

#########################################################################################################
#                                    Ausführen der Funktionen                                           #
#########################################################################################################
# Definieren von a
a = [4,5,6]
print("a ist definert als a = [4,5,6]\n")
print()

# An die Funktion f1 wird eine Referenz auf a übergeben und innerhalb der Funktion wird der Wert von a
# modifziert, das Ergebnis jedoch nur in eine lokals Variable a gespeichert. Die lokale Varibale a enthält
# demnach folgenden Wert: a = [4,5,6,4,5,6]
# Dies gilt jedoch nur lokal innerhlab der Funktion, sodass die globale Variable a nach wie vor den Wert
# a = [4,5,6] besitzt.
print("Ausführen der Funktion f1")
f1(a)
print("Aktueller Wert der Variable a:")
print(a)
print()

# An die Funktion f2 wird wieder eine Referenz auf a übergeben und innerhalb der Funktion wird eine
# lokale Variable b definiert, die auf den Wert von a zeigt. An die Variable b wird nun der Wert 7
# angehangen. Da b und a den gleichen Wert referenzieren, zeigt nun auch die gloable Variable a auf
# den modifizierten Wert a = [4,5,6,7].
print("Ausführen der Funktion f2")
f2(a)
print("Aktueller Wert der Variable a:")
print(a)
print()

# An die Funktion f3 wir erneut eine Referenz auf a übergeben (Achtung a = [4,5,6,7]) und innerhalb der
# Funktion wird eine lokale Variable b definiert, die den Wert von a erweitert mit ['88'] enthält.
# Nun wird mittels a.append die globale Variable a so modifiziert, dass an a eine Liste angehangen wird,
# die den Wert der gloabeln Variable a enthält und den Wert der lokalen Variable b.
# Die globale Variable a sieht nun folgendermaßen aus: a = [4,5,6,7,[[4,5,6,7],[4,5,6,7,'88']]]
print("Ausführen der Funktion f3")
f3(a)
print("Aktueller Wert der Variable a:")
print(a)
print()

# Um nun auf das Element '88' zuzugreifen, müssen die Einträge der einzelnen verschachtelten Listen
# abgearbeitet werden.
# a[4] = [[4,5,6,7],[4,5,6,7,'88']]
# a[4][1] = [4,5,6,7,'88']
# a[4][1][4] = '88'
print("Zugreifen auf das Element '88' mit a[4][1][4]:")
print(a[4][1][4])