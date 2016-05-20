# coding=utf-8
from cini.models import Fiabilidad

from expects import *


with description('Calculando el CINI de un elemento de fiabiliadd'):

    with description('la primera posición'):
        with it('must be 2'):
            l = Fiabilidad()
            expect(l.cini[1]).to(equal('2'))

    with description('la segunda posición'):
        with it('must be 6'):
            l = Fiabilidad()
            expect(l.cini[2]).to(equal('6'))

    with description('la tercera posición'):
        with before.each:
            self.fiab = Fiabilidad()
        with context('si 110kV<=U<220kV'):
            with it('must be 2'):
                for v in range(110, 220):
                    self.fiab.tension = v
                    cini = self.fiab.cini
                    expect(cini[3]).to(equal('2'))
        with context('si 36kV<=U<110kV'):
            with it('must be 3'):
                for v in range(36, 110):
                    self.fiab.tension = v
                    cini = self.fiab.cini
                    expect(cini[3]).to(equal('3'))
        with context('si 1kV<=U<36kV'):
            with it('must be 4'):
                for v in range(1, 36):
                    self.fiab.tension = v
                    cini = self.fiab.cini
                    expect(cini[3]).to(equal('4'))

    with description('la cuarta posición'):
        with before.all:
            self.fiab = Fiabilidad()
        with it('must be 0'):
            cini = self.fiab.cini
            expect(cini[4]).to(equal('0'))

    with description('la quinta posición'):
        with before.all:
            self.fiab = Fiabilidad()
        with context('si el tipo es seccionador'):
            with it('must be 1'):
                self.fiab.tipo = 'S'
                cini = self.fiab.cini
                expect(cini[5]).to(equal('1'))
        with context('si el tipo es reconectador'):
            with it('must be 2'):
                self.fiab.tipo = 'R'
                cini = self.fiab.cini
                expect(cini[5]).to(equal('2'))
        with context('si el tipo es teleseñalizador'):
            with it('must be 3'):
                self.fiab.tipo = 'T'
                cini = self.fiab.cini
                expect(cini[5]).to(equal('3'))
        with context('si el tipo es fusible'):
            with it('must be 4'):
                self.fiab.tipo = 'F'
                cini = self.fiab.cini
                expect(cini[5]).to(equal('4'))
        with context('si el tipo es seccionalizador'):
            with it('must be 5'):
                self.fiab.tipo = 'SA'
                cini = self.fiab.cini
                expect(cini[5]).to(equal('5'))
        with context('si el tipo es interruptor'):
            with it('must be 6'):
                self.fiab.tipo = 'I'
                cini = self.fiab.cini
                expect(cini[5]).to(equal('6'))
        with context('si el tipo es interruptor-seccionador'):
            with it('must be 7'):
                self.fiab.tipo = 'IS'
                cini = self.fiab.cini
                expect(cini[5]).to(equal('7'))

    with description('la sexta posición'):
        with before.all:
            self.fiab = Fiabilidad()
        with context('si es manual'):
            with it('must be 1'):
                self.fiab.telemando = False
                cini = self.fiab.cini
                expect(cini[6]).to(equal('1'))
        with context('si es telemando'):
            with it('must be 2'):
                self.fiab.telemando = True
                cini = self.fiab.cini
                expect(cini[6]).to(equal('2'))

    with description('la séptima posición'):
        with before.all:
            self.fiab = Fiabilidad()
        with context('si la situación es subestación'):
            with it('must be 1'):
                self.fiab.situacion = 'SE'
                cini = self.fiab.cini
                expect(cini[7]).to(equal('1'))
        with context('si la situación es centro de transformación'):
            with it('must be 2'):
                self.fiab.situacion = 'CT'
                cini = self.fiab.cini
                expect(cini[7]).to(equal('2'))
        with context('si la situación es en tramo de línia'):
            with it('must be 3'):
                self.fiab.situacion = 'LAT'
                cini = self.fiab.cini
                expect(cini[7]).to(equal('3'))