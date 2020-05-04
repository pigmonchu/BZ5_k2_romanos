import unittest

import romanos

class RomanNumberTest(unittest.TestCase):

    def test_symbols_romans(self):
        self.assertEqual(romanos.romano_a_entero('I'), 1)
        self.assertEqual(romanos.romano_a_entero('V'), 5)
        self.assertEqual(romanos.romano_a_entero('X'), 10)
        self.assertEqual(romanos.romano_a_entero('L'), 50)
        self.assertEqual(romanos.romano_a_entero('C'), 100)
        self.assertEqual(romanos.romano_a_entero('D'), 500)
        self.assertEqual(romanos.romano_a_entero('M'), 1000)
        self.assertEqual(romanos.romano_a_entero('K'), 'Error en formato')

        self.assertEqual(romanos.romano_a_entero(''), 'Error en formato')

    def test_repetitions(self):
        self.assertEqual(romanos.romano_a_entero('II'), 2)
        self.assertEqual(romanos.romano_a_entero('MMM'), 3000)
        self.assertEqual(romanos.romano_a_entero('KKK'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('MK'), 'Error en formato')

    def test_only_three(self):
        self.assertEqual(romanos.romano_a_entero('IIII'), 'Error en formato')

    def test_digitos_decrecientes(self):
        self.assertEqual(romanos.romano_a_entero('XVIII'), 18)
        self.assertEqual(romanos.romano_a_entero('XI'), 11)
        self.assertEqual(romanos.romano_a_entero('XV'), 15)
        self.assertEqual(romanos.romano_a_entero('XX'), 20)
        self.assertEqual(romanos.romano_a_entero('CI'), 101)

    def test_digitos_restan(self):
        self.assertEqual(romanos.romano_a_entero('XIX'), 19)

    def test_resta_separacion_un_grado(self):
        self.assertEqual(romanos.romano_a_entero('XC'), 90)
        self.assertEqual(romanos.romano_a_entero('XD'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('IL'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('XM'), 'Error en formato')

    def test_resta_de_multiplos_5_NO(self):
        self.assertEqual(romanos.romano_a_entero('VC'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('XCV'), 95)

    def test_resta_un_solo_simbolo(self):
        self.assertEqual(romanos.romano_a_entero('XXL'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('IXL'), 'Error en formato')
        self.assertEqual(romanos.romano_a_entero('XXX'), 30)

if __name__ == '__main__':
    unittest.main()
        