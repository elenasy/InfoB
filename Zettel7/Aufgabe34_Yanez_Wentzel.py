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
n=3
gitter = {
    (i,j): [[(i2,j),wichtung(i,j,i2,j)] for i2 in (i-1,i+1) if i2 in range(n)] +
        [[(i,j2),wichtung(i,j,i,j2)] for j2 in (j-1,j+1) if j2 in range(n)]
    for i in range(n) for j in range(n)}

###################################################################################################################

def findeGeringsteDistanz(abstand,listeAllerKnoten,minAbstand):
    knoten=()
    kleinsteDistanz=float("inf")

    for element in abstand:
        if element in listeAllerKnoten:
            if abstand[element] <= minAbstand:
                knoten=element
                kleinsteDistanz=abstand[element]
                minAbstand=kleinsteDistanz
    return[knoten,kleinsteDistanz,minAbstand]


def findeKuerzestenWeg(graph,start,ziel):

    ### Initialisieren
    abstand={}
    vorgaenger={}
    listeAllerKnoten=[]
    minAbstand=float("inf")

    for x in range(n):
        for y in range(n):
            knotenpunkt = (x, y)
            if knotenpunkt not in listeAllerKnoten:
                listeAllerKnoten.append(knotenpunkt)

    for knoten in graph:
        abstand[knoten]=float("inf")
        vorgaenger[knoten]=[]

    abstand[start]=0

    aktuellerKnoten=(start)

    while listeAllerKnoten:
        geringsterKnoten,abstand[geringsterKnoten],minAbstand=findeGeringsteDistanz(abstand,listeAllerKnoten,minAbstand)

        del listeAllerKnoten[listeAllerKnoten.index(geringsterKnoten)]

        for nachbar in graph[geringsterKnoten]:
            if nachbar[0] in listeAllerKnoten:
                neuerAbstand=abstand[geringsterKnoten]+nachbar[1]
                if neuerAbstand < abstand[nachbar[0]]:
                    abstand[nachbar[0]]=neuerAbstand
                    vorgaenger[nachbar[0]]=geringsterKnoten

        minAbstand=findeGeringsteDistanz(abstand,listeAllerKnoten,minAbstand)[2]
        aktuellerKnoten=geringsterKnoten
        if aktuellerKnoten == ziel:
            break

    weg=[]
    weg.append(ziel)
    momentanerKnoten=ziel
    while vorgaenger[momentanerKnoten]:
        momentanerKnoten=vorgaenger[momentanerKnoten]
        weg.append(momentanerKnoten)
    weg.append(start)

    return list(reversed(weg))

print(findeKuerzestenWeg(gitter,(0,0),(1,4)))




