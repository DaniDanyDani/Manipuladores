from junta import JuntaRevolucao, JuntaPrismatica
from robo import RoboArticulado

# 1. Cria as juntas (idealmente já com o tamanho dos elos embutidos)
j1 = JuntaRevolucao("Base")
t1 = JuntaPrismatica("L1")
j2 = JuntaRevolucao("Ombro")
t2 = JuntaPrismatica("L2")
j3 = JuntaRevolucao("Cotovelo")
t3 = JuntaPrismatica("L3")
j4 = JuntaRevolucao("Atuador")

# 2. Monta o Robô
meu_robo = RoboArticulado("Braco_Mecanico", [j1, t1, j2, t2, j3, t3, j4])

# 3. Na simulação, passa os ângulos (ex: 90 graus na base, 45 no ombro, 0 no cotovelo)
angulos_no_tempo_1 = [90, 1, 45, 1, 0, 1, 0]
posicao_ponta = meu_robo.calcular_cinematica_direta(angulos_no_tempo_1)

print(f"A garra do robô está na posição: {posicao_ponta}")