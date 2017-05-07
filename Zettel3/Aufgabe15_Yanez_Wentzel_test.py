# Testen der Aufagbe 15
# Zettel3, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel

import unittest
from Aufgabe15_Yanez_Wentzel import *

if __name__ == '__main__':
    unittest.main()

class TestVerfolger(unittest.TestCase):

    def test_verfolge(self):
        # Erzeugen eines Zielschildkrötenobjekts
        ziel = Turtle()
        ziel.setposition(5, 5)

        t = Verfolger(ziel)
        t.verfolge(1)

        expected=(0.71,0.71)
        actual=t.position()
        self.assertAlmostEqual(expected,actual,2)