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


with description('Un Centro transformador'):
    with before.all:
        self.ct = CentroTransformador()
    with _it('tener el atributo tensión primario'):
        expect(hasattr(self.ct, 'tension_p')).to(be_true)
    with context('el atributo reparto'):
        with before.all:
            self.ct = CentroTransformador()
        with _it('debe existir'):
            expect(hasattr(self.ct, 'reparto')).to(be_true)
        with _it('debe ser True por defecto'):
            expect(self.ct.reparto).to(be_true)
    with _it('tener el atributo tensión secundario'):
        expect(hasattr(self.ct, 'tension_s')).to(be_true)
    with _it('tener el atributo tipo'):
        expect(hasattr(self.ct, 'tipo')).to(be_true)
    with _it('tener el atributo transformadores'):
        expect(hasattr(self.ct, 'transformadores')).to(be_true)
    with _it('el atributo tranformadores debe ser una lista'):
        expect(self.ct.transformadores).to(be_an(list))
    with context('el atributo potencia instalada'):
        with before.all:
            self.ct = CentroTransformador()
        with _it('debe existir'):
            expect(hasattr(self.ct, 'potencia_instalada')).to(be_true)
        with _it('debe ser la suma de las potencias de los transformadores que no esten en reserva'):
            trafo1 = Transformador()
            trafo1.potencia = 50

            trafo2 = Transformador()
            trafo2.potencia = 50

            expect(self.ct.potencia_instalada).to(equal(100))

