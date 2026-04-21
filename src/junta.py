from abc import ABC, abstractmethod

class Junta(ABC):
    def __init__(self, name, numGL, frameName):
        self.setName(name)
        self.setFrame(frameName)
    
    def setName(self, name):
        self.__name = name
    def setFrame(self, frameName):
        self.__frame = frameName
    def setNumGL(self, numGL):
        self.__numGL = numGL

    def getName(self):
        return self.__name
    def getFrame(self):
        return self.__frame
    def getNumGL(self):
        return self.__numGL