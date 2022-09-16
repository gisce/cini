# coding=utf-8
from cini.models import *
from expects import *

with description('Calculando un CINI de un generador'):
    with description('la primera posición'):
        with it('debe ser 4'):
            g = Generador()
            expect(g.cini[1]).to(equal('4'))
            
    with description('la segunda posición'):
        with it('debe ser 3'):
            g = Generador()
            expect(g.cini[2]).to(equal('3'))
            
    with description('la quinta posición'):
        with it('debe ser 0'):
            g = Generador()
            expect(g.cini[5]).to(equal('0'))
            
    with description('la séptima posición'):
        with it('debe ser 0'):
            g = Generador()
            expect(g.cini[7]).to(equal('0'))

    with description('la tercera posición'):
        with before.all:
            self.generador = Generador()
        with context('Si la tensión 110kV<=U<220kV'):
            with it('debe ser 2'):
                for v in range(110000, 220000, 1000):
                    self.generador.tension = v
                    cini = self.generador.cini
                    expect(cini[3]).to(equal('2'))
        with context('Si la tensión 36kV<=U<110kV'):
            with it('debe ser 3'):
                for v in range(36000, 110000, 1000):
                    self.generador.tension = v
                    cini = self.generador.cini
                    expect(cini[3]).to(equal('3'))
        with context('Si la tensión 1kV<=U<36kV'):
            with it('sebe ser 4'):
                for v in range(1000, 36000, 1000):
                    self.generador.tension = v
                    cini = self.generador.cini
                    expect(cini[3]).to(equal('4'))
        with context('Si la tensión U < 1kV'):
            with it('sebe ser 5'):
                for v in range(100, 1000, 100):
                    self.generador.tension = v
                    cini = self.generador.cini
                    expect(cini[3]).to(equal('5'))

    with description('la cuarta posición'):
            with before.all:
                self.generador = Generador()
            with context('si la tecnologia es a11'):
                with it('debe ser 2'):
                    self.generador.tecnologia = 'a11'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('2'))
            with context('si la tecnologia es a12'):
                with it('debe ser 2'):
                    self.generador.tecnologia = 'a12'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('2'))
            with context('si la tecnologia es a13'):
                with it('debe ser 2'):
                    self.generador.tecnologia = 'a13'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('2'))
            with context('si la tecnologia es a20'):
                with it('debe ser 4'):
                    self.generador.tecnologia = 'a20'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('4'))
            with context('si la tecnologia es b11'):
                with it('debe ser 5'):
                    self.generador.tecnologia = 'b11'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('5'))
            with context('si la tecnologia es b12'):
                with it('debe ser 9'):
                    self.generador.tecnologia = 'b12'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('9'))
            with context('si la tecnologia es b21'):
                with it('debe ser 7'):
                    self.generador.tecnologia = 'b21'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('7'))
            with context('si la tecnologia es b22'):
                with it('debe ser 8'):
                    self.generador.tecnologia = 'b22'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('8'))
            with context('si la tecnologia es b30'):
                with it('debe ser 9'):
                    self.generador.tecnologia = 'b30'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('9'))
            with context('si la tecnologia es b41'):
                with it('debe ser 1'):
                    self.generador.tecnologia = 'b41'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('1'))
            with context('si la tecnologia es b42'):
                with it('debe ser 1'):
                    self.generador.tecnologia = 'b42'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('1'))
            with context('si la tecnologia es b51'):
                with it('debe ser 1'):
                    self.generador.tecnologia = 'b51'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('1'))
            with context('si la tecnologia es b52'):
                with it('debe ser 1'):
                    self.generador.tecnologia = 'b52'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('1'))
            with context('si la tecnologia es b60'):
                with it('debe ser 3'):
                    self.generador.tecnologia = 'b60'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('3'))
            with context('si la tecnologia es b71'):
                with it('debe ser 9'):
                    self.generador.tecnologia = 'b71'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('9'))
            with context('si la tecnologia es b72'):
                with it('debe ser 9'):
                    self.generador.tecnologia = 'b72'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('9'))
            with context('si la tecnologia es b80'):
                with it('debe ser 3'):
                    self.generador.tecnologia = 'b80'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('3'))
            with context('si la tecnologia es c10'):
                with it('debe ser 4'):
                    self.generador.tecnologia = 'c10'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('4'))
            with context('si la tecnologia es c20'):
                with it('debe ser 4'):
                    self.generador.tecnologia = 'c20'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('4'))
            with context('si la tecnologia es c30'):
                with it('debe ser 9'):
                    self.generador.tecnologia = 'c30'
                    cini = self.generador.cini
                    expect(cini[4]).to(equal('9'))

    with description('la sexta posición'):
        with before.all:
            self.generador = Generador()
        with context('si la potencia S<=1 MVA'):
            with it('debe ser A'):
                for v in range(1, 1000, 100):
                    self.generador.potencia = v
                    cini = self.generador.cini
                    expect(cini[6]).to(equal('A'))
        with context('si la potencia 1<S<=2 MVA'):
            with it('debe ser B'):
                for v in range(2000, 1000, -100):
                    self.generador.potencia = v
                    cini = self.generador.cini
                    expect(cini[6]).to(equal('B'))
        with context('si la potencia 2<S<=5 MVA'):
            with it('debe ser C'):
                for v in range(5000, 2000, -200):
                    self.generador.potencia = v
                    cini = self.generador.cini
                    expect(cini[6]).to(equal('C'))
        with context('si la potencia 5<S<=10 MVA'):
            with it('debe ser D'):
                for v in range(10000, 5000, -500):
                    self.generador.potencia = v
                    cini = self.generador.cini
                    expect(cini[6]).to(equal('D'))
        with context('si la potencia 10<S<15 MVA'):
            with it('debe ser E'):
                for v in range(14950, 10000, -250):
                    self.generador.potencia = v
                    cini = self.generador.cini
                    expect(cini[6]).to(equal('E'))
        with context('si la potencia 15<=S<20 MVA'):
            with it('debe ser F'):
                for v in range(15000, 20000):
                    self.generador.potencia = v
                    cini = self.generador.cini
                    expect(cini[6]).to(equal('F'))
        with context('si la potencia 20<=S<25 MVA'):
            with it('debe ser G'):
                for v in range(20000, 25000):
                    self.generador.potencia = v
                    cini = self.generador.cini
                    expect(cini[6]).to(equal('G'))
        with context('si la potencia 25<=S<30 MVA'):
            with it('debe ser H'):
                for v in range(25000, 30000):
                    self.generador.potencia = v
                    cini = self.generador.cini
                    expect(cini[6]).to(equal('H'))
        with context('si la potencia 30<=S<40 MVA'):
            with it('debe ser I'):
                for v in range(30000, 40000):
                    self.generador.potencia = v
                    cini = self.generador.cini
                    expect(cini[6]).to(equal('I'))
        with context('si la potencia S>=40 MVA'):
            with it('debe ser J'):
                for v in range(40000, 100000, 10000):
                    self.generador.potencia = v
                    cini = self.generador.cini
                    expect(cini[6]).to(equal('J'))
