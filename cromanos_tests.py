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


if __name__ == '__main__':
    unittest.main()
