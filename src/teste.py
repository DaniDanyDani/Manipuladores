import numpy as np
from junta import JuntaRevolucao, JuntaPrismatica
from robo import RoboArticulado

# 1. Cria as juntas passando o eixo direto na criação.
j1 = JuntaRevolucao("Base", axis="z")
t1 = JuntaPrismatica("L1", axis="x")
j2 = JuntaRevolucao("Ombro", axis="z")
t2 = JuntaPrismatica("L2", axis="x")
j3 = JuntaRevolucao("Cotovelo", axis="z")
t3 = JuntaPrismatica("L3", axis="x")
j4 = JuntaRevolucao("Atuador", axis="z")

# 2. Monta o Robô
meu_robo = RoboArticulado("Braco_Mecanico", [j1, t1, j2, t2, j3, t3, j4])

# 3. Simulação
angulos_no_tempo_1 = [0, 0, 90, 1, 90, 1, 0]
posicao_ponta = meu_robo.calcular_cinematica_direta(angulos_no_tempo_1)
posicao_arredondada = np.round(posicao_ponta, 4)

print(f"A garra do robô está na posição: {posicao_arredondada}")