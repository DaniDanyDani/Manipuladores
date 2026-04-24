import unittest
import numpy as np

# Importando do seu pacote src
from src.frame import Frame

class TestFrame(unittest.TestCase):
    def test_frame_default_initialization(self):
        """Testa se o frame base inicializa com a matriz Identidade 4x4"""
        f = Frame(name="Base")
        self.assertEqual(f.name, "Base")
        np.testing.assert_array_equal(f.origin, np.zeros(3))
        np.testing.assert_array_equal(f.matrix, np.eye(4))

    def test_frame_translation(self):
        """Testa se a matriz 4x4 aloca a translação corretamente"""
        origem = [10.0, -5.0, 3.0]
        f = Frame(name="Deslocado", origin=origem)
        self.assertEqual(f.matrix[0, 3], 10.0)
        self.assertEqual(f.matrix[1, 3], -5.0)
        self.assertEqual(f.matrix[2, 3],  3.0)

    def test_frame_rotation_z(self):
        """Testa se o RPY no eixo Z gera a rotação correta"""
        f = Frame(name="Rot_Z", rpy=[0, 0, np.pi/2]) # 90 graus em Z
        
        # O cosseno de 90 é 0 e o seno é 1
        np.testing.assert_almost_equal(f.matrix[0, 0], 0.0)
        np.testing.assert_almost_equal(f.matrix[1, 0], 1.0)
        np.testing.assert_almost_equal(f.matrix[0, 1], -1.0)

if __name__ == '__main__':
    unittest.main()