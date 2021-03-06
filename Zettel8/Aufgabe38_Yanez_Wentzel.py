# Aufgabenzettel 8, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 38

######################################################################################################################
#                                                  Aufgabe 38: Halde                                                 #
######################################################################################################################

class Halde:
    def __init__(self):
        self.schl = [None] # Element 0 wird nicht verwendet
        self.werte= [None]
        self.inHalde = {}
        self.n = 0

    def vertausche(self,i,j):
        self.schl[i],self.schl[j] = self.schl[j],self.schl[i]
        w1,w2 = self.werte[j],self.werte[i]
        self.werte[i],self.werte[j] = w1,w2
        self.inHalde[w1],self.inHalde[w2] = i,j

    def einfügen(self,zustand,schlüssel):
        self.n += 1
        if self.n>=len(self.schl):
            self.schl.append(schlüssel)
            self.werte.append(zustand)
        else:
            self.schl[self.n] = schlüssel
            self.werte[self.n] = zustand
        self.inHalde[zustand] = self.n
        self.zuklein(self.n)

    def entferneMin(self):
        if self.n==0: raise ValueError
        self.vertausche(1,self.n)
        self.n -= 1
        self.zugroß(1)
        return self.werte[self.n+1], self.schl[self.n+1]

    def Schlüsselverkleinern(self,zustand,schlüssel):
        i = self.inHalde[zustand]
        self.schl[i] = schlüssel
        self.zuklein(i)

    def zugroß(self,i):
        "Element a[i] der Halde a[1..n] ist eventuell zu groß."
        kind1 = 2*i
        kind2 = 2*i+1
        if kind1>self.n: return
        if kind2>self.n:
            kind = kind1
        else:
            if self.schl[kind1]<self.schl[kind2]:
                kind=kind1
            else:
                kind=kind2
        if self.schl[i]>self.schl[kind]:
            self.vertausche(kind,i)
            self.zugroß(kind)

    def zuklein(self,i):
        "Element a[i] der Halde ist eventuell zu klein."
        if i==1: return
        eltern = i//2
        if self.schl[eltern]>self.schl[i]:
            self.vertausche(eltern,i)
            self.zuklein(eltern)

    def Anzahl_kleiner(self,k):
        self.keysLower=[]
        self.allKeys=self.inHalde.values()
        for schluessel in self.allKeys:
            if schluessel < k:
                self.keysLower.append(schluessel)

        print("Anzahl der Schlüssel kleiner als ",k,":",len(self.keysLower))
