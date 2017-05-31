# Aufgabenzettel 6, Infromatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 30

######################################################################################################################
#                                           Aufgabe 30a: Haldensortieren                                             #
######################################################################################################################

def schreibeElementInHeap(heap,element):
    # Einfügen des Elements an die letzte Stelle des Heaps
    heap.append(element)

    elementIndex = len(heap)-1
    elternIndex=(elementIndex-1)//2

    while heap[elementIndex] < heap[elternIndex]:
        heap[elementIndex], heap[elternIndex] = heap[elternIndex], heap[elementIndex]

        elementIndex = elternIndex
        elternIndex = elementIndex//2

    return heap

a=[5,1,4,2,7,3,6]
heap=[]

for listenelement in a:
    schreibeElementInHeap(heap,listenelement)

def berechneKinder(elternIndex):
    return (2 * elternIndex + 1, 2 * elternIndex + 2)

def berechneVergleichskind(heap,linkesKind,rechtesKind):
    if rechtesKind > len(heap)-1:
        vergleichsKind = linkesKind
    else:
        if heap[linkesKind] <= heap[rechtesKind]:
            vergleichsKind = linkesKind
        else:
            vergleichsKind = rechtesKind
    return vergleichsKind

def entferneElementAusHeap(heap):
    # Tauschen des Wurzelelements mit dem letzten Element
    heap[0],heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    wurzelElement=heap.pop()

    elternIndex=0
    linkesKind, rechtesKind = berechneKinder(elternIndex)

    if linkesKind > len(heap)-1:
        return (heap,wurzelElement)

    vergleichsKind= berechneVergleichskind(heap,linkesKind,rechtesKind)

    while heap[elternIndex] > heap[vergleichsKind]:
        heap[elternIndex],heap[vergleichsKind] = heap[vergleichsKind], heap[elternIndex]
        elternIndex=vergleichsKind

        linkesKind, rechtesKind = berechneKinder(elternIndex)

        if linkesKind > len(heap) - 1:
            break

        vergleichsKind = berechneVergleichskind(heap,linkesKind,rechtesKind)

    return (heap,wurzelElement)

sortierteListe=[]

for listenelement in a:
   heap,wurzelelement=entferneElementAusHeap(heap)
   sortierteListe.append(wurzelelement)

print(sortierteListe)
print(heap)

######################################################################################################################
#                                 Aufagbe 30b: Umschreiben von zuklein und zugroß                                    #
######################################################################################################################
# Umschreiben der Funktion zuklein ohne Rekursion

# def zuklein(liste,index):
#     '''Element a[i] der Halde ist eventuell zu klein'''
#     if index==1:
#         return
#
#     # Berechnen eines neues Indizes
#     eltern=index//2
#
#     # Wenn das Element an der Stelle des Indizes Eltern größer ist als an der Stelle des übergebenen Indizes, werden
#     # beide Elemente getauscht
#     if liste[eltern]>liste[index]:
#         liste[eltern],liste[index]=liste[index],liste[eltern]
#         return eltern
#
# # Ausfphren der Funktion ohne Rekursion
# index=5
# a=[5,1,4,3,7,2,6]
#
# while index!=1:
#     index=zuklein(a,index)

