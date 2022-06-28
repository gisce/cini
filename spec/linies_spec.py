# coding=utf-8
from cini.models import *
from decimal import Decimal

from expects import *


def frange(start, end, step=0.1):
    """Floating range
    """
    step = Decimal(step)
    precision = abs(step.as_tuple().exponent)
    start = Decimal(str(round(start, precision)))
    end = Decimal(str(round(end, precision)))

    r = start
    while r < end:
        res = round(float(r), precision)
        yield res
        r += step


with description('Calculando el CINI de una Línia'):

    with description('La primera posición'):
        with it('must be 2'):
            l = Linea()
            expect(l.cini[1]).to(equal('2'))

    with description('La segunda posición'):
        with it('must be 0'):
            l = Linea()
            expect(l.cini[2]).to(equal('0'))

    with description('La tercera posición'):
        with context('Si el voltage es 110kV <= U < 220 kV'):
            with it('must be 2'):
                l = Linea()
                for x in range(110000, 220000):
                    l.tension = x
                    expect(l.cini[3]).to(equal('2'))

        with context('Si el voltage es 36kV <= U < 110 kV'):
            with it('must be 3'):
                l = Linea()
                for x in range(36000, 110000):
                    l.tension = x
                    expect(l.cini[3]).to(equal('3'))
        with context('Si el voltage es  1kV <= U < 36kV'):
            with it('must be 4'):
                l = Linea()
                for x in range(1000, 36000):
                    l.tension = x
                    expect(l.cini[3]).to(equal('4'))
        with context('Si el voltage es  U < 1kV'):
            with it('must be 5'):
                for v in range(1, 1000):
                    l = Linea()
                    l.tension = v
                    expect(l.cini[3]).to(equal('5'))

    with description('La cuarta posición'):
        with context('Si tensada sobre postes, un circuito'):
            with it('must be 1'):
                l = Linea()
                l.despliegue = 'AP'
                l.num_circuitos = 1
                expect(l.cini[4]).to(equal('1'))
        with context('Si tensada sobre postes, doble circuit'):
            with it('must be 2'):
                l = Linea()
                l.despliegue = 'AP'
                l.num_circuitos = 2
                expect(l.cini[4]).to(equal('2'))
        with context('tensada sobre postes, más de dos circuitos'):
            with it('must be 3'):
                l = Linea()
                l.despliegue = 'AP'
                l.num_circuitos = 3
                expect(l.cini[4]).to(equal('3'))
        with context('Si apoyada sobre fachada, un circuito'):
            with it('must be 4'):
                l = Linea()
                l.despliegue = 'AF'
                l.num_circuitos = 1
                expect(l.cini[4]).to(equal('4'))
        with context('Si apoyada sobre fachada, doble circuito'):
            with it('must be 5'):
                l = Linea()
                l.despliegue = 'AF'
                l.num_circuitos = 2
                expect(l.cini[4]).to(equal('5'))
        with context('Si apoyada sobre fachada, más de dos circuitos'):
            with it('must be 6'):
                l = Linea()
                l.despliegue = 'AF'
                l.num_circuitos = 3
                expect(l.cini[4]).to(equal('6'))
        with context('Si subterránea, un circuito'):
            with it('must be 7'):
                l = Linea()
                l.despliegue = 'S'
                l.num_circuitos = 1
                expect(l.cini[4]).to(equal('7'))
        with context('Si subterránea, doble circuito'):
            with it('must be 8'):
                l = Linea()
                l.despliegue = 'S'
                l.num_circuitos = 2
                expect(l.cini[4]).to(equal('8'))
        with context('Si subterránea, más de dos circuitos'):
            with it('must be 9'):
                l = Linea()
                l.despliegue = 'S'
                l.num_circuitos = 3
                expect(l.cini[4]).to(equal('9'))

    with description('La quinta posición'):
        with context('Simplex'):
            with it('must be 1'):
                l = Linea()
                l.num_conductores = 1
                expect(l.cini[5]).to(equal('1'))
        with context('Dúplex'):
            with it('must be 2'):
                l = Linea()
                l.num_conductores = 2
                expect(l.cini[5]).to(equal('2'))
        with context('Tríplex'):
            with it('must be 3'):
                l = Linea()
                l.num_conductores = 3
                expect(l.cini[5]).to(equal('3'))

    with description('La sexta posición'):
        with context('Si tensión < 1kV'):
            with before.all:
                self.linia = Linea()
                self.linia.tension = 0.400
            with context('Sección S<= 16 mm2'):
                with it('must be A'):
                    for s in range(0, 17):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('A'))
            with context('Sección 16 mm2 < S<= 25 mm2'):
                with it('must be B'):
                    for s in range(17, 26):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('B'))
            with context('Sección 25 mm2 < S<= 50 mm2'):
                with it('must be C'):
                    for s in range(26, 51):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('C'))
            with context('Sección 50 mm2 < S<= 95 mm2'):
                with it('must be D'):
                    for s in range(51, 96):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('D'))
            with context('Sección 95 mm2 < S<= 150 mm2'):
                with it('must be E'):
                    for s in range(96, 151):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('E'))
            with context('Sección 150 mm2 < S<= 240 mm2'):
                with it('must be F'):
                    for s in range(151, 241):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('F'))
            with context('Sección  240 mm2 < S<= 400 mm2'):
                with it('must be G'):
                    for s in range(241, 401):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('G'))
            with context('Sección S> 400 mm2'):
                with it('must be H'):
                    for s in [401, 500, 1000]:
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('H'))
        with context('Si tensión >= 1kV'):
            with before.all:
                self.linia = Linea()
                self.linia.tension = 20000
            with context('Sección S<= 32,4 mm2'):
                with it('must be I'):
                    for s in [10, 20, 32.4]:
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('I'))
            with context('Sección 32,4 mm2 < S<= 56,2 mm'):
                with it('must be J'):
                    for s in frange(32.5, 56.3):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('J'))
            with context('Sección 56,2 mm2 < S<= 78,6 mm2'):
                with it('must be K'):
                    for s in frange(56.3, 78.7):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('K'))
            with context('Sección 78,6 mm2 < S<= 95,1 mm2'):
                with it('must be L'):
                    for s in frange(78.7, 95.2):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('L'))
            with context('Sección 95,1 mm2 < S<= 116,7 mm2'):
                with it('must be M'):
                    for s in frange(95.2, 116.8):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('M'))
            with context('Sección 116,7 mm2 < S<= 152,7 mm2'):
                with it('must be N'):
                    for s in frange(116.8, 152.8):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('N'))
            with context('Sección 152,7 mm2 < S<= 181,6 mm'):
                with it('must be O'):
                    for s in frange(152.8, 181.7):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('O'))
            with context('Sección 181,6 mm2 < S<= 242 mm2'):
                with it('must be P'):
                    for s in frange(181.7, 242.1):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('P'))
            with context('Sección 242 mm2 < S<= 290 mm2 '):
                with it('must be Q'):
                    for s in range(243, 291):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('Q'))
            with context('Sección 290 mm2 < S<= 400 mm2'):
                with it('must be R'):
                    for s in range(291, 401):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('R'))
            with context('Sección 400 mm2 < S<= 500 mm2'):
                with it('must be S'):
                    for s in range(401, 501):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('S'))
            with context('Sección S > 500 mm2'):
                with it('must be T'):
                    for s in (501, 600, 1000):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('T'))
        
    with context('La séptima posición'):
        with before.each:
            self.linia = Linea()
        with context('Si tensión U ≤ 0,23 kV'):
            with it('must be A'):
                for v in range(230, 0, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                expect(cini[7]).to(equal('A'))
        with context('Si tensión 0,230 < U <= 0,4 kV'):
            with it('must be B'):
                for v in range(400, 230, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('B'))
        with context('Si tensión 0.4 < U <= 1 kV'):
            with it('must be C'):
                for v in range(1000, 400, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('C'))
        with context('Si tensión 1 < U <= 3 kV'):
            with it('must be D'):
                for v in range(3000, 1000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('D'))
        with context('Si tensión 3 < U <= 5 kV'):
            with it('must be E'):
                for v in range(5000, 3000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('E'))
        with context('Si tensión 5 < U <= 5,5 kV'):
            with it('must be F'):
                for v in range(5500, 5000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('F'))
        with context('Si tensión 5.5 < U <= 6 kV'):
            with it('must be G'):
                for v in range(6000, 5500, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('G'))
        with context('Si tensión 6 < U <= 6,6 kV'):
            with it('must be H'):
                for v in range(6600, 6000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('H'))
        with context('Si tensión 6.6 < U <= 10 kV'):
            with it('must be I'):
                for v in range(10000, 6600, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('I'))
        with context('Si tensión 10 < U <= 11 kV'):
            with it('must be J'):
                for v in range(11000, 10000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('J'))
        with context('Si tensión 11 < U <= 12kV'):
            with it('must be K'):
                for v in range(12000, 11000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('K'))
        with context('Si tensión 12 < U <= 13,2 kV'):
            with it('must be L'):
                for v in range(13200, 12000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('L'))
        with context('Si tensión 13,2 < U <= 15 kV'):
            with it('must be M'):
                for v in range(15000, 13200, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('M'))
        with context('Si tensión 15 < U <= 16 kV'):
            with it('must be N'):
                for v in range(16000, 15000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('N'))
        with context('Si tensión 16 < U <= 20 kV'):
            with it('must be O'):
                for v in range(20000, 16000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('O'))
        with context('Si tensión 20 < U <= 22 kV'):
            with it('must be P'):
                for v in range(22000, 20000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('P'))
        with context('Si tensión 22 < U <= 24 kV'):
            with it('must be Q'):
                for v in range(24000, 22000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('Q'))
        with context('Si tensión 24 < U <= 25 kV'):
            with it('must be R'):
                for v in range(25000, 24000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('R'))
        with context('Si tensión 25 < U <= 30 kV'):
            with it('must be S'):
                for v in range(30000, 25000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('S'))
        with context('Si tensión 30 < U <= 33 kV'):
            with it('must be T'):
                for v in range(33000, 30000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('T'))
        with context('Si tensión 33 < U <= 45 kV'):
            with it('must be U'):
                for v in range(45000, 33000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('U'))
        with context('Si tensión 45 < U <= 50 kV'):
            with it('must be V'):
                for v in range(50000, 45000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('V'))
        with context('Si tensión 50 < U <= 55 kV'):
            with it('must be W'):
                for v in range(55000, 50000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('W'))
        with context('Si tensión 55 < U <= 66 kV'):
            with it('must be X'):
                for v in range(66000, 55000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('X'))
        with context('Si tensión 66 < U <= 110 kV'):
            with it('must be Y'):
                for v in range(110000, 66000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('Y'))
        with context('Si tensión 110 < U <= 130 kV'):
            with it('must be Z'):
                for v in range(130000, 110000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('Z'))
        with context('Si tensión 130 < U <= 132 kV'):
            with it('must be 1'):
                for v in range(132000, 130000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('1'))
        with context('Si tensión 133 < U <= 150 kV'):
            with it('must be 2'):
                for v in range(150000, 133000, -1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('2'))
        with context('Si no es ninguna de las anteriores (Otros)'):
            with it('must be 5'):
                self.linia.tension = 200000
                cini = self.linia.cini
                expect(cini[7]).to(equal('5'))
