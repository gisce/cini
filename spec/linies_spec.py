# coding=utf-8
from cini.models import *

from expects import *


def frange(start, end, step=0.1):
    """Floating range
    """
    r = start
    while r < end:
        yield r
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
                for x in xrange(110, 220):
                    l.tension = x
                    expect(l.cini[3]).to(equal('2'))

        with context('Si el voltage es 36kV <= U < 110 kV'):
            with it('must be 3'):
                l = Linea()
                for x in xrange(36, 110):
                    l.tension = x
                    expect(l.cini[3]).to(equal('3'))
        with context('Si el voltage es  1kV <= U < 36kV'):
            with it('must be 4'):
                l = Linea()
                for x in xrange(1, 36):
                    l.tension = x
                    expect(l.cini[3]).to(equal('4'))
        with context('Si el voltage es  U < 1kV'):
            with it('must be 5'):
                l = Linea()
                l.tension = 0.220
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
                    for s in xrange(0, 17):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('A'))
            with context('Sección 16 mm2 < S<= 25 mm2'):
                with _it('must be B'):
                    for s in xrange(17, 26):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('B'))
            with context('Sección 25 mm2 < S<= 50 mm2'):
                with _it('must be C'):
                    for s in xrange(26, 51):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('C'))
            with context('Sección 50 mm2 < S<= 95 mm2'):
                with _it('must be D'):
                    for s in xrange(51, 96):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('D'))
            with context('Sección 95 mm2 < S<= 150 mm2'):
                with _it('must be E'):
                    for s in xrange(96, 151):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('E'))
            with context('Sección 150 mm2 < S<= 240 mm2'):
                with _it('must be F'):
                    for s in xrange(151, 241):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('F'))
            with context('Sección  240 mm2 < S<= 400 mm2'):
                with _it('must be G'):
                    for s in xrange(241, 401):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('F'))
            with context('Sección S> 400 mm2'):
                with _it('must be H'):
                    for s in [401, 500, 1000]:
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('F'))
        with context('Si tensión >= 1kV'):
            with before.all:
                self.linia = Linea()
                self.linia.tension = 20000
            with context('Sección S<= 32,4 mm2'):
                with _it('must be I'):
                    for s in [10, 20, 32.4]:
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('I'))
            with context('Sección 32,4 mm2 < S<= 56,2 mm'):
                with _it('must be J'):
                    for s in frange(32.5, 56.3):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('J'))
            with context('Sección 56,2 mm2 < S<= 78,6 mm2'):
                with _it('must be K'):
                    for s in frange(56.3, 78.6):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('K'))
            with context('Sección 78,6 mm2 < S<= 95,1 mm2'):
                with _it('must be L'):
                    for s in frange(78.6, 95.1):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('L'))
            with context('Sección 95,1 mm2 < S<= 116,7 mm2'):
                with _it('must be M'):
                    for s in frange(95.2, 116.7):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('M'))
            with context('Sección 116,7 mm2 < S<= 152,7 mm2'):
                with _it('must be N'):
                    for s in frange(116.8, 152.7):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('N'))
            with context('Sección 152,7 mm2 < S<= 181,6 mm'):
                with _it('must be O'):
                    for s in frange(152.8, 181.6):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('O'))
            with context('Sección 181,6 mm2 < S<= 242 mm2'):
                with _it('must be P'):
                    for s in frange(181.6, 243.1):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('P'))
            with context('Sección 242 mm2 < S<= 290 mm2 '):
                with _it('must be Q'):
                    for s in xrange(243, 290):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('P'))
            with context('Sección 290 mm2 < S<= 400 mm2'):
                with _it('must be R'):
                    for s in xrange(291, 400):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('R'))
            with context('Sección 400 mm2 < S<= 500 mm2'):
                with _it('must be S'):
                    for s in xrange(401, 500):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('S'))
            with context('Sección S > 500 mm2'):
                with _it('must be T'):
                    for s in (501, 600, 1000):
                        self.linia.seccion = s
                        cini = self.linia.cini
                        expect(cini[6]).to(equal('T'))
        
    with context('La séptima posición'):
        with before.each:
            self.linia = Linea()
        with context('Si tensión U ≤ 0,23 kV'):
            with _it('must be A'):
                self.linia.tension = 0.230
                cini = self.linia.cini
                expect(cini[7]).to(equal('A'))
        with context('Si tensión 0,230 < U <= 0,4 kV'):
            with _it('must be B'):
                self.linia.tension = 0.4
                cini = self.linia.cini
                expect(cini[7]).to(equal('B'))
        with context('Si tensión 0.4 < U <= 1 kV'):
            with _it('must be C'):
                for v in frange(0.5, 1.1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('C'))
        with context('Si tensión 1 < U <= 3 kV'):
            with _it('must be D'):
                for v in xrange(2, 4):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('D'))
        with context('Si tensión 3 < U <= 5 kV'):
            with _it('must be E'):
                for v in xrange(4, 6):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('E'))
        with context('Si tensión 5 < U <= 5,5 kV'):
            with _it('must be F'):
                for v in frange(5.1, 5.6):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('F'))
        with context('Si tensión 5.5 < U <= 6 kV'):
            with _it('must be G'):
                for v in frange(5.6, 6.1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('G'))
        with context('Si tensión 6 < U <= 6,6 kV'):
            with _it('must be H'):
                for v in frange(6.1, 6.7):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('H'))
        with context('Si tensión 6.6 < U <= 10 kV'):
            with _it('must be I'):
                for v in frange(6.7, 10.1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('I'))
        with context('Si tensión 10 < U <= 11 kV'):
            with _it('must be J'):
                for v in frange(10.1, 11.1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('J'))
        with context('Si tensión 11 < U <= 12kV'):
            with _it('must be K'):
                for v in frange(11.1, 12.1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('K'))
        with context('Si tensión 12 < U <= 13,2 kV'):
            with _it('must be L'):
                for v in frange(12.1, 13.3):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('L'))
        with context('Si tensión U = 15 kV'):
            with _it('must be M'):
                for v in frange(12.1, 13.3):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('L'))
        with context('Si tensión 15 < U <= 16 kV'):
            with _it('must be N'):
                for v in frange(15, 16.1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('N'))
        with context('Si tensión 16 < U <= 20 kV'):
            with _it('must be O'):
                for v in xrange(17, 21):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('O'))
        with context('Si tensión 20 < U <= 22 kV'):
            with _it('must be P'):
                for v in xrange(21, 23):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('P'))
        with context('Si tensión 22 < U <= 24 kV'):
            with _it('must be Q'):
                for v in xrange(23, 25):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('Q'))
        with context('Si tensión 24 < U <= 25 kV'):
            with _it('must be R'):
                for v in xrange(24.1, 25.1):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('R'))
        with context('Si tensión 25 < U <= 30 kV'):
            with _it('must be S'):
                for v in xrange(26, 21):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('S'))
        with context('Si tensión 30 < U <= 33 kV'):
            with _it('must be T'):
                for v in xrange(31, 34):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('T'))
        with context('Si tensión 33 < U <= 45 kV'):
            with _it('must be U'):
                for v in xrange(34, 46):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('U'))
        with context('Si tensión 45 < U <= 50 kV'):
            with _it('must be V'):
                for v in xrange(46, 51):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('V'))
        with context('Si tensión 50 < U <= 55 kV'):
            with _it('must be W'):
                for v in xrange(51, 56):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('W'))
        with context('Si tensión 55 < U <= 66 kV'):
            with _it('must be X'):
                for v in xrange(56, 67):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('X'))
        with context('Si tensión 66 < U <= 110 kV'):
            with _it('must be Y'):
                for v in xrange(67, 111):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('Y'))
        with context('Si tensión 110 < U <= 130 kV'):
            with _it('must be Z'):
                for v in xrange(111, 131):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('Z'))
        with context('Si tensión 130 < U <= 132 kV'):
            with _it('must be 1'):
                for v in xrange(131, 133):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('1'))
        with context('Si tensión 133 < U <= 150 kV'):
            with _it('must be 2'):
                for v in xrange(134, 151):
                    self.linia.tension = v
                    cini = self.linia.cini
                    expect(cini[7]).to(equal('2'))
        with context('Si no es ninguna de las anteriores (Otros)'):
            with _it('must be 5'):
                self.linia.tension = 200
                cini = self.linia.cini
                expect(cini[7]).to(equal('5'))