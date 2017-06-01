# Aufgabenzettel 6, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 30

######################################################################################################################
#                                           Aufgabe 30a: Haldensortieren                                             #
######################################################################################################################
# Lösung siehe Aufgabe30a_Yanez_Wentzel.pdf
# Wir dachten, es wäre so anschaulicher zu erklären und schöner zu kontrollieren.

######################################################################################################################
#                                 Aufagbe 30b: Umschreiben von zuklein und zugroß                                    #
######################################################################################################################
# Umschreiben der Funktion zuklein ohne Rekursion

def zuklein(a,i):
    "Element a[i] der Halde ist eventuell zu klein."
    if i== 1:
        return
    eltern = i//2

    while a[eltern]>a[i] and i > 1:
        a[eltern],a[i] = a[i],a[eltern]

        i = eltern
        eltern = i//2

# Umschreiben der Funktion zugroß ohne Rekursion

def zugroß(a,n,i):
    "Element a[i] der Halde a[1..n] ist eventuell zu groß."

    while True:
        kind1 = 2*i     # linkes Kind
        kind2 = 2*i+1   # rechtes Kind

        if kind1 > n:   # linkes Kind existiert nicht
            return

        if kind2 > n:  # rechtes Kind existiert nicht, aber linkes Kind
            kind = kind1
        else:
            if a[kind1] < a[kind2]:
                kind = kind1
            else:
                kind = kind2

        if a[kind]>a[i]:    # Wenn das kleinste Kind größer als das Elternelement ist, können wir aufhören,
            return          # da die Heapbedingung erfüllt ist
        else:
            a[kind], a[i] = a[i], a[kind]
            i=kind





