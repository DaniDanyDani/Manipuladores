import numpy as np

class Frame:
    def __init__(self, T: np.ndarray, index: int = None):
        """
        T: matriz homogênea 4x4
        """
        self.T = T
        self.index = index

    @classmethod
    def from_rt(cls, R: np.ndarray, t: np.ndarray, index=None):
        T = np.eye(4)
        T[:3, :3] = R
        T[:3, 3] = t
        return cls(T, index)

    def inv(self):
        return Frame(np.linalg.inv(self.T), self.index)

    def __matmul__(self, other):
        return Frame(self.T @ other.T)

    def __repr__(self):
        return f"Frame(index={self.index})"