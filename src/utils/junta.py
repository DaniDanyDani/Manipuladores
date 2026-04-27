from abc import ABC, abstractmethod
from frame import NumericalFrame, SymbolicFrame
from utils import transformMatrix

class Junta(ABC):
    def __init__(self, juntaName=None, juntaAxis="z", juntaOrigin=None, frameAxis=None, sensorJunta=None) -> None:
        self._juntaName = juntaName if juntaName is not None else "Junta"
        self._juntaAxis = juntaAxis.lower()
        self._sensorJunta = sensorJunta
        self._juntaFrame = self._initFrame(juntaOrigin, frameAxis)

    @abstractmethod
    def _initFrame(self, origin, axis):
        pass

    @abstractmethod
    def applyJunta(self, q):
        """Aplica o movimento da junta dado um valor 'q' (distância ou ângulo)"""
        pass

    @property
    def juntaName(self):
        return self._juntaName
    
    @property
    def juntaFrame(self):
        return self._juntaFrame


# ABSTRAÇÕES DE DOMÍNIO

class NumericalJunta(Junta):
    def _initFrame(self, origin, axis):
        return NumericalFrame(self._juntaName, frameOrigin=origin, frameAxis=axis)

class SymbolicJunta(Junta):
    def _initFrame(self, origin, axis):
        return SymbolicFrame(self._juntaName, frameOrigin=origin, frameAxis=axis)


# IMPLEMENTAÇÕES

class NumericalJuntaRevolucional(NumericalJunta):
    def applyJunta(self, theta):
        """Cria matriz de rotação com o ângulo theta e aplica ao frame da junta"""
        tH = transformMatrix("r", self._juntaAxis, theta)
        return self._juntaFrame.transform(tH)

class NumericalJuntaPrismatica(NumericalJunta):
    def applyJunta(self, d):
        """Cria matriz de translação com a distância d e aplica ao frame da junta"""
        tH = transformMatrix("t", self._juntaAxis, d)
        return self._juntaFrame.transform(tH)

class SymbolicJuntaRevolucional(SymbolicJunta):
    def applyJunta(self, theta_sym):
        tH = transformMatrix("r", self._juntaAxis, theta_sym)
        return self._juntaFrame.transform(tH)

class SymbolicJuntaPrismatica(SymbolicJunta):
    def applyJunta(self, d_sym):
        tH = transformMatrix("t", self._juntaAxis, d_sym)
        return self._juntaFrame.transform(tH)

if __name__ == "__main__":
    import sympy as sp
    import numpy as np
    
    print("--- Teste Numérico (Prismática) ---")
    # Junta prismática no eixo Z, na origem (0,0,0)
    j1 = NumericalJuntaPrismatica("J1_Prismatica", juntaAxis="z", juntaOrigin=[0,0,0])
    
    # Move a junta em 5 unidades
    frame_resultante = j1.applyJunta(5)
    
    print("Frame Original (Inalterado):")
    print(j1.juntaFrame)
    print("Frame Movido:")
    print(frame_resultante)

    print("\n--- Teste Simbólico (Revolucional) ---")
    q1 = sp.symbols('q1')
    j2 = SymbolicJuntaRevolucional("J2_Revolucional", juntaAxis="z")
    frame_sym_resultante = j2.applyJunta(q1)
    sp.pprint(frame_sym_resultante.frame)
    print("\n--- Teste Simbólico (Revolucional) Substituindo valor ---")
    sp.pprint(frame_sym_resultante.frame.subs({q1: sp.pi/2}).evalf())