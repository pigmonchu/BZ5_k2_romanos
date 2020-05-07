import unittest

import cromanos

class RomanNumberTest(unittest.TestCase):
    def test_crea_romano(self):
        nr = cromanos.RomanNumber(25)
        self.assertEqual(nr.value, 25)
        self.assertEqual(nr.rvalue, 'XXV')

        snr = cromanos.RomanNumber('XXIV')
        self.assertEqual(snr.value, 24)
        self.assertEqual(snr.rvalue, 'XXIV')

        tnr = cromanos.RomanNumber('XXXX')
        self.assertEqual(tnr.value, 'Error en formato')
        self.assertEqual(tnr.rvalue, 'Error en formato')

        cnr = cromanos.RomanNumber(0)
        self.assertEqual(cnr.value, 'Overflow')
        self.assertEqual(cnr.rvalue, 'Overflow')

        qnr = cromanos.RomanNumber(4000)
        self.assertEqual(qnr.value, "Overflow")
        self.assertEqual(qnr.rvalue, "Overflow")

    def test_representation(self):
        nr = cromanos.RomanNumber(25)
        self.assertEqual(str(nr), 'XXV')
        #self.assertEqual(nr, 'XXV')

    def test_equal_romans(self):
        nr1 = cromanos.RomanNumber(25)
        nr2 = cromanos.RomanNumber('XXV')
        self.assertEqual(nr1, nr2)

    def test_add_roman(self):
        nr1 = cromanos.RomanNumber(1)
        nr2 = cromanos.RomanNumber('XXIV')
        nr3 = nr1+nr2 
        self.assertEqual(nr1+nr2, cromanos.RomanNumber(25))
        self.assertEqual(nr3.value, 25)
        self.assertTrue(isinstance(nr3, cromanos.RomanNumber))

    def test_add_integer(self):
        nr1 = cromanos.RomanNumber('XXIII')
        nr3 = nr1 + 1
        self.assertEqual(nr3.value, 24)
        self.assertTrue(isinstance(nr3, cromanos.RomanNumber))

        nr2 = 1 + nr1
        self.assertEqual(nr2.value, 24)
        self.assertTrue(isinstance(nr2, cromanos.RomanNumber))


if __name__ == '__main__':
    unittest.main()
