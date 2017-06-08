# Zettel 7 , Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 34

######################################################################################################################
#                               Aufgabe 34: Finden des kürzesten Wegs                                                #
######################################################################################################################
def wichtung(x1,y1,x2,y2):
    '''Funktion berechnet die Wichtung einer Kante zwischen den Knoten (x1,y1) und (x2,y2)'''
    ergebnis = 3*(x1-2*y2)**2+abs(((12*x2+20*y1)%17)-8)
    return ergebnis

# Erstellen des gerichteten und gewichteten Graphen
n=8
gitter = {
    (i,j): [[(i2,j),wichtung(i,j,i2,j)] for i2 in (i-1,i+1) if i2 in range(n)] +
        [[(i,j2),wichtung(i,j,i,j2)] for j2 in (j-1,j+1) if j2 in range(n)]
    for i in range(n) for j in range(n)}



def findeGeringsteDistanz(abstand):
    '''Funktion findet den geringsten Abstand im Wörterbuch 'abstand' und Übergibt diesen und den dazugehörigen Key'''
    knoten=min(abstand)
    kleinsteDistanz=abstand[knoten]

    return[knoten,kleinsteDistanz]

# Finden des kürzesten Weges im Gitter durch die Anwendung des Dijkstra-Algorithmus
def findeKuerzestenWeg(graph,start,ziel):

    # Abfangen ungültiger Start- und Endpunkteingaben
    # Achtung: Algorithmus könnte allgemein angewandt werden und dann ist dieses Abfangen nicht mehr unbedingt richtig
    # Für diese spezielle Aufgabe jedoch, sollte man zumindest sicherstellen, dass es sich um Tupel handelt
    if type(start)!=tuple or type(ziel)!=tuple:
        raise TypeError("Die eigegbenen Punkte müssen Tupel sein!")

    ### Initialisieren
    abstand={}
    vorgaenger={}
    listeAllerKnoten=[]
    minAbstand=float("inf")

    # Erzeugen einer Liste mit allen Knoten des Gitters
    for x in range(n):
        for y in range(n):
            knotenpunkt = (x, y)
            if knotenpunkt not in listeAllerKnoten:
                listeAllerKnoten.append(knotenpunkt)


    for knoten in graph:
        abstand[knoten]=float("inf") # Belegen aller Keys des Abstands-Wörterbuches mit 'unendlich'
        vorgaenger[knoten]=[]

    abstand[start]=0
    aktuellerKnoten=(start)

    while listeAllerKnoten:
        geringsterKnoten,abstand[geringsterKnoten]=findeGeringsteDistanz(abstand)
        del listeAllerKnoten[listeAllerKnoten.index(geringsterKnoten)]

        # Berechnen bzw. Updaten der Abstände angrenzender Punkte zum aktuellen Punkt
        for nachbar in graph[geringsterKnoten]:
            if nachbar[0] in listeAllerKnoten:
                neuerAbstand=abstand[geringsterKnoten]+nachbar[1]
                if neuerAbstand < abstand[nachbar[0]]:
                    abstand[nachbar[0]]=neuerAbstand
                    vorgaenger[nachbar[0]]=geringsterKnoten

        aktuellerKnoten=geringsterKnoten
        del abstand[geringsterKnoten]

        # Abbruch, wenn Ziel erreicht
        if aktuellerKnoten == ziel:
            break

    weg=[]
    weg.append(ziel)
    momentanerKnoten=ziel
    # Zurückverfolgen des Weges anhand der Vorgänger
    while vorgaenger[momentanerKnoten]:
        momentanerKnoten=vorgaenger[momentanerKnoten]
        weg.append(momentanerKnoten)

    return list(reversed(weg))

# Ausprobieren der Funktion
print("##### Aufgabe 34 #####")
print("Finden des kürzesten Wegs in einem gewichteten 8x8-Gitter von Startpunkt (0,0) bis zum Ziel (7,7)")
print("Der kürzeste Weg ist: ")
print(findeKuerzestenWeg(gitter,(0,0),(7,7)))
print("##### ENDE #####")





