# coding=utf-8
from cini.models import *

from expects import *


with description('Calculando un CINI de un transformador'):
    with description('la primera posición'):
        with it('must be 2'):
            t = Transformador()
            expect(t.cini[1]).to(equal('2'))

    with description('la segunda posición'):
        with it('must be 7'):
            t = Transformador()
            expect(t.cini[2]).to(equal('7'))

    with description('la tercera posición'):
        with before.all:
            self.trafo = Transformador()
        with context('Si la tensión primaria >= 400 kV'):
            with it('must be 0'):
                for v in (400, 500, 1000):
                    self.trafo.tension_p = v
                    cini = self.trafo.cini
                    expect(cini[3]).to(equal('0'))
        with context('Si la tensión primaria 220kV<=U<400 kV'):
            with it('must be 1'):
                for v in range(220, 400):
                    self.trafo.tension_p = v
                    cini = self.trafo.cini
                    expect(cini[3]).to(equal('1'))
        with context('Si la tensión primaria 110kV<=U<220kV'):
            with it('must be 2'):
                for v in range(110, 220):
                    self.trafo.tension_p = v
                    cini = self.trafo.cini
                    expect(cini[3]).to(equal('2'))
        with context('Si la tensión primaria 36kV<=U<110kV'):
            with it('must be 3'):
                for v in range(36, 110):
                    self.trafo.tension_p = v
                    cini = self.trafo.cini
                    expect(cini[3]).to(equal('3'))
        with context('Si la tensión primaria 1kV<=U<36kV'):
            with it('must be 4'):
                for v in range(1, 36):
                    self.trafo.tension_p = v
                    cini = self.trafo.cini
                    expect(cini[3]).to(equal('4'))

    with description('la cuarta posición'):
        with before.all:
            self.trafo = Transformador()
        with context('Si la tensión secundaria 110kV<=U<220kV'):
            with it('must be 2'):
                for v in range(110, 220):
                    self.trafo.tension_p = v
                    self.trafo.tension_s = v
                    cini = self.trafo.cini
                    expect(cini[4]).to(equal('2'))
        with context('Si la tensión secundaria 36kV<=U<110kV'):
            with it('must be 3'):
                for v in range(36, 110):
                    self.trafo.tension_p = v
                    self.trafo.tension_s = v
                    cini = self.trafo.cini
                    expect(cini[4]).to(equal('3'))
        with context('Si la tensión secundaria 1kV<=U<36kV'):
            with it('must be 4'):
                for v in range(1, 36):
                    self.trafo.tension_p = v
                    self.trafo.tension_s = v
                    cini = self.trafo.cini
                    expect(cini[4]).to(equal('4'))
        with context('Si la tensión secundaria U < 1 Kv'):
            with it('must be 5'):
                self.trafo.tension_p = 0.400
                self.trafo.tension_s = 0.400
                cini = self.trafo.cini
                expect(cini[4]).to(equal('5'))
    
    with description('la quinta posición'):
        with before.all:
            self.trafo = Transformador()
        with context('si está en una subestación'):
            with it('must be 1'):
                self.trafo.situacion = 'SE'
                cini = self.trafo.cini
                expect(cini[5]).to(equal('1'))
        with context('si está en un centro de transformación'):
            with it('must be 2'):
                self.trafo.situacion = 'CT'
                cini = self.trafo.cini
                expect(cini[5]).to(equal('2'))
    
    with description('la sexta posición'):
        with before.all:
            self.trafo = Transformador()
        with context('si la potencia S<1 MVA'):
            with it('must be A'):
                self.trafo.potencia = 0.05
                cini = self.trafo.cini
                expect(cini[6]).to(equal('A'))
        with context('si la potencia 1<=S<5 MVA'):
            with it('must be B'):
                for v in range(1, 5):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('B'))
        with context('si la potencia 5<=S<10 MVA'):
            with it('must be C'):
                for v in range(5, 10):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('C'))
        with context('si la potencia 10<=S<15 MVA'):
            with it('must be D'):
                for v in range(10, 15):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('D'))
        with context('si la potencia 15<=S<20 MVA'):
            with it('must be E'):
                for v in range(15, 20):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('E'))
        with context('si la potencia 20<=S<25 MVA'):
            with it('must be F'):
                for v in range(20, 25):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('F'))
        with context('si la potencia 25<=S<30 MVA'):
            with it('must be G'):
                for v in range(25, 30):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('G'))
        with context('si la potencia 30<=S<40 MVA'):
            with it('must be H'):
                for v in range(30, 40):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('H'))
        with context('si la potencia 40<=S<60 MVA'):
            with it('must be I'):
                for v in range(40, 60):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('I'))
        with context('si la potencia 60<=S<80 MVA'):
            with it('must be J'):
                for v in range(60, 80):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('J'))
        with context('si la potencia 80<=S<100 MVA'):
            with it('must be K'):
                for v in range(80, 100):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('K'))
        with context('si la potencia 100<=S<120 MVA'):
            with it('must be L'):
                for v in range(100, 120):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('L'))
        with context('si la potencia 120<=S<150 MVA'):
            with it('must be M'):
                for v in range(120, 150):
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('M'))
        with context('si la potencia S>=150 MVA'):
            with it('must be N'):
                for v in [150]:
                    self.trafo.potencia = v
                    cini = self.trafo.cini
                    expect(cini[6]).to(equal('N'))

    with description('la séptima posición'):
        with before.all:
            self.trafo = Transformador()
        with context('si el trafo en servicio'):
            with it('must be 0'):
                self.trafo.estado = 'S'
                cini = self.trafo.cini
                expect(cini[7]).to(equal('0'))
        with context('si el trafo en reserva'):
            with it('must be 1'):
                self.trafo.estado = 'R'
                cini = self.trafo.cini
                expect(cini[7]).to(equal('1'))
        with context('si el trafo es móvil'):
            with it('must be 2'):
                self.trafo.estado = 'M'
                cini = self.trafo.cini
                expect(cini[7]).to(equal('2'))
