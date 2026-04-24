import sys
import os
import numpy as np

# Configurando o path para encontrar a pasta 'src'
caminho_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if caminho_raiz not in sys.path:
    sys.path.append(caminho_raiz)

from src.frame import Frame
from src.junta import JuntaRotacional
from src.robo import RoboArticulado

# =======================================================
# 1. CONFIGURAÇÃO DOS FRAMES (Estrutura Física)
# =======================================================
# O Frame 0 é a base. Os outros frames estão deslocados 0.3m no X local do anterior.
# Se fosse 3D, você poderia passar rpy=[np.pi/2, 0, 0] para tombar um eixo.
f1 = Frame(name="F1", origin=[0.0, 0.0, 0.0])
f2 = Frame(name="F2", origin=[0.3, 0.0, 0.0])
f3 = Frame(name="F3", origin=[0.3, 0.0, 0.0])
f_garra = Frame(name="F_Garra", origin=[0.3, 0.0, 0.0]) # A ponta da garra está a 0.3m da J3

# =======================================================
# 2. MODELAGEM DAS JUNTAS (Atuadores)
# =======================================================
# Especificamos explicitamente o eixo 'z' para clareza
j1 = JuntaRotacional(name="J1", frame=f1, axis='z')
j2 = JuntaRotacional(name="J2", frame=f2, axis='z')
j3 = JuntaRotacional(name="J3", frame=f3, axis='z')
j_garra = JuntaRotacional(name="JG", frame=f_garra, axis='z') # Travada (0 rad)

# =======================================================
# 3. MONTAGEM DO ROBÔ
# =======================================================
robo = RoboArticulado(name="Planar_3R", joints=[j1, j2, j3, j_garra])

# =======================================================
# 4. APLICAÇÃO DOS VALORES (Cinemática Direta)
# =======================================================
# Lembra: para o código bater com o "Z para dentro" e "Y para cima" da questão,
# usamos a lógica de inverter o sinal se estivermos usando um sistema destro padrão.
val_j1 = -np.pi/2 # +90 deg Horário
val_j2 =  np.pi/2 # -90 deg Anti-horário
val_j3 = -np.pi/2 # +90 deg Horário
valores_atuacao = [val_j1, val_j2, val_j3, 0.0]

# =======================================================
# 5. RESULTADOS
# =======================================================
print("=== RESULTADOS (MODELO 3D-READY) ===")

posicoes = robo.get_xyz_positions(valores_atuacao)
for i, pos in enumerate(posicoes):
    print(f"Ponto {i}: X={pos[0]:.2f}, Y={pos[1]:.2f}, Z={pos[2]:.2f}")

matrizes = robo.forward_kinematics(valores_atuacao)
m_final = matrizes[-1]

# Calculando a orientação final
phi_rad = np.arctan2(m_final[1, 0], m_final[0, 0])
phi_deg = np.rad2deg(phi_rad)

print("\n=== RESPOSTA FINAL ===")
print(f"x   = {m_final[0, 3]:.1f} m")
print(f"y   = {m_final[1, 3]:.1f} m")
print(f"phi = {phi_deg:.0f}°")