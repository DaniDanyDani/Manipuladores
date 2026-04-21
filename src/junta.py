from abc import ABC, abstractmethod
from frame import Frame

class Junta(ABC):
    def __init__(self, name=None, numGL=None, frame=None):
        self.name = "{0}" if name is None else name
        self.numGL = 0 if numGL is None else numGL
        self.frame = Frame() if frame is None else frame
    
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, valor):
        self.__name = valor

    @property
    def numGL(self):
        return self.__numGL
        
    @numGL.setter
    def numGL(self, valor):
        self.__numGL = valor

    @property
    def frame(self):
        return self.__frame
        
    @frame.setter
    def frame(self, valor):
        self.__frame = valor if isinstance(valor, Frame) else Frame()


class JuntaPrismatica(Junta):
    def __init__(self, name=None, numGL=None, frame=None):
        super().__init__(name, numGL, frame)



class JuntaCilindrica(Junta):
    def __init__(self, name=None, numGL=None, frame=None):
        super().__init__(name, numGL, frame)



class JuntaEsferica(Junta):
    def __init__(self, name=None, numGL=None, frame=None):
        super().__init__(name, numGL, frame)

