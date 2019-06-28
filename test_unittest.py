import service    # The code to test
import unittest   # The test framework

class Test_TestService(unittest.TestCase):

    # def test_deve_retornar_2_quando_informar_1_e_1(self):
    #     self.assertEqual(service.soma(1, 1), 2)

    def test_deve_retornar2_quando_o_numero_for_1(self):
        self.assertEqual(service.quantidade_caracter('um'), 2)

    def test_calcula_tamanho_para_5_sendo_21(self):
        self.assertEqual(service.calcula_tamanho(5), 21)

    def test_retorna_string_numero(self):
        self.assertEqual(service.retorna_string_numero(4), 'quatro')

    def test_calcula_tamanho_para_1_sendo_2(self):
        self.assertEqual(service.calcula_tamanho(1), 2)

    def test_calcula_tamanho_para_2_sendo_6(self):
        self.assertEqual(service.calcula_tamanho(2), 6)

    def test_calcula_tamanho_para_9_sendo_37(self):
        self.assertEqual(service.calcula_tamanho(9), 37)

    def test_calcula_tamanho_para_19_sendo_100(self):
        self.assertEqual(service.calcula_tamanho(19), 100)

    def test_calcula_tamanho_para_20_sendo_105(self):
        self.assertEqual(service.calcula_tamanho(20), 105)

    def test_calcula_tamanho_para_21_sendo_113(self):
        self.assertEqual(service.calcula_tamanho(21), 113)

    def test_calcula_tamanho_para_30_sendo_202(self):
        self.assertEqual(service.calcula_tamanho(30), 202)

if __name__ == '__main__':
    unittest.main()