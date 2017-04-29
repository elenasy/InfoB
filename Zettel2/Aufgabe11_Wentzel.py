# Bianca Wentzel
# 2. Übungszettel, Informatik B
# Aufgabe 11

############################################################################################################
#                                   Aufgabe 11) Finden des Weges                                           #
############################################################################################################
# Berchnung der Distanz vom Startknoten
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

#def findeWeg(G,Distanzen,Zielknoten):
#    pass

n=4
gitter={
    (i,j):[(i2,j2) for i2 in (i-1,i+1) if i2 in range(n)
                  for j2 in (j-1,j+1) if j2 in range(n)]
    for i in range(n) for j in range(n)}

print(BFS(gitter,(1,1)))
print(gitter)