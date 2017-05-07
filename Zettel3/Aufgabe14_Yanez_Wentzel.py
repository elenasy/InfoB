# Elena Schmidt Yanez, Bianca Wentzel
# 3. Aufgabenzettel, Informatik B
# Aufgabe 14

######################################################################################################################
#                               Aufgabe 14: lokale und globale Variablen                                             #
######################################################################################################################
def f(a,b):
    print("f: a=",a," =",b)
    a=a+b
    b+=a
    a=2*b
    print("f: a=",a," =",b)

# Es werden die Variablen a und b global mit a=2 und b=4 belegt.
a=2
b=4
print("main: a=",a," b=",b)

f(a,b)
print("main: a=",a," b=",b)
















#####
def f():
    print("Hier ist f.")
    return 5
def g1(a):
    x=a
    return x+2*a
def g2(a):
    x=a()
    return x+2*a
print("main:",g1(f()))
print("main:",g2(f))
