from abc import ABC, abstractmethod
import numpy as np
from src.frame import Frame

class Junta(ABC):
    def __init__(self, name: str, frame: Frame, axis: str = 'z'):
        if not isinstance(name, str):
            raise TypeError("Joint name must be a string.")
        if not isinstance(frame, Frame):
            raise TypeError("frame must be an instance of the Frame class.")
        if axis not in ['x', 'y', 'z']:
            raise ValueError("Actuation axis must be 'x', 'y', or 'z'.")

        self.name = name
        self.frame = frame
        self.axis = axis

    def apply_actuation(self, value: float) -> np.ndarray:
        if not isinstance(value, (int, float, np.number)):
            raise TypeError("Actuation value must be a numeric type (int or float).")
            
        return self.frame.matrix @ self._calc_actuation_matrix(float(value))

    @abstractmethod
    def _calc_actuation_matrix(self, value: float) -> np.ndarray:
        pass


class JuntaRotacional(Junta):
    def _calc_actuation_matrix(self, angle: float) -> np.ndarray:
        transformation_matrix = np.eye(4, dtype=float)
        cos_q = np.cos(angle)
        sin_q = np.sin(angle)
        
        if self.axis == 'z':
            transformation_matrix[0:2, 0:2] = [[cos_q, -sin_q], [sin_q, cos_q]]
        elif self.axis == 'y':
            transformation_matrix[0:3:2, 0:3:2] = [[cos_q, sin_q], [-sin_q, cos_q]]
        elif self.axis == 'x':
            transformation_matrix[1:3, 1:3] = [[1, 0], [0, 1]] # Mantém X intocado
            transformation_matrix[1:3, 1:3] = [[cos_q, -sin_q], [sin_q, cos_q]]
            
        return transformation_matrix