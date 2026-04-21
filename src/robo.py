from abc import ABC, abstractmethod
from junta import Junta
import numpy as np

class Robo(ABC):
    def __init__(self, numJuntas, numLinks):
        self.setNumJuntas(numJuntas)
        self.setNumLinks(numLinks)
    
    def setNumJuntas(self, numJuntas):
        self.__numJuntas = numJuntas
    def setNumLinks(self, numLinks):
        self.__numLinks = numLinks
        
    def getNumJuntas(self):
        return self.__numJuntas
    def getNumLinks(self):
        return self.__numLinks
    
    @abstractmethod
    def calcular_cinematica_direta(self, valores_das_juntas):
        pass

class RoboArticulado(Robo):
    def __init__(self, nome, lista_de_juntas):
        # Em vez de apenas passar o número de juntas, passamos as instâncias delas!
        super().__init__(len(lista_de_juntas), len(lista_de_juntas))
        self.nome = nome
        self.juntas = lista_de_juntas

    # ESTE É O MÉTODO QUE A SUA SIMULAÇÃO VAI CHAMAR!
    def calcular_cinematica_direta(self, valores_das_juntas):
        """
        Recebe uma lista de ângulos/deslocamentos e retorna a posição (X, Y, Z) da ponta do robô.
        """
        if len(valores_das_juntas) != len(self.juntas):
            raise ValueError("A quantidade de ângulos fornecida não bate com o número de juntas do robô.")

        # Começamos com a Matriz Identidade 4x4 (Frame Global/Base do robô)
        T_total = np.eye(4)

        # Multiplicamos as matrizes em cadeia: T01 * T12 * T23 ...
        for junta, valor in zip(self.juntas, valores_das_juntas):
            # Assumindo que você renomeou o método para calcular_tMat como conversamos antes
            T_atual = junta.calcular_tMat("z", valor) 
            
            # Multiplicação de matrizes no Numpy é feita com @
            T_total = T_total @ T_atual

        # A posição final X, Y e Z fica armazenada na última coluna (índice 3) das 3 primeiras linhas
        posicao_x = T_total[0, 3]
        posicao_y = T_total[1, 3]
        posicao_z = T_total[2, 3]

        return np.array([posicao_x, posicao_y, posicao_z])


class RoboCartesiano(Robo):
    def __init__(self, numJuntas, numLinks):
        super().__init__(numJuntas, numLinks)


class RoboEsferico(Robo):
    def __init__(self, numJuntas, numLinks):
        super().__init__(numJuntas, numLinks)


class RoboCilindrico(Robo):
    def __init__(self, numJuntas, numLinks):
        super().__init__(numJuntas, numLinks)


class RoboSCARA(Robo):
    def __init__(self, numJuntas, numLinks):
        super().__init__(numJuntas, numLinks)

