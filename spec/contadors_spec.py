# coding=utf-8
from cini.models import Contador

from expects import *

with description('Calculando un CINI de un Contador'):
    with description('la primera posición'):
        with it('must be 3'):
            c = Contador()
            expect(c.cini[1]).to(equal('3'))

    with description('la segunda posición'):
        with it('must be 1'):
            c = Contador()
            expect(c.cini[2]).to(equal('1'))

    with description('la tercera posición'):
        with it('must be 0'):
            c = Contador()
            expect(c.cini[3]).to(equal('0'))

    with description('la cuarta posición'):
        with before.all:
            self.c = Contador()
        with context('Si el contador es propiedad del cliente'):
            with it('must be 2'):
                self.c.propiedad = 'client'
                cini = self.c.cini
                expect(cini[4]).to(equal('2'))
        with context('Si el contador es propiedad de la empresa'):
            with it('must be 1'):
                self.c.propiedad = 'empresa'
                cini = self.c.cini
                expect(cini[4]).to(equal('1'))

    with description('la quinta posición'):
        with before.all:
            self.c = Contador()
        with context('Si el contador es tipo 4 y la tecnologia es prime'):
            with it('must be 2'):
                self.c.tipo_agree = '4'
                self.c.tecnologia = 'prime'
                cini = self.c.cini
                expect(cini[5]).to(equal('2'))
        with context('Si el contador es tipo 4 y la tecnologia no es prime'):
            with it('must be 1'):
                self.c.tipo_agree = '4'
                self.c.tecnologia = 'otra'
                cini = self.c.cini
                expect(cini[5]).to(equal('1'))
        with context('Si el contador es tipo 2'):
            with it('must be 2'):
                self.c.tipo_agree = '2'
                cini = self.c.cini
                expect(cini[5]).to(equal('2'))
        with context('Si el contador es tipo 3 y es telegestionado'):
            with it('must be 2'):
                self.c.tipo_agree = '3'
                self.c.telegestionado = True
                cini = self.c.cini
                expect(cini[5]).to(equal('2'))
        with context('Si el contador es tipo 3, no es telegestionado y la '
                     'tecnologia es telemeasure'):
            with it('must be 2'):
                self.c.tipo_agree = '3'
                self.c.telegestionado = False
                self.c.tecnologia = 'telemeasure'
                cini = self.c.cini
                expect(cini[5]).to(equal('2'))
        with context('Si el contador es tipo 3 y no es telegestionado'):
            with it('must be 1'):
                self.c.tipo_agree = '3'
                self.c.telegestionado = False
                cini = self.c.cini
                expect(cini[5]).to(equal('1'))
        with context('Si el contador es tipo 5 y la tecnologia es prime'):
            with it('must be 3'):
                self.c.tipo_agree = '5'
                self.c.tecnologia = 'prime'
                cini = self.c.cini
                expect(cini[5]).to(equal('3'))
        with context('Si el contador es tipo 5 y la tecnologia no es prime'):
            with it('must be 1'):
                self.c.tipo_agree = '5'
                self.c.tecnologia = 'otra'
                cini = self.c.cini
                expect(cini[5]).to(equal('1'))

    with description('la sexta posición'):
        with before.all:
            self.c = Contador()
        with context('Si el contador es tipo 2'):
            with it('must be L'):
                self.c.tipo_agree = '2'
                cini = self.c.cini
                expect(cini[6]).to(equal('L'))
        with context('Si el contador es tipo 3 y la tarifa es BT'):
            with it('must be M'):
                self.c.tipo_agree = '3'
                self.c.tipo_tarifa = 'BT'
                cini = self.c.cini
                expect(cini[6]).to(equal('M'))
        with context('Si el contador es tipo 3 y la tarifa es AT'):
            with it('must be N'):
                self.c.tipo_agree = '3'
                self.c.tipo_tarifa = 'AT'
                cini = self.c.cini
                expect(cini[6]).to(equal('N'))
        with context('Si el contador es tipo 4'):
            with it('must be O'):
                self.c.tipo_agree = '4'
                cini = self.c.cini
                expect(cini[6]).to(equal('O'))
        with context('Si el contador es tipo 5 y monofasico'):
            with it('must be P'):
                self.c.tipo_agree = '5'
                self.c.fases = 'monofasico'
                cini = self.c.cini
                expect(cini[6]).to(equal('P'))
        with context('Si el contador es tipo 5 y trifasico'):
            with it('must be Q'):
                self.c.tipo_agree = '5'
                self.c.fases = 'trifasico'
                cini = self.c.cini
                expect(cini[6]).to(equal('Q'))
        with context('Si el contador no cumple ninguna de las anteriores '
                     'condicions'):
            with it('must be U'):
                self.c.tipo_agree = 'otro'
                self.c.fases = 'otro'
                cini = self.c.cini
                expect(cini[6]).to(equal('U'))

    with description('la séptima posición'):
        with it('must be 0'):
            c = Contador()
            expect(c.cini[7]).to(equal('0'))
