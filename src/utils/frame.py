import numpy as np
import sympy as sp
from abc import ABC, abstractmethod
from utils import transformMatrix

class Frame(ABC):
    def __init__(self, frameName=None, frameOrigin=None, frameAxis=None) -> None:
        self._frameName = frameName if frameName is not None else "Frame_0"
        self._frameMatrix = self.Tmatrix() 
        
        if frameAxis is not None:
            self._frameMatrix[0:3, 0:3] = frameAxis 
        if frameOrigin is not None:
            self._frameMatrix[0:3, 3] = frameOrigin 

    @property
    def frame(self):
        return self._frameMatrix

    @property
    def name(self):
        return self._frameName

    @abstractmethod
    def Tmatrix(self):
        pass

    @abstractmethod
    def transform(self, matrix_h):
        """Aplica a transformação"""
        pass

    def __repr__(self):
        return f"--- {self._frameName} ---\n{self._frameMatrix}\n"

class NumericalFrame(Frame):
    def Tmatrix(self):
        return np.eye(4)
    
    def transform(self, matrix_h):
        novo_frame = NumericalFrame(self._frameName + "_transf")
        novo_frame._frameMatrix = self._frameMatrix @ matrix_h
        return novo_frame

class SymbolicFrame(Frame):
    def Tmatrix(self):
        return sp.eye(4)
    
    def transform(self, matrix_h):
        novo_frame = SymbolicFrame(self._frameName + "_transf")
        novo_frame._frameMatrix = self._frameMatrix * matrix_h
        return novo_frame