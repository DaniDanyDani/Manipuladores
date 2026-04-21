from abc import ABC, abstractmethod
from junta import Junta

class Robo(ABC):
    def __init__(self, numJuntas, numLinks):
        self.setNumJuntas(numJuntas)
        self.setNumLinks(numLinks)
    
    def setNumJuntas(self, numJuntas):
        self.__numJuntas = numJuntas
    def setNumLinks(self, numLinks):
        self.__numLinks = numLinks
        
    def getNumJuntas(self):
        return self.__numJuntas
    def getNumLinks(self):
        return self.__numLinks
    
    @staticmethod
    def createRobo(self, juntasList, linksList):
        pass

class RoboArticulado(Robo):
    def __init__(self, numJuntas, numLinks):
        super().__init__(numJuntas, numLinks)


class RoboCartesiano(Robo):
    def __init__(self, numJuntas, numLinks):
        super().__init__(numJuntas, numLinks)


class RoboEsferico(Robo):
    def __init__(self, numJuntas, numLinks):
        super().__init__(numJuntas, numLinks)


class RoboCilindrico(Robo):
    def __init__(self, numJuntas, numLinks):
        super().__init__(numJuntas, numLinks)


class RoboSCARA(Robo):
    def __init__(self, numJuntas, numLinks):
        super().__init__(numJuntas, numLinks)

