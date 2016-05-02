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
        with context('si tensión primario 1kV<=U<36kV'):
            with _it('must be 4'):
                for v in range(1, 36):
                    self.ct.tension = v
                    cini = self.ct.cini
                    expect(cini[3]).to(equal('4'))

    with description('la cuarta posición'):
        with before.all:
            self.ct = CentroTransformador()
        with context('si la tensión del secundario U < 1 Kv'):
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
    
    with context('la séptima posición'):
        with context('si tiene un transformador'):
            with context('si la potencia = 0 kVA'):
                with _it('must be A'):
                    pass
            with context('si la potencia 0 < p <= 15 kVA'):
                with _it('must be B'):
                    pass
            with context('si la potencia 15 < p <= 25 kVA'):
                with _it('must be C'):
                    pass
            with context('si la potencia 25 < p <= 50 kVA'):
                with _it('must be D'):
                    pass
            with context('si la potencia 50 < p <= 100 kVA'):
                with _it('must be E'):
                    pass
            with context('si la potencia 100 < p <= 160 kVA'):
                with _it('must be F'):
                    pass
            with context('si la potencia 160 < p <= 250 kVA'):
                with _it('must be G'):
                    pass
            with context('si la potencia 250 < p <= 400 kVA'):
                with _it('must be H'):
                    pass
            with context('si la potencia 400 < p <= 630 kVA'):
                with _it('must be I'):
                    pass
            with context('si la potencia 630 < p <= 1000 kVA'):
                with _it('must be J'):
                    pass
            with context('si la potencia 1000 < p <= 1250 kVA'):
                with _it('must be K'):
                    pass
        with context('si tiene 2 transformadores'):
            with context('si la potencia <= 2x15 kVA'):
                with _it('must be L'):
                    pass
            with context('si la potencia 2x15 < p <= 2x25 kVA'):
                with _it('must be M'):
                    pass
            with context('si la potencia 2x25 < p <= 2x50 kVA'):
                with _it('must be N'):
                    pass
            with context('si la potencia 2x50 < p <= 2x100 kVA'):
                with _it('must be O'):
                    pass
            with context('si la potencia 2x100 < p <= 2x160 kVA'):
                with _it('must be P'):
                    pass
            with context('si la potencia 2x160 < p <= 2x250 kVA'):
                with _it('must be Q'):
                    pass
            with context('si la potencia 2x250 < p <= 2x400 kVA'):
                with _it('must be R'):
                    pass
            with context('si la potencia 2x400 < p <= 2x630 kVA'):
                with _it('must be S'):
                    pass
            with context('si la potencia 2x630 < p <= 2x1000 kVA'):
                with _it('must be T'):
                    pass
            with context('si la potencia 2x1000 < p <= 2x1250 kVA'):
                with _it('must be U'):
                    pass
        with context('Si no tiene ningún transformador'):
            with context('si no es de reparto o reflexión'):
                with _it('must be V'):
                    pass
            with context('si es de reparto o reflexión'):
                with _it('must be Z'):
                    pass
