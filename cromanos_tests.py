import unittest

import cromanos

class RomanNumberTest(unittest.TestCase):
    def test_symbols_romans(self):
        
        nr = cromanos.RomanNumber()

        self.assertEqual(nr.romano_a_entero('I'), 1)
        self.assertEqual(nr.romano_a_entero('V'), 5)
        self.assertEqual(nr.romano_a_entero('X'), 10)
        self.assertEqual(nr.romano_a_entero('L'), 50)
        self.assertEqual(nr.romano_a_entero('C'), 100)
        self.assertEqual(nr.romano_a_entero('D'), 500)
        self.assertEqual(nr.romano_a_entero('M'), 1000)
        self.assertEqual(nr.romano_a_entero('K'), 'Error en formato')

        self.assertEqual(nr.romano_a_entero(''), 'Error en formato')

if __name__ == '__main__':
    unittest.main()
