# coding=utf-8
from cini.models import *

from expects import *

with description('Calculando el CINI de un Centro transformador'):

    with description('la primera posición'):
        with _it('must be 2'):
            ct = CentroTransformador()
            expect(l.cini[1]).to(equal('2'))

    with description('la segunda posición'):
        with _it('must be 2'):
            l = Linea()
            expect(l.cini[2]).to(equal('2'))
    
    with description('la tercera posición'):
        with before.all:
            self.ct = CentroTransformador()
        with context('si 1kV<=U<36kV'):
            with _it('must be 4'):
                for v in range(1, 36):
                    self.ct.tension = v
                    cini = self.ct.cini
                    expect(cini[3]).to(equal('4'))

    with description('la cuarta posición'):
        with before.all:
            self.ct = CentroTransformador()
        with context('si U < 1 Kv'):
            with _it('must be 5'):
                for v in (0.4, 0.9):
                    self.ct.tension = v
                    cini = self.ct.cini
                    expect(cini[4]).to(equal('5'))

    with description('la quinta posición'):
        with before.all:
            self.ct = CentroTransformador()
        with context('si el tipo es Intemperie'):
            with _it('must be 1'):
                self.ct.tipo = 'I'
                cini = self.ct.cini
                expect(cini[5]).to(equal('1'))
        with context('si el tipo es Caseta'):
            with _it('must be 2'):
                self.ct.tipo = 'C'
                cini = self.ct.cini
                expect(cini[5]).to(equal('2'))
        with context('si el tipo es Local'):
            with _it('must be 3'):
                self.ct.tipo = 'L'
                cini = self.ct.cini
                expect(cini[5]).to(equal('3'))
        with context('si el tipo es Subterráneo'):
            with _it('must be 4'):
                self.ct.tipo = 'S'
                cini = self.ct.cini
                expect(cini[5]).to(equal('4'))
        with context('si el tipo es Móvil'):
            with _it('must be 9'):
                self.ct.tipo = 'M'
                cini = self.ct.cini
                expect(cini[5]).to(equal('9'))

    with description('la sexta posicion'):
        with before.all:
            self.ct = CentroTransformador()
        with context('si la tensión U <= 1 kV'):
            with _it('must be C'):
                pass
        with context('si la tensión U = 3 kV'):
            with _it('must be D'):
                pass
        with context('si la tension U = 5 kV'):
            with _it('must be E'):
                pass
        with context('si la tension U = 5,5 kV'):
            with _it('must be F'):
                pass
        with context('si la tension U = 6 kV'):
            with _it('must be G'):
                pass
        with context('si la tension U = 6,6 kV'):
            with _it('must be H'):
                pass
        with context('si la tensión U = 10 kV'):
            with _it('must be I'):
                pass
        with context('si la tensión U = 11 kV'):
            with _it('must be J'):
                pass
        with context('si la tensión U = 12 kV'):
            with _it('must be K'):
                pass
        with context('si la tensión U = 13,2 kV'):
            with _it('must be L'):
                pass
        with context('si la tensión U = 15 kV'):
            with _it('must be M'):
                pass
        with context('si la tensión U = 16 kV'):
            with _it('must be N'):
                pass
        with context('si la tensión U = 20 kV'):
            with _it('must be O'):
                pass
        with context('si la tensión U = 22 kV'):
            with _it('must be P'):
                pass
        with context('si la tensión U = 24 kV'):
            with _it('must be Q'):
                pass
        with context('si la tensión U = 25 kV'):
            with _it('must be R'):
                pass
        with context('si la tensión U = 30 kV'):
            with _it('must be S'):
                pass
        with context('si la tensión U = 33 kV'):
            with _it('must be T'):
                pass