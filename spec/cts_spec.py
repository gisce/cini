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
                self.ct.transformadores.append(self.trafo1)
            with context('si la potencia = 0 kVA'):
                with it('must be A'):
                    self.trafo1.potencia = 0
                    cini = self.ct.cini
                    expect(cini[7]).to(equal('A'))
            with context('si la potencia 0 < p <= 15 kVA'):
                with it('must be B'):
                    for v in range(1, 16):
                        self.trafo1.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('B'))
            with context('si la potencia 0 < p < 20 kVA'):
                with it('must be B'):
                    for v in range(1, 20):
                        self.trafo1.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('B'))
            with context('si la potencia 20 <= p < 37.5 kVA'):
                with it('must be C'):
                    for v in range(20, 38):
                        self.trafo1.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('C'))
                    self.trafo1.potencia = 37.4
                    cini = self.ct.cini
                    expect(cini[7]).to(equal('C'))
            with context('si la potencia 37.5 <= p < 75 kVA'):
                with it('must be D'):
                    self.trafo1.potencia = 37.5
                    cini = self.ct.cini
                    expect(cini[7]).to(equal('C'))
                    for v in range(38, 75):
                        self.trafo1.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('D'))
            with context('si la potencia 75 <= p < 130 kVA'):
                with it('must be E'):
                    for v in range(75, 130):
                        self.trafo1.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('E'))
            with context('si la potencia 130 <= p < 205 kVA'):
                with it('must be F'):
                    for v in range(130, 205):
                        self.trafo1.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('F'))
            with context('si la potencia 205 <= p < 325 kVA'):
                with it('must be G'):
                    for v in range(205, 325):
                        self.trafo1.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('G'))
            with context('si la potencia 325 <= p < 515 kVA'):
                with it('must be H'):
                    for v in range(325, 515):
                        self.trafo1.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('H'))
            with context('si la potencia 515 <= p < 815 kVA'):
                with it('must be I'):
                    for v in range(515, 815):
                        self.trafo1.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('I'))
            with context('si la potencia 815 <= p < 1125 kVA'):
                with it('must be J'):
                    for v in range(815, 1125):
                        self.trafo1.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('J'))
            with context('si la potencia 1125 <= p <= 1250 kVA'):
                with it('must be K'):
                    for v in range(1125, 1251):
                        self.trafo1.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('K'))
        with context('si tiene 2 transformadores'):
            with before.all:
                self.trafo1 = Transformador()
                self.trafo2 = Transformador()
                self.ct.transformadores = [self.trafo1, self.trafo2]
            with context('si la potencia <= 2x15 kVA'):
                with it('must be L'):
                    self.trafo1.potencia = 15
                    self.trafo2.potencia = 15
                    cini = self.ct.cini
                    expect(cini[7]).to(equal('L'))
            with context('si la potencia 2x15 < p <= 2x25 kVA'):
                with it('must be M'):
                    for v in range(16, 26):
                        self.trafo1.potencia = v
                        self.trafo2.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('M'))
            with context('si la potencia 2x25 < p <= 2x50 kVA'):
                with it('must be N'):
                    for v in range(26, 51):
                        self.trafo1.potencia = v
                        self.trafo2.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('N'))
            with context('si la potencia 2x50 < p <= 2x100 kVA'):
                with it('must be O'):
                    for v in range(51, 101):
                        self.trafo1.potencia = v
                        self.trafo2.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('O'))
            with context('si la potencia 2x100 < p <= 2x160 kVA'):
                with it('must be P'):
                    for v in range(101, 161):
                        self.trafo1.potencia = v
                        self.trafo2.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('P'))
            with context('si la potencia 2x160 < p <= 2x250 kVA'):
                with it('must be Q'):
                    for v in range(161, 251):
                        self.trafo1.potencia = v
                        self.trafo2.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('Q'))
            with context('si la potencia 2x250 < p <= 2x400 kVA'):
                with it('must be R'):
                    for v in range(251, 401):
                        self.trafo1.potencia = v
                        self.trafo2.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('R'))
            with context('si la potencia 2x400 < p <= 2x630 kVA'):
                with it('must be S'):
                    for v in range(401, 631):
                        self.trafo1.potencia = v
                        self.trafo2.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('S'))
            with context('si la potencia 2x630 < p <= 2x1000 kVA'):
                with it('must be T'):
                    for v in range(631, 1001):
                        self.trafo1.potencia = v
                        self.trafo2.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('T'))
            with context('si la potencia 2x1000 < p <= 2x1250 kVA'):
                with it('must be U'):
                    for v in range(1001, 1251):
                        self.trafo1.potencia = v
                        self.trafo2.potencia = v
                        cini = self.ct.cini
                        expect(cini[7]).to(equal('U'))
        with context('Si no tiene ningún transformador'):
            with context('si no es de reparto o reflexión'):
                with it('must be V'):
                    self.ct.transformadores = []
                    self.ct.reparto = True
                    cini = self.ct.cini
                    expect(cini[7]).to(equal('V'))
            with context('si es de reparto o reflexión'):
                with it('must be Z'):
                    self.ct.transformadores = []
                    self.ct.reparto = False
                    cini = self.ct.cini
                    expect(cini[7]).to(equal('Z'))
