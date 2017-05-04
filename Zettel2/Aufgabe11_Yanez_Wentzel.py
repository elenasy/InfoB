# Elena Schmidt Yanez,Bianca Wentzel
# 2. Übungszettel, Informatik B
# Aufgabe 11

############################################################################################################
#                                Aufgabe 11) Finden des kürzestesn Weges                                   #
############################################################################################################
# Berechnung der Distanz vom Startknoten
def BFS(G,Startknoten):
    Distanz={Startknoten:0}
    L=[Startknoten]
    while L:
        u=L[0]
        del L[0]
        for v in G[u]:
            if v not in Distanz:
                Distanz[v]=Distanz[u]+1
                L.append(v)
    return Distanz

# Funktion zum Finden des kürzesten Wegs vom Start- zum Zielknoten anhand der berechneten Distanzen
def findeWeg(G,Distanzen,Zielknoten):
    # Überprüfen, ob der angegebene Zielpunkt ein gültiges Format besitzt
    if type(Zielknoten) != tuple:
        raise TypeError("Der Zielknoten muss ein Tupel sein!")

    #Überprüfen, ob der eingegebene Zielpunkt innerhalb des Gitter liegt
    if Zielknoten not in G:
        raise IndexError("Der Grpah enthält den angegebenen Knoten nicht!")

    weg=[]
    liste=[Zielknoten]
    while liste:
        aktuellerKnoten=liste[0]
        weg.append(aktuellerKnoten)
        del liste[0:] # es werden alle übrigen Knoten gelöscht, da nun die Nachbarknoten
        # von einem der gerfundenen Knoten berechnet werden sollen
        for nachbarKnoten in G[aktuellerKnoten]:
            if (Distanzen[nachbarKnoten] >= 0) and Distanzen[nachbarKnoten] == (Distanzen[aktuellerKnoten]-1):
                if nachbarKnoten not in weg:
                    liste.append(nachbarKnoten)
    return list(reversed(weg))

# Ausprobieren der Funktionen
# Defineiren eines Gitters
n=5
gitter = {
	(i,j) : [(i2,j) for i2 in (i-1,i+1) if i2 in range(n)] +
		[(i,j2) for j2 in (j-1,j+1) if j2 in range(n)]
	for i in range(n) for j in range(n) }

print("##### Aufgabe 11 #####")
print("Verwendeter Graph:")
print(gitter)
print()

print("Berechnung der Distanzen vom Knoten (1,1) ergibt:")
print(BFS(gitter,(1,1)))
dists=BFS(gitter,(1,1))

# Schöne Ausgabe der berechneten Distanzen
for i in range(n):
	for j in range(n):
		print(dists[i,j], end=' ')
	print()

print("Einer der kürzesten Wege vom Zielknoten (,):")
print(findeWeg(gitter,dists,(3,4)))
print()
print("##### Ende der Aufgabe #####")