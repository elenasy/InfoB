# Zettel 5, Informatik B
# Elena, Schmidt Yanez, Bianca Wentzel
# Aufgabe 23

######################################################################################################################
#                                           Aufgabe 23a: Insertion Sort                                              #
######################################################################################################################
# Bei dem Sortieren durch Einfügen, geht man das Feld von links durch.
# Hier beispielhaft der Quellcode des Insertion-Sort-Algorithmus
# Vorerst wird eine Hilfsfunktion definiert, die besagt, dass die Zahlen den Platz tauschen.
def swap (a,i,j):
    a[i],a[j]=a[j],a[i]

def insertionSort(a):
    for i in range(1,len(a)):
        j=i-1
        while j>=0 and a[j]>a[j+1]:
            swap(a,j,j+1)
            j=j-1

# Hier nun die ausführliche Erklärung, wie das Insertionsort-Verfahren funktioniert/ arbeitet:

# Ausgangsliste: [5,1,4,2,7,3,4]

# Zuerst wird das zweite Element der Liste ausgewählt (hier die 1) und mit dem ersten Element der Liste verglichen.
# Da das erste Element der Liste größer ist, als das aktuell ebtrachtete Element, werden die beiden getauscht.

# Neue Form der Liste: [1,5,4,2,7,3,4]

# Nun wird das dritte Element der Liste ausgwählt (hier die 4) und mit dem zweiten Element der Liste verglichen.
# Da die 5 größer als die 4 ist, werden die beiden Elemente getauscht. Nun wird die 4 mit dem ersten Element der Liste
# verglichen, also der 1. Da die 1 kleiner ist als die 4, werden die beiden Elemente an den Plätzen belassen, an denen
# sie sich befinden.

# Neue Form der Liste: [1,4,5,2,7,3,4]

# Nun wird das vierte Element (hier die 2) der Liste ausgewählt und mit dem dritten Element der Liste verglichen.
# Da die 5 größer ist als die 2, werden die beiden Elemente getauscht. Nun wird die 2 mit der 4 (2. Element) verglichen.
# Da auch die 4 größer als die 2 ist, tauschen die Elemente ihre Plätze. Nun wird die 2 mit der 1 verlgichen und da die
# 1 kleiner ist als die 2, bleiben die beiden Elemente an ihren Plätzen.

# Neue Form der Liste: [1,2,4,5,7,3,4]

# Nun wird das fünfte Element der Liste (also die 7) ausgewählt und mit dem vierten Element, also der 5 verlgichen.
# Da die 5 kleiner als die 7 ist, bleibt die 7 an ihrem Platz in der Liste.

# Neue Form der Liste: [1,2,4,5,7,3,4]

# Nun wird das sechste Element der Liste, also die 3, ausgewählt und mit dem vorherigen Element verlgichen. Da die 7
# größer als die 3 ist, tauschen die beiden Elemente ihre PLätze. Nun wird die 5 mit der 3 verglichen und erneut
# werden die Plätze getauscht, da die 5 größer als die 3 ist. Nun wird die 4 mit der 3 verglichen und wiederum
# getauscht, da auch die 4 größer als die 3 ist. Nun vergleicht man die 2 mit der 3 und beide Elemente behalten ihre
# Plätz ein der Liste bei, da die 2 kleiner als die 3 ist und demnach nicht getauscht wird.

# Neue Form der Liste: [1,2,3,4,5,7,4]

# Nun wird das letzte Element der Liste ausgewählt und mit dem Element davor verglichen. Da die 7 größer als die 4 ist,
# tauschen beide Elemente ihre Plätze. Dann wird die 5 mit der 4 verglichen und wiederum getauscht, da die 5 größer als
# die 4 ist. Nun wird die 4 mit der 4 verglichen und da die 4 (4. Element) nicht größer als das ausgewählte Element ist,
# wird nicht mehr getauscht.

# Finale Form der Liste: [1,2,3,4,4,5,7]









# Aufgabe 23 b alternativer Sortieralgorithmus
# Ein alternativer Sortieralgorithmus zu Insertion-Sort ist Selection-Sort.
# Bei Selection-Sort wird ein Durchlauf '?''?'ber alle Elemente gemacht und das kleinste
Element bestimmt.
# Das kleinste Element wird an die 1.Stelle gebracht.
# Da zum Ermitteln des Minimums immer der komplette nocht nicht sortierte Teil des
Arrays durchlaufen werden muss,
# ben'?''?'tigt Selection-Sort auch im besten Fall (n*(n-1))/2 Vergleiche.
# Laufzeit: Insertion-Sort ben'?''?'tigt im Durchschnitt (n*(n-1))/4 Vergleiche.
# Das sind bereits weniger als der beste Fall des Selection-Sort. Die Laufzeit von
Selection-Sort ist deswegen
# langsamer, als Insertion-Sort.
