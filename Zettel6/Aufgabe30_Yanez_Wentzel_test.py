from Aufgabe30_Yanez_Wentzel import *
import unittest

if __name__ == '__main__':
    unittest.main()

######################################################################################################################
#                                   Testen des Schreibens eines Elements in einen Heap                               #
######################################################################################################################

class TestschreibeElementInHeap(unittest.TestCase):

    def test_fuegeElementInLeerenHeapEin(self):
        expected=[1]
        actual=schreibeElementInHeap([],1)
        self.assertListEqual(expected,actual)

    def test_fuegeDreiZumHeapHinzu(self):
        expected=[1,2,3,5,7,4]
        actual=schreibeElementInHeap([1,2,4,5,7],3)
        self.assertListEqual(expected,actual)

class TestentferneElementAusHeap(unittest.TestCase):

    def test_EntferneEinsAusHeap(self):
        expected=[2,5,3,6,7,4]
        actual=entferneElementAusHeap([1,2,3,5,7,4,6])[0]
        self.assertListEqual(expected,actual)






