# Bianca Wentzel
# Übungszettel 2, Informatik B
# Tests der Aufgabe 9

import unittest
from Aufgabe09_Wentzel import *

if __name__ == '__main__':
    unittest.main()

###########################################################################################################
#                           Test der Berechnung des Skalarprodukts (9a)                                   #
###########################################################################################################
# Es muss getestet werden: - es werden zwei leere Listen übergeben
#                          - es werden zwei Listen mit unterschiedlichen Dimensionen übergeben
#                          - es werden Listen mit Elementen übergeben, die keine int oder float sind
#                          - es werden zwei gültige Listen übergeben

class TestSkalarprodukt(unittest.TestCase):

    def test_leereListen(self):
        expected=0
        actual=Skalarprodukt([],[])
        self.assertEqual(actual,expected)

    def test_gueltigeListen(self):
        expected=3
        actual=Skalarprodukt([1,2,5],[2,3,-1])
        self.assertEqual(actual,expected)

    def test_unterschDimListen(self):
        with self.assertRaises(IndexError):
            Skalarprodukt([1,2,3],[2,3])

    def test_ungueltigesElementListen(self):
        with self.assertRaises(ValueError):
            Skalarprodukt([1,2,(4,3)],[4,5,'string'])

###########################################################################################################
#                   Test des Erstellens eines Histogramms für eine Zeichenkette                           #
###########################################################################################################
# Es muss getestet werden: - es wird keine Zeichenkette übergeben
#                          - es wird eine leere Zeichenkette übergeben
#                          - es wird eine gültige Zeichenkette übergeben

class TestHistogramm(unittest.TestCase):

    def test_leereZeichenkette(self):
        expected={}
        actual=Histogramm('')
        self.assertDictEqual(expected,actual)

    def test_keineZeichenkette(self):
        with self.assertRaises(TypeError):
            Histogramm(9258)

    def test_gueltigeZeichenkette(self):
        expected={'H':1,'a':1,'l':2,'o':1}
        actual=Histogramm('Hallo')
        self.assertDictEqual(expected,actual)

##########################################################################################################
#                               Test des Verkettens von Listen                                           #
##########################################################################################################
# Es muss getestet werden: - es wird keine Liste übergeben
#                          - es befinden sich keine Listen in der übergebenen Liste
#                          - es sind leere Listen enthalten
#                          - es wird eine gültige Liste mit enthaltenen Listen übergeben

class TestVerketten(unittest.TestCase):

    def test_keineListe(self):
        with self.assertRaises(TypeError):
            Verketten((4,3,6,(5,7)))

    def test_keineListenInListe(self):
        with self.assertRaises(TypeError):
            Verketten([1,2,3,'a'])

    def test_leereListen(self):
        expected=[]
        actual=Verketten([[],[],[]])
        self.assertEqual(actual, expected)

    def test_leereListe(self):
        expected = []
        actual = Verketten([])
        self.assertEqual(actual, expected)

    def test_gueltigeListe(self):
        expected=[1,2,2,[1,4],True]
        actual=Verketten([[1,2],[2,[1,4]],[True]])
        self.assertEqual(actual, expected)