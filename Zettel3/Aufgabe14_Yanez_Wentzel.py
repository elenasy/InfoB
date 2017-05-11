# Elena Schmidt Yanez, Bianca Wentzel
# 3. Aufgabenzettel, Informatik B
# Aufgabe 14

######################################################################################################################
#                               Aufgabe 14: lokale und globale Variablen                                             #
######################################################################################################################
# 1. Anweisungblock
def f(a, b):
    print("f: a =", a, " b =", b)
    a = a + b
    b += a
    a = 2 * b
    print("f: a =", a, " b =", b)

# Defineiren der gloablen Variablen a und b
a = 2
b = 4

print("main: a =", a, " b =", b)
f(b, a)
print("main: a =", a, " b =", b)
# Der erste Print-Befehl gibt die Werte der global belegten Variablen a =2 und b =4 aus
# Danach wird die Funktion f(b,a) (Achtung Reihenfolge) aufgerufen, die dann den ersten internen Print-Befehl
#  abarbeitet und a=4 und b=2 ausgibt. Danach werden die übergebenen Parameter intern verändert zu a= 4+2 also a=6
# und b+=6 also b=8  und dann wird die interne Variable a nochmal überschrieben mit a = 2*8 also a=16.
# Nun werden die veränderten lokalen Variablen ausgegeben, also a= 16 und b=8.
# Danach wird werden wieder die nach wie vor unveränderten gloablen Variablen a und b ausgegeben, also a=2 und b=4

# 2. Anweisungsblock
def f():
    print("Hier ist f.")
    return 5
def g1(a):
    x = a
    return x + 2 * a
def g2(a):
    x = a()
    return x + 2 * a()

print("main:", g1(f()))
print("main:", g2(f))

# Die erst ePrintanweisung ruft die Funktion g1 auf und übergibt ihr die Funktion f(). Zuerst wird also die
# Print-Anweisung der Funktion f() ausgeführt und dann der Wert 5 returnt und an die Funktion g1 übergeben. Dort wird
# dieser Wert als Parameter weitergegeben und lokal in der Funktion g1 in eine Variable x gespeichert. In der
# Retrun-Anweisung wird dann eine mathematische Operation damit ausgeführt und der zurückgegebene Wert ausgegeben:
# main=15 (a=5 und x=a -> 5+2*5)
# Nun wird die zweite Printanweisung ausgeführt. der Funktion g2 wird der Funktionsname f der Funktion f() übergeben.
# Innerhalb der Funktion g2 wird die lokale Varibale mit der Funktion f() belegt, da der Funktionname übergeben wird und
# mit den darauffolgenden () wieder zu einer Funktion wird.
# Im Return-Statement wird nun folgendes durchgeführt: f() + 2 * f(). Also wird zweimal hintereinander die Funktion f()
# aufgerufen, die dann ihre Pirnt-Anweisung ausführt und dann jedes mal "Hier ist f." ausgibt. Nach der Ausführung der
# Print-Anweisung in f(), gibt diese Funktion den Wert 5 zurück und demnach wird dann zum Schluss die mathematische
# Operation ausgeführt und zurückgegeben und dann ausgegeben. 5*2*5=15