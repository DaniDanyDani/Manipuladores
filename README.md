# Manipuladores Roboticos - Cinematica Direta

Este projeto e uma biblioteca em Python para modelagem de manipuladores roboticos. Ele permite a criacao de frames de coordenadas, definicao de juntas (rotacionais) e o calculo da cinematica direta de robos articulados usando matrizes de transformacao homogenea 4x4.

## Estrutura do Projeto

- `src/`: Contem o nucleo da biblioteca (logica de matrizes, juntas e robo).
- `tests/`: Testes automatizados para garantir a fidelidade matematica.
- `scripts/`: Exemplos praticos de uso (ex: robo planar do Enade).
- `requirements.txt`: Lista de dependencias do projeto.

## Instalacao

1. Certifique-se de ter o [Miniconda](https://docs.conda.io/en/latest/miniconda.html) ou Anaconda instalado.
2. Clone o repositorio e entre na pasta do projeto:
   ```bash
   git clone https://github.com/DaniDanyDani/Manipuladores.git
   cd Manipuladores
3. Crie o ambiente virtual a partir do arquivo de configuracao:
   ```bash
   conda env create -f environment.yml
4. Ative o ambiente criado:
   ```bash
   conda activate manipulador-env

## Exemplo de uso

Para rodar o exemplo do robo planar de 3 juntas (baseado na questao do ENADE), utilize o script na pasta **scripts**:

```bash
python scripts/exemplo_robo_planar.py
```

### Funcionalidades Atuais
- [x] Frames de Coordenadas: Suporte a translacao (x, y, z) e rotacao RPY (Roll, Pitch, Yaw).

- [x] Juntas Rotacionais: Atuacao dinamica em torno dos eixos X, Y ou Z.

- [x] Robo Articulado: Calculo de cadeia cinematica e obtencao de coordenadas globais XYZ.