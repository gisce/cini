# coding=utf-8
from cini.models import *

from expects import *


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
            with context('Sección S<= 16 mm2'):
                with _it('must be A'):
                    pass
            with context('Sección 16 mm2 < S<= 25 mm2'):
                with _it('must be B'):
                    pass
            with context('Sección 25 mm2 < S<= 50 mm2'):
                with _it('must be C'):
                    pass
            with context('Sección 50 mm2 < S<= 95 mm2'):
                with _it('must be D'):
                    pass
            with context('Sección 95 mm2 < S<= 150 mm2'):
                with _it('must be E'):
                    pass
            with context('Sección 150 mm2 < S<= 240 mm2'):
                with _it('must be F'):
                    pass
            with context('Sección  240 mm2 < S<= 400 mm2'):
                with _it('must be G'):
                    pass
            with context('Sección S> 400 mm2'):
                with _it('must be H'):
                    pass
        with context('Si tensión >= 1kV'):
            with context('Sección S<= 32,4 mm2'):
                with _it('must be I'):
                    pass
            with context('Sección 32,4 mm2 < S<= 56,2 mm'):
                with _it('must be J'):
                    pass
            with context('Sección 56,2 mm2 < S<= 78,6 mm2'):
                with _it('must be K'):
                    pass
            with context('Sección 78,6 mm2 < S<= 95,1 mm2'):
                with _it('must be L'):
                    pass
            with context('Sección 95,1 mm2 < S<= 116,7 mm2'):
                with _it('must be M'):
                    pass
            with context('Sección 116,7 mm2 < S<= 152,7 mm2'):
                with _it('must be N'):
                    pass
            with context('Sección 152,7 mm2 < S<= 181,6 mm'):
                with _it('must be O'):
                    pass
            with context('Sección 181,6 mm2 < S<= 242 mm2'):
                with _it('must be P'):
                    pass
            with context('Sección 242 mm2 < S<= 290 mm2 '):
                with _it('must be Q'):
                    pass
            with context('Sección 290 mm2 < S<= 400 mm2'):
                with _it('must be R'):
                    pass
            with context('Sección 400 mm2 < S<= 500 mm2'):
                with _it('must be S'):
                    pass
            with context('Sección S > 500 mm2'):
                with _it('must be T'):
                    pass
        
    with context('La séptima posición'):
        with context('Si tensión U ≤ 0,23 kV'):
            with _it('must be A'):
                pass
        with context('Si tensión U = 0,4 kV'):
            with _it('must be B'):
                pass
        with context('Si tensión U = 1 kV'):
            with _it('must be C'):
                pass
        with context('Si tensión U = 3 kV'):
            with _it('must be D'):
                pass
        with context('Si tensión U = 5 kV'):
            with _it('must be E'):
                pass
        with context('Si tensión U = 5,5 kV'):
            with _it('must be F'):
                pass
        with context('Si tensión U = 6 kV'):
            with _it('must be G'):
                pass
        with context('Si tensión U = 6,6 kV'):
            with _it('must be H'):
                pass
        with context('Si tensión U = 10 kV'):
            with _it('must be I'):
                pass
        with context('Si tensión U = 11 kV'):
            with _it('must be J'):
                pass
        with context('Si tensión U = 12kV'):
            with _it('must be K'):
                pass
        with context('Si tensión U = 13,2 kV'):
            with _it('must be L'):
                pass
        with context('Si tensión U = 15 kV'):
            with _it('must be M'):
                pass
        with context('Si tensión U = 16 kV'):
            with _it('must be N'):
                pass
        with context('Si tensión U = 20 kV'):
            with _it('must be O'):
                pass
        with context('Si tensión U = 22 kV'):
            with _it('must be P'):
                pass
        with context('Si tensión U = 24 kV'):
            with _it('must be Q'):
                pass
        with context('Si tensión U = 25 kV'):
            with _it('must be R'):
                pass
        with context('Si tensión U = 30 kV'):
            with _it('must be S'):
                pass
        with context('Si tensión U = 33 kV'):
            with _it('must be T'):
                pass
        with context('Si tensión U = 45 kV'):
            with _it('must be U'):
                pass
        with context('Si tensión U = 50 kV'):
            with _it('must be V'):
                pass
        with context('Si tensión U = 55 kV'):
            with _it('must be W'):
                pass
        with context('Si tensión U = 66 kV'):
            with _it('must be X'):
                pass
        with context('Si tensión U = 110 kV'):
            with _it('must be Y'):
                pass
        with context('Si tensión U = 130 kV'):
            with _it('must be Z'):
                pass
        with context('Si tensión U = 132 kV'):
            with _it('must be 1'):
                pass
        with context('Si tensión U = 150 kV'):
            with _it('must be 2'):
                pass
        with context('Si no es ninguna de las anteriores (Otros)'):
            with _it('must be 5'):
                pass
