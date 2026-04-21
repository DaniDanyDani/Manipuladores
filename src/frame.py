from abc import ABC, abstractmethod

class Frame(ABC):
    def __init__(self, origem, orientacao):
        self.setOrigem(origem)
        self.setOrientacao(origem)