# coding=utf-8
from cini.models import *

from expects import *

with description('Calculando el CINI de un Centro transformador'):

    with description('la primera posición'):
        with it('must be 2'):
            ct = CentroTransformador()
            expect(ct.cini[1]).to(equal('2'))

    with description('la segunda posición'):
        with it('must be 2'):
            ct = CentroTransformador()
            expect(ct.cini[2]).to(equal('2'))
    
    with description('la tercera posición'):
        with before.all:
            self.ct = CentroTransformador()
        with context('si tensión primario 1kV<=U<36kV'):
            with it('must be 4'):
                for v in range(1, 36):
                    self.ct.tension_p = v
                    cini = self.ct.cini
                    expect(cini[3]).to(equal('4'))

    with description('la cuarta posición'):
        with before.all:
            self.ct = CentroTransformador()
        with context('si la tensión del secundario U < 1 Kv'):
            with it('must be 5'):
                for v in (0.4, 0.9):
                    self.ct.tension_s = v
                    cini = self.ct.cini
                    expect(cini[4]).to(equal('5'))

    with description('la quinta posición'):
        with before.all:
            self.ct = CentroTransformador()
        with context('si el tipo es Intemperie'):
            with it('must be 1'):
                self.ct.tipo = 'I'
                cini = self.ct.cini
                expect(cini[5]).to(equal('1'))
        with context('si el tipo es Caseta'):
            with it('must be 2'):
                self.ct.tipo = 'C'
                cini = self.ct.cini
                expect(cini[5]).to(equal('2'))
        with context('si el tipo es Local'):
            with it('must be 3'):
                self.ct.tipo = 'L'
                cini = self.ct.cini
                expect(cini[5]).to(equal('3'))
        with context('si el tipo es Subterráneo'):
            with it('must be 4'):
                self.ct.tipo = 'S'
                cini = self.ct.cini
                expect(cini[5]).to(equal('4'))
        with context('si el tipo es Móvil'):
            with it('must be 9'):
                self.ct.tipo = 'M'
                cini = self.ct.cini
                expect(cini[5]).to(equal('9'))

    with description('la sexta posicion'):
        with before.all:
            self.ct = CentroTransformador()
        with context('si la tensión U <= 1 kV'):
            with it('must be C'):
                for v in [0.2, 0.5, 0.8, 1]:
                    self.ct.tension = v
                    cini = self.ct.cini
                    expect(cini[6]).to(equal('C'))
        with context('si la tensión U = 3 kV'):
            with it('must be D'):
                self.ct.tension = 3
                cini = self.ct.cini
                expect(cini[6]).to(equal('D'))
        with context('si la tension U = 5 kV'):
            with it('must be E'):
                self.ct.tension = 5
                cini = self.ct.cini
                expect(cini[6]).to(equal('E'))
        with context('si la tension U = 5,5 kV'):
            with it('must be F'):
                self.ct.tension = 5.5
                cini = self.ct.cini
                expect(cini[6]).to(equal('F'))
        with context('si la tension U = 6 kV'):
            with it('must be G'):
                self.ct.tension = 6
                cini = self.ct.cini
                expect(cini[6]).to(equal('G'))
        with context('si la tension U = 6,6 kV'):
            with it('must be H'):
                self.ct.tension = 6.6
                cini = self.ct.cini
                expect(cini[6]).to(equal('H'))
        with context('si la tensión U = 10 kV'):
            with it('must be I'):
                self.ct.tension = 10
                cini = self.ct.cini
                expect(cini[6]).to(equal('I'))
        with context('si la tensión U = 11 kV'):
            with it('must be J'):
                self.ct.tension = 11
                cini = self.ct.cini
                expect(cini[6]).to(equal('J'))
        with context('si la tensión U = 12 kV'):
            with it('must be K'):
                self.ct.tension = 12
                cini = self.ct.cini
                expect(cini[6]).to(equal('K'))
        with context('si la tensión U = 13,2 kV'):
            with it('must be L'):
                self.ct.tension = 13.2
                cini = self.ct.cini
                expect(cini[6]).to(equal('L'))
        with context('si la tensión U = 15 kV'):
            with it('must be M'):
                self.ct.tension = 15
                cini = self.ct.cini
                expect(cini[6]).to(equal('M'))
        with context('si la tensión U = 16 kV'):
            with it('must be N'):
                self.ct.tension = 16
                cini = self.ct.cini
                expect(cini[6]).to(equal('N'))
        with context('si la tensión U = 20 kV'):
            with it('must be O'):
                self.ct.tension = 20
                cini = self.ct.cini
                expect(cini[6]).to(equal('O'))
        with context('si la tensión U = 22 kV'):
            with it('must be P'):
                self.ct.tension = 22
                cini = self.ct.cini
                expect(cini[6]).to(equal('P'))
        with context('si la tensión U = 24 kV'):
            with it('must be Q'):
                self.ct.tension = 24
                cini = self.ct.cini
                expect(cini[6]).to(equal('Q'))
        with context('si la tensión U = 25 kV'):
            with it('must be R'):
                self.ct.tension = 25
                cini = self.ct.cini
                expect(cini[6]).to(equal('R'))
        with context('si la tensión U = 30 kV'):
            with it('must be S'):
                self.ct.tension = 30
                cini = self.ct.cini
                expect(cini[6]).to(equal('S'))
        with context('si la tensión U = 33 kV'):
            with it('must be T'):
                self.ct.tension = 33
                cini = self.ct.cini
                expect(cini[6]).to(equal('T'))
    
    with context('la séptima posición'):
        with before.all:
            self.ct = CentroTransformador()
        with context('si tiene un transformador'):
            with before.all:
                self.trafo1 = Transformador()
                self.ct.transformadores = [self.trafo1]

            with it('must match letras_1trafo'):
                potencias = [0, 0.1, 20, 20.1, 37.5, 37.6, 75, 75.1,
                             130, 130.1, 205, 205.1, 325, 325.1, 515,
                             515.1, 815, 815.1, 1125, 1125.1]
                letras = ('ABBCCDDEEFFGGHHIIJJK')
                for potencia, letra in zip(potencias, letras):
                    self.trafo1.potencia = potencia
                    cini = self.ct.cini
                    expect(cini[7]).to(equal(letra))
        with context('si tiene dos transformadores'):
            with before.all:
                self.trafo1 = Transformador()
                self.trafo2 = Transformador()
                self.ct.transformadores = [self.trafo1, self.trafo2]
            with it('must match letras_2trafos'):
                potencias = [7.55, 15, 15.05, 37.5, 37.55, 75, 75.05, 130,
                             130.05, 175, 175.05, 250, 250.05, 400, 400.05, 630,
                             630.05, 1125, 1125.05]
                letras = 'LLMMNNOOPPQQRRSSTTU'
                for potencia, letra in zip(potencias, letras):
                    self.trafo1.potencia = potencia
                    self.trafo2.potencia = potencia
                    cini = self.ct.cini
                    expect(cini[7]).to(equal(letra))
        with context('si no tiene transformadores'):
            with it('must be V si no es de reparto ni reflexión'):
                self.ct.transformadores = []
                self.ct.reparto = False
                cini = self.ct.cini
                expect(cini[7]).to(equal('V'))
            with it('must be Z si es de reparto o reflexión'):
                self.ct.transformadores = []
                self.ct.reparto = True
                cini = self.ct.cini
                expect(cini[7]).to(equal('Z'))
