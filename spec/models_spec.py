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
    with it('tener atributo tensión primaria'):
        expect(hasattr(self.trafo, 'tension_p')).to(be_true)
    with it('tener atributo tensión secundaria'):
        expect(hasattr(self.trafo, 'tension_s')).to(be_true)
    with it('tener atributo situación'):
        expect(hasattr(self.trafo, 'situacion')).to(be_true)
    with it('tener atributo potencia'):
        expect(hasattr(self.trafo, 'potencia')).to(be_true)
    with it('tener atributo estado'):
        expect(hasattr(self.trafo, 'estado')).to(be_true)


with description('Un Centro transformador'):
    with before.all:
        self.ct = CentroTransformador()
    with it('tener el atributo tensión primario'):
        expect(hasattr(self.ct, 'tension_p')).to(be_true)
    with context('el atributo reparto'):
        with before.all:
            self.ct = CentroTransformador()
        with it('debe existir'):
            expect(hasattr(self.ct, 'reparto')).to(be_true)
        with it('debe ser True por defecto'):
            expect(self.ct.reparto).to(be_true)
    with it('tener el atributo tensión secundario'):
        expect(hasattr(self.ct, 'tension_s')).to(be_true)
    with it('tener el atributo tipo'):
        expect(hasattr(self.ct, 'tipo')).to(be_true)
    with it('tener el atributo transformadores'):
        expect(hasattr(self.ct, 'transformadores')).to(be_true)
    with it('el atributo tranformadores debe ser una lista'):
        expect(self.ct.transformadores).to(be_an(list))
    with context('el atributo potencia instalada'):
        with before.all:
            self.ct = CentroTransformador()
        with it('debe existir'):
            expect(hasattr(self.ct, 'potencia_instalada')).to(be_true)
        with it('debe ser la suma de las potencias de los transformadores que no esten en reserva'):
            trafo1 = Transformador()
            trafo1.potencia = 50

            trafo2 = Transformador()
            trafo2.potencia = 50
            
            self.ct.transformadores.extend([trafo1, trafo2])

            expect(self.ct.potencia_instalada).to(equal(100))


with description('una subestación'):
    with before.all:
        self.sub = Subestacion()
    with it('debe ser del tipu Centro tranformador'):
        expect(self.sub).to(be_an(CentroTransformador))


with description('Una Posición'):
    with before.each:
        self.pos = Posicion()
    with it('debe tener el atributo tensión'):
        expect(hasattr(self.pos, 'tension')).to(be_true)
    with it('debe tener el atributo para saber si tiene interruptor'):
        expect(hasattr(self.pos, 'interruptor')).to(be_true)
    with it('debe tener el atributo situación'):
        expect(hasattr(self.pos, 'situacion')).to(be_true)
    with it('debe tener el atributo tipo'):
        expect(hasattr(self.pos, 'tipo')).to(be_true)
    with it('debe tener el atributo actuación'):
        expect(hasattr(self.pos, 'actuacion')).to(be_true)


with description('Un Parque'):
    with before.all:
        self.parque = Parque()
    with it('debe tener el atributo tension'):
        expect(hasattr(self.parque, 'tension')).to(be_true)
    with it('debe tener el atributo tipo'):
        expect(hasattr(self.parque, 'tipo')).to(be_true)
    with it('debe tener el atributo barras'):
        expect(hasattr(self.parque, 'barras')).to(be_true)


with description('Un elemento de fiabilidad'):
    with before.all:
        self.fiab = Fiabilidad()
    with it('debe tener el atributo tensión'):
        expect(self.fiab).to(have_property('tension'))
    with it('debe tener el atributo tipo'):
        expect(self.fiab).to(have_property('tipo'))
    with it('debe tener el atributo telemando'):
        expect(self.fiab).to(have_property('telemando'))
    with it('debe tener el atributo situación'):
        expect(self.fiab).to(have_property('situacion'))

with description('Un Contador'):
    with before.all:
        self.conta = Contador()
    with it('debe tener el atributo fases'):
        expect(self.conta).to(have_property('fases'))
    with it('debe tener el atributo tecnologia'):
        expect(self.conta).to(have_property('tecnologia'))
    with it('debe tener el atributo telegestionado'):
        expect(self.conta).to(have_property('telegestionado'))
    with it('debe tener el atributo tipo_agree'):
        expect(self.conta).to(have_property('tipo_agree'))
    with it('debe tener el atributo tipo_tarifa'):
        expect(self.conta).to(have_property('tipo_tarifa'))
    with it('debe tener el atributo propiedad_cliente'):
        expect(self.conta).to(have_property('propiedad_cliente'))