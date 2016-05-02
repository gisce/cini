# coding=utf-8
from cini.models import *

from expects import *


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


with description('Un transformador'):
    with before.all:
        self.trafo = Transformador()
    with it('tener atributo tensión'):
        expect(hasattr(self.trafo, 'tension')).to(be_true)
    with it('tener atributo situación'):
        expect(hasattr(self.trafo, 'situacion')).to(be_true)
    with it('tener atributo potencia'):
        expect(hasattr(self.trafo, 'potencia')).to(be_true)
    with it('tener atributo estado'):
        expect(hasattr(self.trafo, 'estado')).to(be_true)
