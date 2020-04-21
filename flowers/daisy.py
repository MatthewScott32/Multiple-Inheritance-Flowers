from actions import IBloom, IWither
from .flower import Flower

class Daisy(IBloom, IWither, Flower):
    def __init__(self, name, stem, color):
        IBloom.__init__(self)
        IWither.__init__(self)
        Flower.__init__(self, stem, color)
        self.name = name

    def __str__(self):
        return f'{self.name}'