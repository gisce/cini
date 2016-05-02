# coding=utf-8
from cini.models import *

from expects import *


with description('Calculando un CINI de un transformador'):
    with description('la primera posición'):
        with it('must be 2'):
            t = Transformador()
            expect(t.cini[1]).to(equal('2'))

    with description('la segunda posición'):
        with it('must be 7'):
            t = Transformador()
            expect(t.cini[2]).to(equal('7'))

    with description('la tercera posición'):
        with before.all:
            self.trafo = Transformador()
        with context('Si la tensión >= 400 kV'):
            with it('must be 0'):
                for v in (400, 500, 1000):
                    self.trafo.tension = v
                    cini = self.trafo.cini
                    expect(cini[3]).to(equal('0'))
        with context('Si la tensión 220kV<=U<400 kV'):
            with it('must be 1'):
                for v in range(220, 400):
                    self.trafo.tension = v
                    cini = self.trafo.cini
                    expect(cini[3]).to(equal('1'))
        with context('Si la tensión 110kV<=U<220kV'):
            with it('must be 2'):
                for v in range(110, 220):
                    self.trafo.tension = v
                    cini = self.trafo.cini
                    expect(cini[3]).to(equal('2'))
        with context('Si la tensión 36kV<=U<110kV'):
            with it('must be 3'):
                for v in range(36, 110):
                    self.trafo.tension = v
                    cini = self.trafo.cini
                    expect(cini[3]).to(equal('3'))
        with context('Si la tensión 1kV<=U<36kV'):
            with it('must be 4'):
                for v in range(1, 36):
                    self.trafo.tension = v
                    cini = self.trafo.cini
                    expect(cini[3]).to(equal('4'))

    with description('la cuarta posición'):
        with context('Si la tensión 110kV<=U<220kV'):
            with it('must be 2'):
                for v in range(110, 220):
                    self.trafo.tension = v
                    cini = self.trafo.cini
                    expect(cini[4]).to(equal('2'))
        with context('Si la tensión 36kV<=U<110kV'):
            with it('must be 3'):
                for v in range(36, 110):
                    self.trafo.tension = v
                    cini = self.trafo.cini
                    expect(cini[4]).to(equal('3'))
        with context('Si la tensión 1kV<=U<36kV'):
            with it('must be 4'):
                for v in range(1, 36):
                    self.trafo.tension = v
                    cini = self.trafo.cini
                    expect(cini[4]).to(equal('4'))
        with context('Si la tensión U < 1 Kv'):
            with it('must be 5'):
                self.trafo.tension = 0.400
                cini = self.trafo.cini
                expect(cini[4]).to(equal('5'))
    
    with description('la quinta posición'):
        with before.all:
            self.trafo = Transformador()
        with context('si está en una subestación'):
            with it('must be 1'):
                self.trafo.situacion = 'SE'
                cini = self.trafo.cini
                expect(cini[5]).to(equal('1'))
        with context('si está en un centro de transformación'):
            with it('must be 2'):
                self.trafo.situacion = 'CT'
                cini = self.trafo.cini
                expect(cini[5]).to(equal('2'))
    
    with description('la sexta posición'):
        with before.all:
            self.trafo = Transformador()
        with context('si la potencia S<1 MVA'):
            with it('must be A'):
                self.trafo.potencia = 0.05
                cini = self.trafo.cini
                expect(cini[6]).to(equal('A'))
        with context('si la potencia 1<=S<5 MVA'):
            with it('must be B'):
                for v in range(1, 5):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('B'))
        with context('si la potencia 5<=S<10 MVA'):
            with it('must be C'):
                for v in range(5, 10):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('C'))
        with context('si la potencia 10<=S<15 MVA'):
            with it('must be D'):
                for v in range(10, 15):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('D'))
        with context('si la potencia 15<=S<20 MVA'):
            with it('must be E'):
                for v in range(15, 20):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('E'))

    with description('la séptima posición'):
        with before.all:
            self.trafo = Transformador()
        with context('si el trafo en servicio'):
            with it('must be 0'):
                self.trafo.estado = 'S'
                cini = self.trafo.cini
                expect(cini[7]).to(equal('0'))
        with context('si el trafo en reserva'):
            with it('must be 1'):
                self.trafo.estado = 'R'
                cini = self.trafo.cini
                expect(cini[7]).to(equal('1'))
        with context('si el trafo es móvil'):
            with it('must be 2'):
                self.trafo.estado = 'M'
                cini = self.trafo.cini
                expect(cini[7]).to(equal('2'))
