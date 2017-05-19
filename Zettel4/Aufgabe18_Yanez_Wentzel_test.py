
import unittest
from Aufgabe18_Yanez_Wentzel import *

if __name__ == '__main__':
    unittest.main()

class TestEinzelExperiment(unittest.TestCase):

    # Die Funktion erzeugt uns eine Funktion randint, die nach und nach alle Zahlen der gegebenen Liste ausgibt
    # und uns somit eine vorhersehbare und vor allem prüfbare "random"-Zahl liefert, um unsere Test auszuführen
    def erzeugeRandintFunktion(self,liste):
        neuerIterator=iter(liste)

        def randint(start,ende):
            return next(neuerIterator)
        return randint

    # Best Case, man benötigt jeweils nur pro Zahl nur einen Versuch
    def test_randomBestCase(self):
        expected=10
        actual=einzelExperiment(10,self.erzeugeRandintFunktion(range(1,11)))
        self.assertEqual(expected,actual[1])



