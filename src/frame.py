import numpy as np

class Frame:
    def __init__(self, origem=None, orientacao=None):
        self.origem = np.array([0.0, 0.0, 0.0]) if origem is None else origem
        self.orientacao = np.eye(3) if orientacao is None else orientacao
    
    @property
    def origem(self):
        """Retorna a origem"""
        return self.__origem
    @origem.setter
    def origem(self, valor):
        """Define a origem"""
        self.__origem = np.array(valor)

    @property
    def orientacao(self):
        """Retorna a orientação"""
        return self.__orientacao
    @orientacao.setter
    def orientacao(self, matriz):
        """Garante que a matriz de rotação seja ortonormal"""
        matriz = np.array(matriz)
        
        x_norm = matriz[0] / np.linalg.norm(matriz[0])
        y_norm = matriz[1] / np.linalg.norm(matriz[1])
        z_norm = matriz[2] / np.linalg.norm(matriz[2])

        self.__orientacao = np.array([x_norm, y_norm, z_norm])