# coding=utf-8
from cini.models import Posicion

from expects import *


with description('Calculando el CINI de una posición'):
    with context('la primera posición'):
        with it('must be 2'):
            pos = Posicion()
            cini = pos.cini
            expect(cini[1]).to(equal('2'))

    with context('la segunda posición'):
        with it('must be 8'):
            pos = Posicion()
            cini = pos.cini
            expect(cini[2]).to(equal('8'))
    
    with context('la tercera posición'):
        with before.each:
            self.pos = Posicion()
        with context('si la tensión U >= 110 kV'):
            with it('must be A'):
                for v in (110, 400, 1000):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[3]).to(equal('A'))
        with context('si la tensión 110 kV > U ≥ 36 kV'):
            with it('must be B'):
                for v in range(36, 110):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[3]).to(equal('B'))
        with context('si la tensión 36 kV > U ≥ 1 kV'):
            with it('must be C'):
                for v in range(1, 36):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[3]).to(equal('C'))

    with context('la cuarta posición'):
        with context('si tiene interruptor'):
            with it('must be 2'):
                pos = Posicion()
                pos.interruptor = True
                cini = pos.cini
                expect(cini[4]).to(equal('2'))
        with context('si no tiene interruptor'):
            with it('must be 3'):
                pos = Posicion()
                pos.interruptor = False
                cini = pos.cini
                expect(cini[4]).to(equal('3'))
    
    with context('la quinta posición'):
        with before.each:
            self.pos = Posicion()
        with context('si la situación es de Interior'):
            with before.each:
                self.pos.situacion = 'I'
            with context('si el tipo es Blindada'):
                with it('must be A'):
                    self.pos.tipo = 'B'
                    cini = self.pos.cini
                    expect(cini[5]).to(equal('A'))
            with context('si el tipo es Convencional'):
                with it('must be C'):
                    self.pos.tipo = 'C'
                    cini = self.pos.cini
                    expect(cini[5]).to(equal('C'))
            with context('si el tipo es Híbrida'):
                with it('must be E'):
                    self.pos.tipo = 'H'
                    cini = self.pos.cini
                    expect(cini[5]).to(equal('E'))
        with context('si la situación es de Intemperie'):
            with before.each:
                self.pos.situacion = 'E'
            with context('si el tipo es Blindada'):
                with it('must be B'):
                    self.pos.tipo = 'B'
                    cini = self.pos.cini
                    expect(cini[5]).to(equal('B'))
            with context('si el tipo es Convencional'):
                with it('must be D'):
                    self.pos.tipo = 'C'
                    cini = self.pos.cini
                    expect(cini[5]).to(equal('D'))
            with context('si el tipo es Híbrida'):
                with it('must be F'):
                    self.pos.tipo = 'H'
                    cini = self.pos.cini
                    expect(cini[5]).to(equal('F'))
        with context('si la situación es Móvil'):
            with before.each:
                self.pos.situacion = 'M'
            with context('si el tipo es Blindada'):
                with it('must be G'):
                    self.pos.tipo = 'B'
                    cini = self.pos.cini
                    expect(cini[5]).to(equal('G'))

    with description('la sexta posición'):
        with before.each:
            self.pos = Posicion()
        with context('si la actuación es de Linea'):
            with it('must be 1'):
                self.pos.actuacion = 'L'
                cini = self.pos.cini
                expect(cini[6]).to(equal('1'))
        with context('si la actuación es de Transformación'):
            with it('must be 2'):
                self.pos.actuacion = 'T'
                cini = self.pos.cini
                expect(cini[6]).to(equal('2'))
        with context('si la actuación es de Acoplamiento'):
            with it('must be 3'):
                self.pos.actuacion = 'A'
                cini = self.pos.cini
                expect(cini[6]).to(equal('3'))
        with context('si la actuación es de medida'):
            with it('must be 4'):
                self.pos.actuacion = 'M'
                cini = self.pos.cini
                expect(cini[6]).to(equal('4'))
        with context('si la actuación es de reserva'):
            with it('must be 5'):
                self.pos.actuacion = 'R'
                cini = self.pos.cini
                expect(cini[6]).to(equal('5'))

    with description('la séptima posición'):
        with before.each:
            self.pos = Posicion()
        with context('si la tensión <= 1 kV'):
            with it('must be C'):
                self.pos.tension = 1
                cini = self.pos.cini
                expect(cini[7]).to(equal('C'))
        with context('si la tensión 1 < U <= 3 kV'):
            with it('must be D'):
                for v in range(3, 1, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('D'))
        with context('si la tensión 3 < U <= 5 kV'):
            with it('must be E'):
                for v in range(5, 3, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('E'))
        with context('si la tensión 5 < U <= 5.5 kV'):
            with it('must be F'):
                for v in range(55, 50, -1):
                    self.pos.tension = v / 10.0
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('F'))
        with context('si la tensión 5.5 < U <= 6 kV'):
            with it('must be G'):
                for v in range(60, 55, -1):
                    self.pos.tension = v / 10.0
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('G'))
        with context('si la tensión 6 < U <= 6.6 kV'):
            with it('must be H'):
                for v in range(66, 60, -1):
                    self.pos.tension = v / 10.0
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('H'))
        with context('si la tensión 6.6 < U <= 10 kV'):
            with it('must be I'):
                for v in range(100, 66, -1):
                    self.pos.tension = v / 10.0
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('I'))
        with context('si la tensión 10 < U <= 11 kV'):
            with it('must be J'):
                for v in range(11, 10, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('J'))
        with context('si la tensión 11 < U <= 12 kV'):
            with it('must be K'):
                for v in range(12, 11, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('K'))
        with context('si la tensión 12 < U <= 13.2 kV'):
            with it('must be L'):
                for v in range(132, 120, -1):
                    self.pos.tension = v / 10.0
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('L'))
        with context('si la tensión 13.2 < U <= 15 kV'):
            with it('must be M'):
                for v in range(150, 132, -1):
                    self.pos.tension = v / 10.0
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('M'))
        with context('si la tensión 15 < U <= 16 kV'):
            with it('must be N'):
                for v in range(16, 15, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('N'))
        with context('si la tensión 16 < U <= 20 kV'):
            with it('must be O'):
                for v in range(20, 16, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('O'))
        with context('si la tensión 20 < U <= 22 kV'):
            with it('must be P'):
                for v in range(22, 20, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('P'))
        with context('si la tensión 22 < U <= 24 kV'):
            with it('must be Q'):
                for v in range(24, 22, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('Q'))
        with context('si la tensión 24 < U <= 25 kV'):
            with it('must be R'):
                for v in range(25, 24, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('R'))
        with context('si la tensión 25 < U <= 30 kV'):
            with it('must be S'):
                for v in range(30, 25, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('S'))
        with context('si la tensión 30 < U <= 33 kV'):
            with it('must be T'):
                for v in range(33, 30, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('T'))
        with context('si la tensión 33 < U <= 45 kV'):
            with it('must be U'):
                for v in range(45, 33, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('U'))
        with context('si la tensión 45 < U <= 50 kV'):
            with it('must be V'):
                for v in range(50, 45, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('V'))
        with context('si la tensión 50 < U <= 55 kV'):
            with it('must be W'):
                for v in range(55, 50, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('W'))
        with context('si la tensión 55 < U <= 66 kV'):
            with it('must be X'):
                for v in range(66, 55, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('X'))
        with context('si la tensión 66 < U <= 110 kV'):
            with it('must be Y'):
                for v in range(110, 66, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('Y'))
        with context('si la tensión 110 < U <= 130 kV'):
            with it('must be Z'):
                for v in range(130, 110, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('Z'))
        with context('si la tensión 130 < U <= 132 kV'):
            with it('must be 1'):
                for v in range(132, 130, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('1'))
        with context('si la tensión 132 < U <= 150 kV'):
            with it('must be 2'):
                for v in range(150, 132, -1):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('2'))
        with context('si la tensión > 150 kV'):
            with it('must be 5'):
                for v in (151, 1000):
                    self.pos.tension = v
                    cini = self.pos.cini
                    expect(cini[7]).to(equal('5'))

