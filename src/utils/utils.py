import numpy as np
import sympy as sp

def transformMatrix(tType, axis, value):
    """
    Gera uma matriz de transformação homogênea 4x4 detectando o tipo automaticamente.
    
    Args:
        tType (str): "r" para rotação ou "t" para translação.
        axis (str): "x", "y" ou "z".
        value: Valor numérico (int, float, np.float) ou simbólico (sp.Symbol, sp.Expr).
    """
    if isinstance(value, (sp.Basic, sp.Expr)):
        T = sp.eye(4)
        cos_v, sin_v = sp.cos(value), sp.sin(value)
    else:
        T = np.eye(4)
        cos_v, sin_v = np.cos(value), np.sin(value)

    axis = axis.lower()

    # --- Lógica de Translação ---
    if tType == "t":
        idx = {'x': 0, 'y': 1, 'z': 2}[axis]
        T[idx, 3] = value

    # --- Lógica de Rotação ---
    elif tType == "r":
        if axis == "x":
            T[1:3, 1:3] = [[cos_v, -sin_v], 
                           [sin_v,  cos_v]]
        elif axis == "y":
            T[0, 0], T[0, 2] = cos_v, sin_v
            T[2, 0], T[2, 2] = -sin_v, cos_v
        elif axis == "z":
            T[0:2, 0:2] = [[cos_v, -sin_v], 
                           [sin_v,  cos_v]]
    else:
        raise ValueError("tType deve ser 'r' (rotação) ou 't' (translação)")

    return T