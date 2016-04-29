# coding=utf-8
from cini.models import *


with description('Una Linea'):
    with before.all:
        self.linea = Linea()
    with it('must have atributo tensión'):
        assert hasattr(self.linea, 'tension')
    with it('must have número de circuitos'):
        assert hasattr(self.linea, 'num_circuitos')
    with it('must have número de conductors'):
        assert hasattr(self.linea, 'num_conductores')
    with it('must have sección del cable'):
        assert hasattr(self.linea, 'seccion')
    with it('must have despliegue'):
        assert hasattr(self.linea, 'despliegue')
