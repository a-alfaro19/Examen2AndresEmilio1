import unittest
from Examen2 import MiClase

class TestMiClaseMethods(unittest.TestCase):

    def setUp(self):
        #Creation of the object to use the clases and make the unittesting
        self.objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])

    def test_ObtieneValencia(self):
        #Test of ObtieneValencia method
        self.assertEqual(self.objeto.ObtieneValencia(1234567), 4)
        self.assertEqual(self.objeto.ObtieneValencia(894598765432), 6)

    def test_DivisibleTempo(self):
        #Test of DivisibleTempo method
        self.assertEqual(self.objeto.DivisibleTempo(10), [1, 2, 5, 10])
        self.assertEqual(self.objeto.DivisibleTempo(35), [1, 5, 7, 35])

    def test_ObtieneMasBailable(self):
        #Test of ObtieneMasBailable method
        self.assertEqual(self.objeto.ObtieneMasBailable([0.8, 0.9, 0.7]), 0.9)
        self.assertEqual(self.objeto.ObtieneMasBailable([0.3, 0.10, 0.79]), 0.79)

    def test_VerificaListaCanciones(self):
        #Test of VerificaListaCanciones method
        self.assertEqual(self.objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]), True)
        self.assertEqual(self.objeto.VerificaListaCanciones(["Canción 1", "Canción 2", None]), False)

if __name__ == '__main__':
    unittest.main()
