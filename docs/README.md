# Transformações Homogêneas
## Translação
$$
\begin{bmatrix}
x_{i+1}\\
y_{i+1}\\
z_{i+1}\\
1
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 0 & dx\\
0 & 1 & 0 & dy\\
0 & 0 & 1 & dz\\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x_{i}\\
y_{i}\\
z_{i}\\
1
\end{bmatrix}
$$

## Rotação
### Yaw
$$
\begin{bmatrix}
x_{i+1}\\
y_{i+1}\\
z_{i+1}\\
1
\end{bmatrix}
=
\begin{bmatrix}
\cos(\alpha) & -\sin(\alpha) & 0 & 0 \\ 
\sin(\alpha) & \cos(\alpha)  & 0 & 0 \\ 
0            & 0             & 1 & 0 \\ 
0            & 0             & 0 & 1 
\end{bmatrix}
\begin{bmatrix}
x_{i}\\
y_{i}\\
z_{i}\\
1
\end{bmatrix}
$$

### Roll
$$
\begin{bmatrix}
x_{i+1}\\
y_{i+1}\\
z_{i+1}\\
1
\end{bmatrix}
=
\begin{bmatrix}
1 & 0            & 0             & 0 \\
0 & \cos(\gamma) & -\sin(\gamma) & 0 \\ 
0 & \sin(\gamma) & \cos(\gamma)  & 0 \\ 
0 & 0            & 0             & 1
\end{bmatrix}
\begin{bmatrix}
x_{i}\\
y_{i}\\
z_{i}\\
1
\end{bmatrix}
$$

### Pitch
$$
\begin{bmatrix}
x_{i+1}\\
y_{i+1}\\
z_{i+1}\\
1
\end{bmatrix}
=
\begin{bmatrix}
\cos(\beta)  & 0 & \sin(\beta) & 0 \\ 
0            & 1 & 0           & 0 \\ 
-\sin(\beta) & 0 & \cos(\beta) & 0 \\ 
0            & 0 & 0           & 1 
\end{bmatrix}
\begin{bmatrix}
x_{i}\\
y_{i}\\
z_{i}\\
1
\end{bmatrix}
$$

# Robô
## Base
-> Região estática

## Junta
-> Adiciona graus de liberdade

## Link
-> Une duas Juntas

## Atuador
-> Região de interesse do robô
