from abc import ABC, abstractmethod
from frame import Frame
import numpy as np

class Junta(ABC):
    def __init__(self, name=None, numGL=None, frame=None):
        self.name = "{0}" if name is None else name
        self.numGL = 0 if numGL is None else numGL
        self.frame = Frame() if frame is None else frame
    
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

    @abstractmethod
    def calcular_tMat(self, axis, valor):
        """Calcula e retorna a Matriz de Transformação Homogênea"""
        pass

class JuntaRevolucao(Junta):
    def __init__(self, name=None, numGL=None, frame=None, gl = None):
        super().__init__(name, numGL, frame)

    def calcular_tMat(self, axis, valor):
        valor = np.deg2rad(valor)
        if axis == "z":
             self.__tMat = np.array([[np.cos(valor), -np.sin(valor), 0, 0],
                                     [np.sin(valor), np.cos(valor), 0, 0],
                                     [0, 0, 1, 0],
                                     [0, 0, 0, 1]])
        elif axis == "y":
            self.__tMat = np.array([[np.cos(valor), 0, np.sin(valor), 0],
                                     [0, 1, 0, 0],
                                     [-np.sin(valor), 0, np.cos(valor), 0],
                                     [0, 0, 0, 1]])
        elif axis == "x":
            self.__tMat = np.array([[1, 0, 0, 0],
                                     [0, np.cos(valor), -np.sin(valor), 0],
                                     [0, np.sin(valor), np.cos(valor), 0],
                                     [0, 0, 0, 1]])
        
        return self.__tMat
    

        
class JuntaPrismatica(Junta):
    def __init__(self, name=None, numGL=None, frame=None, gl = None):
        super().__init__(name, numGL, frame)

    def calcular_tMat(self, axis, valor):
        # Começa com a matriz identidade 4x4
        self.__tMat = np.eye(4) 
        
        # Altera apenas a coluna de translação (índice 3) de acordo com o eixo
        if axis == "x":
            self.__tMat[0, 3] = valor
        elif axis == "y":
            self.__tMat[1, 3] = valor
        elif axis == "z":
            self.__tMat[2, 3] = valor
            
        return self.__tMat
