# Zettel 7 , Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 34

######################################################################################################################
#                               Aufgabe 34: Finden des kürzesten Wegs                                                #
######################################################################################################################

# Berechnung der Wichtung der jeweiligen Kante
def wichtung(x1,y1,x2,y2):
    ergebnis = 3*(x1-2*y2)**2+abs(((12*x2+20*y1)%17)-8)
    return ergebnis

# Erstellen des gerichteten und gewichteten Graphen
n=4
gitter = {
    (i,j): [[(i2,j),wichtung(i,j,i2,j)] for i2 in (i-1,i+1) if i2 in range(n)] +
        [[(i,j2),wichtung(i,j,i,j2)] for j2 in (j-1,j+1) if j2 in range(n)]
    for i in range(n) for j in range(n)}

###################################################################################################################

# Finden des Nachbarknotens mit dem kürzesten Abstand
def findeNaechstenNachbar(graph,aktuellerKnoten,listeAllerKnoten):
    nachbar=()
    abstand=float("inf")

    for element in graph[aktuellerKnoten]:
        if element[0] in listeAllerKnoten:
            if element[1] < abstand:
                nachbar=element[0]
                abstand=element[1]
    return [nachbar,abstand]


def findeKuerzestenWeg(graph,start,ziel):
    # Initialisieren
    abstand={}
    vorgaenger={}
    listeAllerKnoten=[]

    for x in range(4):
        for y in range(4):
            knotenpunkt = (x, y)
            if knotenpunkt not in listeAllerKnoten:
                listeAllerKnoten.append(knotenpunkt)

    for knoten in graph:
        abstand[knoten]=float("inf")
        vorgaenger[knoten]=[]
        abstand[start]=0

    aktuellerKnoten=(start)
    del listeAllerKnoten[listeAllerKnoten.index(aktuellerKnoten)]

    while listeAllerKnoten:
        naechsterNachbar,abstand[naechsterNachbar]=findeNaechstenNachbar(graph,aktuellerKnoten,listeAllerKnoten)

        del listeAllerKnoten[listeAllerKnoten.index(naechsterNachbar)]

        for nachbar in graph[naechsterNachbar]:
            if nachbar[0] in listeAllerKnoten:
                neuerAbstand=abstand[naechsterNachbar]+nachbar[1]
                if neuerAbstand < abstand[nachbar[0]]:
                    abstand[nachbar[0]]=neuerAbstand
                    vorgaenger[nachbar[0]]=naechsterNachbar

        aktuellerKnoten=naechsterNachbar

    weg=[]
    weg.append(ziel)
    momentanerKnoten=ziel
    while vorgaenger[momentanerKnoten]:
        momentanerKnoten=vorgaenger[momentanerKnoten]
        weg.append(momentanerKnoten)
    weg.append(start)

    return list(reversed(weg))

print(findeKuerzestenWeg(gitter,(0,0),(2,2)))




