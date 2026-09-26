# test_saldo.py
import unittest
from saldo import consultar_saldo

class TestConsultaSaldo(unittest.TestCase):

    # Caso 1: Cuenta con saldo existente
    def test_consultar_saldo_cuenta_valida(self):
        saldo = consultar_saldo("1234567890")
        self.assertEqual(saldo, 2000.00)

    # Caso 2: Cuenta que no existe
    def test_consultar_saldo_cuenta_no_existente(self):
        saldo = consultar_saldo("0000000000")
        self.assertEqual(saldo, 0.00)

    # Caso 3: Manejo de error cuando la cuenta es invalida (ej. menos de 10 digitos)
    def test_consultar_saldo_cuenta_invalida_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            consultar_saldo("123")

if __name__ == '__main__':
    unittest.main()