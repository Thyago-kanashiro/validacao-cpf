import unittest
import sys
import os

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Agora podemos importar a função de validação de CPF
from function.__init__ import validar_cpf

class TestValidacaoCPF(unittest.TestCase):
    def test_cpf_valido(self):
        self.assertTrue(validar_cpf("529.982.247-25"))  # CPF válido
        self.assertTrue(validar_cpf("52998224725"))     # CPF válido sem máscara

    def test_cpf_invalido(self):
        self.assertFalse(validar_cpf("123.456.789-09"))  # CPF inválido
        self.assertFalse(validar_cpf("111.111.111-11"))  # CPF com dígitos repetidos
        self.assertFalse(validar_cpf("123"))             # CPF com menos de 11 dígitos

    def test_cpf_com_mascara(self):
        self.assertTrue(validar_cpf("529.982.247-25"))   # CPF válido com máscara

if __name__ == "__main__":
    unittest.main()