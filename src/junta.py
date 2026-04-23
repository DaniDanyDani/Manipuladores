from abc import ABC, abstractmethod
from frame import Frame
import numpy as np

class Junta(ABC):
    # Adicionamos o 'axis="z"' como padrão no __init__
    def __init__(self, name=None, numGL=None, frame=None, axis="z"):
        self.name = "{0}" if name is None else name
        self.numGL = 0 if numGL is None else numGL
        self.frame = Frame() if frame is None else frame
        self.axis = axis
    
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, valor):
        self.__name = valor

    @property
    def numGL(self):
        return self.__numGL
        
    @numGL.setter
    def numGL(self, valor):
        self.__numGL = valor

    @property
    def frame(self):
        return self.__frame
        
    @frame.setter
    def frame(self, valor):
        self.__frame = valor if isinstance(valor, Frame) else Frame()
    
    @property
    def axis(self):
        return self.__axis
        
    @axis.setter
    def axis(self, valor):
        valor = str(valor).lower()
        if valor not in ["x", "y", "z"]:
            raise ValueError("O eixo deve ser 'x', 'y' ou 'z'.")
        self.__axis = valor

    @abstractmethod
    # Removemos o parâmetro 'axis' daqui!
    def calcular_tMat(self, valor): 
        """Calcula e retorna a Matriz de Transformação Homogênea"""
        pass


class JuntaRevolucao(Junta):
    def __init__(self, name=None, numGL=None, frame=None, gl=None, axis="z"):
        super().__init__(name, numGL, frame, axis)

    def calcular_tMat(self, valor):
        valor = np.deg2rad(valor)
        if self.axis == "z":
             self.__tMat = np.array([[np.cos(valor), -np.sin(valor), 0, 0],
                                     [np.sin(valor), np.cos(valor), 0, 0],
                                     [0, 0, 1, 0],
                                     [0, 0, 0, 1]])
        elif self.axis == "y":
            self.__tMat = np.array([[np.cos(valor), 0, np.sin(valor), 0],
                                     [0, 1, 0, 0],
                                     [-np.sin(valor), 0, np.cos(valor), 0],
                                     [0, 0, 0, 1]])
        elif self.axis == "x":
            self.__tMat = np.array([[1, 0, 0, 0],
                                     [0, np.cos(valor), -np.sin(valor), 0],
                                     [0, np.sin(valor), np.cos(valor), 0],
                                     [0, 0, 0, 1]])
        
        return self.__tMat
    

        
class JuntaPrismatica(Junta):
    def __init__(self, name=None, numGL=None, frame=None, gl=None, axis="z"):
        super().__init__(name, numGL, frame, axis)

    def calcular_tMat(self, valor):
        self.__tMat = np.eye(4) 
        
        # Trocamos 'axis' por 'self.axis'
        if self.axis == "x":
            self.__tMat[0, 3] = valor
        elif self.axis == "y":
            self.__tMat[1, 3] = valor
        elif self.axis == "z":
            self.__tMat[2, 3] = valor
            
        return self.__tMat