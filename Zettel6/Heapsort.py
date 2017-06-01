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