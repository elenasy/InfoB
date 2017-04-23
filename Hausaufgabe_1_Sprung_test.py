# Testen

# Importieren benötigter Pakete
import unittest
from Hausaufgabe_1_Sprung import find_knots,step_length

class Hausaufgaben_Test(unittest.TestCase):
    # Methode zum Testen des Findens von Knotenpunkten
    def test_find_knots(self):
        expected=[(1,2),(3,2),(4,3),(4,5),(3,6),(1,6)]
        actual=find_knots((2,4))
        self.assertListEqual(sorted(expected),sorted(actual))

    # Methode zum Testen der Bestimmung der Weglänge
    def test_step_length(self):
        expected=1
        actual=step_length((1,1))
        self.assertEqual(expected,actual)

    def test_step_length_2(self):
        expected=2
        actual=step_length((6,3))
        self.assertEqual(expected,actual)

    def test_step_length_0(self):
        expected=0
        actual=step_length((2,3))
        self.assertEqual(expected,actual)

# Alles wird ausgeführt, wenn ide Datei direkt gestartet wird
if __name__ == '__main__':
    unittest.main()