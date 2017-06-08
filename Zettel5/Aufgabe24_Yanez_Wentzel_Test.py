# Zettel 5, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 24

from Aufgabe24_Yanez_Wentzel import *
import unittest

if __name__ == '__main__':
    unittest.main()

######################################################################################################################
#                                           Testen der Algorithmen aus Aufgabe 24                                    #
######################################################################################################################
class TestDiffNumbersLE10(unittest.TestCase):

    def test_ListeErfuelltAnforderung(self):
        beispielListe=[5,22,32,57]
        expected=True
        actual=diffNumbersLE10(beispielListe)
        self.assertEqual(expected,actual)

    def test_ListeErfuelltNichtAnforderun(self):
        beispielListe=[1,12,54]
        expected=False
        actual=diffNumbersLE10(beispielListe)
        self.assertEqual(expected,actual)

    def test_ListeLeer(self):
        beispielListe=[]
        expected=False
        actual=diffNumbersLE10(beispielListe)
        self.assertEqual(expected,actual)

    def test_ListeHatNurEinElement(self):
        beispielListe = [1]
        expected = False
        actual = diffNumbersLE10(beispielListe)
        self.assertEqual(expected, actual)
