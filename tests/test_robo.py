import unittest
import numpy as np

from src.frame import Frame
from src.junta import JuntaRotacional
from src.robo import RoboArticulado

class TestRoboPlanarEnade(unittest.TestCase):
    def setUp(self):
        """Configuração inicial executada antes de cada teste"""
        f1 = Frame("F1", origin=[0, 0, 0])
        f2 = Frame("F2", origin=[0.3, 0, 0])
        f3 = Frame("F3", origin=[0.3, 0, 0])
        f_garra = Frame("F_Garra", origin=[0.3, 0, 0])

        j1 = JuntaRotacional("J1", f1, axis='z')
        j2 = JuntaRotacional("J2", f2, axis='z')
        j3 = JuntaRotacional("J3", f3, axis='z')
        j_garra = JuntaRotacional("JG", f_garra, axis='z')

        self.robo = RoboArticulado("Planar_3R", [j1, j2, j3, j_garra])

    def test_cinematica_direta_questao_enade(self):
        """Testa a cinemática direta simulando a questão do Enade"""
        
        # Angulos da questão (Horário, Anti-Horário, Horário)
        valores = [-np.pi/2, np.pi/2, -np.pi/2, 0.0]
        
        matrizes = self.robo.forward_kinematics(valores)
        matriz_final = matrizes[-1]
        
        x_final = matriz_final[0, 3]
        y_final = matriz_final[1, 3]
        phi_rad = np.arctan2(matriz_final[1, 0], matriz_final[0, 0])
        phi_deg = np.rad2deg(phi_rad)
        
        # Usamos assertAlmostEqual por causa de precisão de ponto flutuante (ex: 0.0000000000001)
        self.assertAlmostEqual(x_final, 0.3, places=2, msg="O X final deveria ser 0.3m")
        self.assertAlmostEqual(y_final, -0.6, places=2, msg="O Y final deveria ser -0.6m")
        self.assertAlmostEqual(phi_deg, -90.0, places=1, msg="A orientação deveria ser -90 graus")

if __name__ == '__main__':
    unittest.main()