import unittest
import numpy as np

from src.frame import Frame
from src.junta import JuntaRotacional

class TestJuntaRotacional(unittest.TestCase):
    def setUp(self):
        """Configuração inicial: cria um Frame base para associar às juntas nos testes."""
        self.frame_base = Frame(name="BaseFrame", origin=[0.0, 0.0, 0.0])

    def test_inicializacao_tipos_invalidos(self):
        """Testa se a classe levanta excepções ao receber parâmetros errados no construtor."""
        # Nome não é string
        with self.assertRaises(TypeError):
            JuntaRotacional(name=123, frame=self.frame_base)
            
        # Frame não é instância da classe Frame
        with self.assertRaises(TypeError):
            JuntaRotacional(name="Junta1", frame=[1, 0, 0])
            
        # Eixo inválido (diferente de 'x', 'y' ou 'z')
        with self.assertRaises(ValueError):
            JuntaRotacional(name="Junta1", frame=self.frame_base, axis='w')

    def test_aplicacao_valor_invalido(self):
        """Testa se a junta recusa valores de actuação que não sejam números."""
        junta = JuntaRotacional(name="J1", frame=self.frame_base, axis='z')
        
        with self.assertRaises(TypeError):
            junta.apply_actuation("90 graus")

    def test_rotacao_eixo_z(self):
        """Testa se a matriz gerada por uma rotação no eixo Z está correcta matematicamente."""
        junta = JuntaRotacional(name="J1_Z", frame=self.frame_base, axis='z')
        angulo_rad = np.pi / 2  # 90 graus
        
        matriz_resultante = junta.apply_actuation(angulo_rad)
        
        # Para +90 graus em Z: 
        # cos(90) = 0, sin(90) = 1
        # Primeira linha [0, 0] deve ser 0; [0, 1] deve ser -1
        self.assertAlmostEqual(matriz_resultante[0, 0], 0.0, places=5)
        self.assertAlmostEqual(matriz_resultante[0, 1], -1.0, places=5)
        # Segunda linha [1, 0] deve ser 1; [1, 1] deve ser 0
        self.assertAlmostEqual(matriz_resultante[1, 0], 1.0, places=5)
        self.assertAlmostEqual(matriz_resultante[1, 1], 0.0, places=5)

    def test_rotacao_com_deslocamento_previo(self):
        """Testa se a junta respeita o Frame original antes de aplicar a rotação do motor."""
        # Frame com deslocamento de 5 unidades em X
        frame_deslocado = Frame(name="F_Deslocado", origin=[5.0, 0.0, 0.0])
        junta = JuntaRotacional(name="J2", frame=frame_deslocado, axis='y')
        
        # Actuação de 0 graus (não roda, apenas mantém a posição estática)
        matriz_resultante = junta.apply_actuation(0.0)
        
        # Verifica se o X continua a ser 5.0 na última coluna da matriz
        self.assertEqual(matriz_resultante[0, 3], 5.0)
        self.assertEqual(matriz_resultante[1, 3], 0.0)
        self.assertEqual(matriz_resultante[2, 3], 0.0)

if __name__ == '__main__':
    unittest.main()