# coding=utf-8
from cini.models import *

from expects import *


with description('Calculando el CINI de una Subestación'):
    with description('la primera posición'):
        with it('must be 2'):
            sub = Subestacion()
            expect(sub.cini[1]).to(equal('2'))

    with description('la segunda posición'):
        with it('must be 1'):
            sub = Subestacion()
            expect(sub.cini[2]).to(equal('1'))

    with description('la tercera posición'):
        with before.each:
            self.sub = Subestacion()
        with context('si tensión primario U>=400 kV'):
            with it('must be 0'):
                for v in (400, 500, 1000):
                    self.sub.tension_p = v
                    cini = self.sub.cini
                    expect(cini[3]).to(equal('0'))
        with context('si tensión primario 220kV<=U<400 kV'):
            with it('must be 1'):
                for v in range(220, 400):
                    self.sub.tension_p = v
                    cini = self.sub.cini
                    expect(cini[3]).to(equal('1'))
        with context('si tensión primario 110kV<=U<220kV'):
            with it('must be 2'):
                for v in range(110, 220):
                    self.sub.tension_p = v
                    cini = self.sub.cini
                    expect(cini[3]).to(equal('2'))
        with context('si tensión primario 36kV<=U<110kV'):
            with it('must be 3'):
                for v in range(36, 110):
                    self.sub.tension_p = v
                    cini = self.sub.cini
                    expect(cini[3]).to(equal('3'))
        with context('si tensión primario 1kV<=U<36kV'):
            with it('must be 4'):
                for v in range(1, 36):
                    self.sub.tension_p = v
                    cini = self.sub.cini
                    expect(cini[3]).to(equal('4'))

    with description('la cuarta posición'):
        with before.each:
            self.sub = Subestacion()
        with context('si tensión secundario 110kV<=U<220kV'):
            with it('must be 2'):
                for v in range(110, 220):
                    self.sub.tension_s = v
                    cini = self.sub.cini
                    expect(cini[4]).to(equal('2'))
        with context('si la tensión secundario 36kV<=U<110kV'):
            with it('must be 3'):
                for v in range(36, 110):
                    self.sub.tension_s = v
                    cini = self.sub.cini
                    expect(cini[4]).to(equal('3'))
        with context('si la tensión secundario 1kV<=U<36kV'):
            with it('must be 4'):
                for v in range(1, 36):
                    self.sub.tension_s = v
                    cini = self.sub.cini
                    expect(cini[4]).to(equal('4'))

    with description('la quinta posición'):
        with before.each:
            self.sub = Subestacion()
        with context('si el tipo es Convencional (C)'):
            with it('must be 1'):
                self.sub.tipo = 'C'
                cini = self.sub.cini
                expect(cini[5]).to(equal('1'))
        with context('si el tipo es Blindada (B)'):
            with it('must be 2'):
                self.sub.tipo = 'B'
                cini = self.sub.cini
                expect(cini[5]).to(equal('2'))
        with context('si el tipo es Móvil (M)'):
            with it('must be 3'):
                self.sub.tipo = 'M'
                cini = self.sub.cini
                expect(cini[5]).to(equal('3'))
    
    with description('la sexta posición'):
        with context('si no es de reparto'):
            with before.each:
                self.sub = Subestacion()
                self.sub.reparto = False
                self.trafo = Transformador()
                self.trafo.estado = 'S'
                self.sub.transformadores.append(self.trafo)
            with context('si la potencia instalada es S<5 MVA'):
                with it('must be A'):
                    for p in range(1, 5):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('A'))
            with context('si la potencia instalada es 5<=S<10 MVA'):
                with it('must be B'):
                    for p in range(5, 10):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('B'))
            with context('si la potencia instalada es 10<=S<15 MVA'):
                with it('must be C'):
                    for p in range(10, 15):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('C'))
            with context('si la potencia instalada es 15<=S<20 MVA'):
                with it('must be D'):
                    for p in range(15, 20):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('D'))
            with context('si la potencia instalada es 20<=S<25 MVA'):
                with it('must be E'):
                    for p in range(20, 25):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('E'))
            with context('si la potencia instalada es 25<=S<30 MVA'):
                with it('must be F'):
                    for p in range(25, 30):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('F'))
            with context('si la potencia instalada es 30<=S<40 MVA'):
                with it('must be G'):
                    for p in range(30, 40):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('G'))
            with context('si la potencia instalada es 40<=S<60 MVA'):
                with it('must be H'):
                    for p in range(40, 60):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('H'))
            with context('si la potencia instalada es 60<=S<80 MVA'):
                with it('must be I'):
                    for p in range(60, 80):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('I'))
            with context('si la potencia instalada es 80<=S<100 MVA'):
                with it('must be J'):
                    for p in range(80, 100):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('J'))
            with context('si la potencia instalada es 100<=S<120 MVA'):
                with it('must be K'):
                    for p in range(100, 120):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('K'))
            with context('si la potencia instalada es 120<=S<150 MVA'):
                with it('must be L'):
                    for p in range(120, 150):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('L'))
            with context('si la potencia instalada es 150<=S<200 MVA'):
                with it('must be N'):
                    for p in range(150, 200):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('N'))
            with context('si la potencia instalada es 200<=S<250 MVA'):
                with it('must be O'):
                    for p in range(200, 250):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('O'))
            with context('si la potencia instalada es 250<=S<300 MVA'):
                with it('must be P'):
                    for p in range(250, 300):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('P'))
            with context('si la potencia instalada es 300<=S<350 MVA'):
                with it('must be Q'):
                    for p in range(300, 350):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('Q'))
            with context('si la potencia instalada es 350<=S<400 MVA'):
                with it('must be R'):
                    for p in range(350, 400):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('R'))
            with context('si la potencia instalada es S>=400 MVA'):
                with it('must be S'):
                    for p in (400, 1000, 4000):
                        self.trafo.potencia = p
                        cini = self.sub.cini
                        expect(cini[6]).to(equal('S'))

        with context('si es de reparto'):
            with it('must be Z'):
                sub = Subestacion()
                sub.reparto = True
                cini = sub.cini
                expect(cini[6]).to(equal('Z'))

    with description('la séptima posición'):
        with it('must be 0'):
            sub = Subestacion()
            cini = sub.cini
            expect(cini[7]).to(equal('0'))
