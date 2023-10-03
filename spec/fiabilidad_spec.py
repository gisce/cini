# coding=utf-8
from cini.models import Fiabilidad
from mamba import *
from expects import *


with description('Calculando el CINI de un elemento de fiabiliadd'):

    with description('la primera posición'):
        with it('must be 2'):
            l = Fiabilidad()
            expect(l.cini[1]).to(equal('2'))

    with description('la segunda posición'):
        with context('si es un CT'):
            with it('must be 8'):
                l = Fiabilidad()
                l.situacion = 'CT'
                expect(l.cini[2]).to(equal('8'))
        with it('must be 6'):
            l = Fiabilidad()
            expect(l.cini[2]).to(equal('6'))

    with description('la tercera posición'):
        with context('Si está en un poste'):
            with before.each:
                self.fiab = Fiabilidad()
                self.fiab.situacion = 'LAT'
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

        with context('Si está en un CT'):
            with before.each:
                self.fiab = Fiabilidad()
                self.fiab.situacion = 'CT'
            with context('si 110kV<=U<220kV'):
                with it('must be 2'):
                    for v in range(110, 220):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[3]).to(equal('A'))
            with context('si 36kV<=U<110kV'):
                with it('must be 3'):
                    for v in range(36, 110):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[3]).to(equal('B'))
            with context('si 1kV<=U<36kV'):
                with it('must be 4'):
                    for v in range(1, 36):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[3]).to(equal('C'))

    with description('la cuarta posición'):
        with context('Si está en un CT'):
            with context('y el tipo es un interruptor automático'):
                with it('must be 2'):
                    l = Fiabilidad()
                    l.situacion = 'CT'
                    l.tipo = 'R'
                    cini = l.cini
                    expect(cini[4]).to(equal('2'))
            with context('otros casos'):
                with it('must be 3'):
                    l = Fiabilidad()
                    l.situacion = 'CT'
                    l.tipo = 'S'
                    cini = l.cini
                    expect(cini[4]).to(equal('3'))
        with before.all:
            self.fiab = Fiabilidad()
        with it('must be 0'):
            cini = self.fiab.cini
            expect(cini[4]).to(equal('0'))

    with description('la quinta posición'):
        with context('si es LAT'):
            with before.all:
                self.fiab = Fiabilidad()
                self.fiab.situacion = 'LAT'
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
        with context('Si es un CT'):
            with before.all:
                self.fiab = Fiabilidad()
                self.fiab.situacion = 'CT'
            with context('el aislante es AIRE'):
                with it('must be C'):
                    self.fiab.aislante = 'aire'
                    cini = self.fiab.cini
                    expect(cini[5]).to(equal('C'))
            with context('los otros casos'):
                with it('must be A'):
                    self.fiab.aislante = 'sf6'
                    cini = self.fiab.cini
                    expect(cini[5]).to(equal('A'))

    with description('la sexta posición'):
        with context('si es LAT'):
            with before.all:
                self.fiab = Fiabilidad()
                self.fiab.situacion = 'LAT'
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
        with context('si es CT'):
            with before.all:
                self.fiab = Fiabilidad()
                self.fiab.situacion = 'CT'
            with context('el tipo posicion es Linia'):
                with it('must be 1'):
                    self.fiab.tipo_posicion = 'L'
                    cini = self.fiab.cini
                    expect(cini[6]).to(equal('1'))
            with context('el tipo posicion es proteccion'):
                with it('must be 2'):
                    self.fiab.tipo_posicion = 'P'
                    cini = self.fiab.cini
                    expect(cini[6]).to(equal('2'))

    with description('la séptima posición'):
        with context('si es LAT'):
            with before.all:
                self.fiab = Fiabilidad()
                self.fiab.situacion = 'LAT'
                with it('must be 3'):
                    cini = self.fiab.cini
                    expect(cini[7]).to(equal('3'))
        with context('si es un CT'):
            with before.all:
                self.fiab = Fiabilidad()
                self.fiab.situacion = 'CT'
            with context('si la tensión <= 1 kV'):
                with it('must be C'):
                    self.fiab.tension = 1
                    cini = self.fiab.cini
                    expect(cini[7]).to(equal('C'))
            with context('si la tensión 1 < U <= 3 kV'):
                with it('must be D'):
                    for v in range(3, 1, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('D'))
            with context('si la tensión 3 < U <= 5 kV'):
                with it('must be E'):
                    for v in range(5, 3, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('E'))
            with context('si la tensión 5 < U <= 5.5 kV'):
                with it('must be F'):
                    for v in range(55, 50, -1):
                        self.fiab.tension = v / 10.0
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('F'))
            with context('si la tensión 5.5 < U <= 6 kV'):
                with it('must be G'):
                    for v in range(60, 55, -1):
                        self.fiab.tension = v / 10.0
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('G'))
            with context('si la tensión 6 < U <= 6.6 kV'):
                with it('must be H'):
                    for v in range(66, 60, -1):
                        self.fiab.tension = v / 10.0
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('H'))
            with context('si la tensión 6.6 < U <= 10 kV'):
                with it('must be I'):
                    for v in range(100, 66, -1):
                        self.fiab.tension = v / 10.0
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('I'))
            with context('si la tensión 10 < U <= 11 kV'):
                with it('must be J'):
                    for v in range(11, 10, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('J'))
            with context('si la tensión 11 < U <= 12 kV'):
                with it('must be K'):
                    for v in range(12, 11, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('K'))
            with context('si la tensión 12 < U <= 13.2 kV'):
                with it('must be L'):
                    for v in range(132, 120, -1):
                        self.fiab.tension = v / 10.0
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('L'))
            with context('si la tensión 13.2 < U <= 15 kV'):
                with it('must be M'):
                    for v in range(150, 132, -1):
                        self.fiab.tension = v / 10.0
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('M'))
            with context('si la tensión 15 < U <= 16 kV'):
                with it('must be N'):
                    for v in range(16, 15, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('N'))
            with context('si la tensión 16 < U <= 20 kV'):
                with it('must be O'):
                    for v in range(20, 16, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('O'))
            with context('si la tensión 20 < U <= 22 kV'):
                with it('must be P'):
                    for v in range(22, 20, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('P'))
            with context('si la tensión 22 < U <= 24 kV'):
                with it('must be Q'):
                    for v in range(24, 22, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('Q'))
            with context('si la tensión 24 < U <= 25 kV'):
                with it('must be R'):
                    for v in range(25, 24, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('R'))
            with context('si la tensión 25 < U <= 30 kV'):
                with it('must be S'):
                    for v in range(30, 25, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('S'))
            with context('si la tensión 30 < U <= 33 kV'):
                with it('must be T'):
                    for v in range(33, 30, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('T'))
            with context('si la tensión 33 < U <= 45 kV'):
                with it('must be U'):
                    for v in range(45, 33, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('U'))
            with context('si la tensión 45 < U <= 50 kV'):
                with it('must be V'):
                    for v in range(50, 45, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('V'))
            with context('si la tensión 50 < U <= 55 kV'):
                with it('must be W'):
                    for v in range(55, 50, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('W'))
            with context('si la tensión 55 < U <= 66 kV'):
                with it('must be X'):
                    for v in range(66, 55, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('X'))
            with context('si la tensión 66 < U <= 110 kV'):
                with it('must be Y'):
                    for v in range(110, 66, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('Y'))
            with context('si la tensión 110 < U <= 130 kV'):
                with it('must be Z'):
                    for v in range(130, 110, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('Z'))
            with context('si la tensión 130 < U <= 132 kV'):
                with it('must be 1'):
                    for v in range(132, 130, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('1'))
            with context('si la tensión 132 < U <= 150 kV'):
                with it('must be 2'):
                    for v in range(150, 132, -1):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('2'))
            with context('si la tensión > 150 kV'):
                with it('must be 5'):
                    for v in (151, 1000):
                        self.fiab.tension = v
                        cini = self.fiab.cini
                        expect(cini[7]).to(equal('5'))
