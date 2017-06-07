# Zettel 7, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 35

######################################################################################################################
#                                   Aufgabe 35: Geld wechseln durch Backtracking                                     #
######################################################################################################################
def munzeIstZulaessig(munze,betrag):
    if munze<=betrag:
        return True
    else:
        return False

def wechseln(muenztypen,betrag):
    muenzindex=0
    maxIndexMuenztypen=len(muenztypen)-1
    teilloesung=[]
    loesung=[]

    while True:
        while True:
            # wenn letztes Element der möglichen Münzstücke erreicht
            if muenzindex==maxIndexMuenztypen:
                # wenn aktuelles Münzstück zulässig
                if munzeIstZulaessig(muenztypen[muenzindex]):





            if (munzeIstZulaessig(muenztypen[muenzindex], betrag) and muenzindex < maxIndexMuenztypen):
                teilloesung.append(muenztypen[muenzindex])
                betrag -= muenztypen[muenzindex]
                muenzindex+=1

            if (munzeIstZulaessig(muenztypen[muenzindex],betrag) and muenzindex==maxIndexMuenztypen):
                if betrag-muenztypen[muenzindex]==0:
                    betrag-=muenztypen[muenzindex]
                    teilloesung.append(muenztypen[muenzindex])
                    loesung.append(teilloesung)









    # while True:
    #     while True:
    #         if (munzeIstZulaessig(muenztypen[muenzindex],betrag) and muenzindex < maxIndexMuenztypen):
    #             loesung.append(muenztypen[muenzindex])
    #             betrag-=muenztypen[muenzindex]
    #             muenzindex+=1
    #
    #         elif (munzeIstZulaessig(muenztypen[muenzindex],betrag) and muenzindex==maxIndexMuenztypen):
    #             if betrag == 0:
    #                 return loesung
    #             if betrag >0:
    #                 betrag+=loesung[-1]
    #                 loesung.pop()
    #                 muenzindex-=1
    #         else:
    #             break
    #
    #
    #     if betrag > 0:
    #
    #         if muenzindex == maxIndexMuenztypen:
    #             betrag+=loesung[-1]
    #             loesung.pop()
    #             break
    #
    #         elif muenzindex < maxIndexMuenztypen:
    #             muenzindex+=1
    #
    #         else:
    #             muenzindex-=1
    #             break

# Ausprobieren der Funktion
kleingeld=[50,10,5,2,20,1]

print(wechseln(kleingeld,33))


