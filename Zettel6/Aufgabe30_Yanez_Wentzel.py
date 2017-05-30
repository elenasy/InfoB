# Aufgabenzettel 6, Infromatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 30

######################################################################################################################
#                                           Aufgabe 30a: Haldensortieren                                             #
######################################################################################################################

def haldensortierung(liste):
    halde=[]
    sortierteliste=[]

    # Afabgen ungültiger Parameterübergaben
    if type(liste) != list:
        raise TypeError("Es muss eine Liste übergeben werden!")

    for element in liste:
        if type(element) != int and type(element) != float:
            raise TypeError("Die Liste darf ausschließlich numerische Elemente beinhalten")

    # Übergeben der Elemente der Liste der Reihe nach
    for element in liste:
        halde.append(element)

    # Counter zur Nachverfolgung der Schritte
    count=0

    while len(halde)>0:
        print("Schritt: ",count)
        print("Halde: ",halde)
        print("Sortierte Liste: ",sortierteliste)
        print()

        # Schreiben des Minimums der Halde in die sortierte Liste und anschließendes Finden des Indexes dieses Elements
        # und Löschen des Elements aus der Halde
        sortierteliste.append(min(halde))
        for i,j in enumerate(halde):
            if j == min(halde):
                index=i
        del halde[index]
        count+=1

    print("Schritt: ",count)
    print("Halde: ",halde)
    print("Sortierte Liste: ",sortierteliste)

a=[5,1,4,3,7,2,6]
haldensortierung(a)

######################################################################################################################
#                                 Aufagbe 30b: Umschreiben von zuklein und zugroß                                    #
######################################################################################################################
# Umschreiben der Funktion zuklein ohne Rekursion

def zuklein(liste,index):
    '''Element a[i] der Halde ist eventuell zu klein'''
    if index==1:
        return

    # Berechnen eines neues Indizes
    eltern=index//2

    # Wenn das Element an der Stelle des Indizes Eltern größer ist als an der Stelle des übergebenen Indizes, werden
    # beide Elemente getauscht
    if liste[eltern]>liste[index]:
        liste[eltern],liste[index]=liste[index],liste[eltern]
        return eltern

# Ausfphren der Funktion ohne Rekursion
index=5
a=[5,1,4,3,7,2,6]

while index!=1:
    index=zuklein(a,index)

