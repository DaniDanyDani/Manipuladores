import numpy as np
from typing import Optional, List, Union

class Frame:
    def __init__(self, name: str, origin: Optional[Union[List[float], np.ndarray]] = None, rpy: Optional[Union[List[float], np.ndarray]] = None):
        if not isinstance(name, str):
            raise TypeError("Frame name must be a string.")

        self.name = name
        self.origin = np.array(origin, dtype=float) if origin is not None else np.zeros(3)
        self.rpy = np.array(rpy, dtype=float) if rpy is not None else np.zeros(3)

        if self.origin.shape != (3,):
            raise ValueError("Origin must be a 1D array or list of length 3: [x, y, z].")
        if self.rpy.shape != (3,):
            raise ValueError("RPY must be a 1D array or list of length 3: [roll, pitch, yaw].")

        self.matrix = self._build_matrix()

    def _build_matrix(self) -> np.ndarray:
        roll, pitch, yaw = self.rpy
        
        rx = np.array([
            [1, 0, 0], 
            [0, np.cos(roll), -np.sin(roll)], 
            [0, np.sin(roll), np.cos(roll)]
        ], dtype=float)
        
        ry = np.array([
            [np.cos(pitch), 0, np.sin(pitch)], 
            [0, 1, 0], 
            [-np.sin(pitch), 0, np.cos(pitch)]
        ], dtype=float)
        
        rz = np.array([
            [np.cos(yaw), -np.sin(yaw), 0], 
            [np.sin(yaw), np.cos(yaw), 0], 
            [0, 0, 1]
        ], dtype=float)
        
        rotation_matrix = rz @ ry @ rx 
        
        transformation_matrix = np.eye(4, dtype=float)
        transformation_matrix[0:3, 0:3] = rotation_matrix
        transformation_matrix[0:3, 3] = self.origin
        
        return transformation_matrix