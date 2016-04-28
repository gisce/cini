# coding=utf-8
"""
Modelos de datos básicos para calcular los CINIS.
"""


class CINI(object):
    def __init__(self):
        self.positions = [' '] * 8
        self.positions[0] = 'I'

    def __getitem__(self, index):
        return self.positions[index]

    def __str__(self):
        return ''.join(self.positions)


class Base(object):
    """
    Base object
    """
    @property
    def cini(self):
        raise NotImplemented


class Linea(Base):
    def __init__(self):
        self.tension = None
        self.num_circuitos = None
        self.seccion = None
        self.despliegue = None

    @property
    def cini(self):
        c = CINI()
        c.positions[1] = '2'
        c.positions[2] = '0'
        if 110 <= self.tension < 220:
            c.positions[3] = '2'
        elif 36 <= self.tension < 110:
            c.positions[3] = '3'
        elif 1 <= self.tension < 36:
            c.positions[3] = '4'
        elif self.tension < 1:
            c.positions[3] = '5'

        if self.despliegue == 'AP':
            if self.num_circuitos == 1:
                c.positions[4] = '1'
            elif self.num_circuitos == 2:
                c.positions[4] = '2'
            elif self.num_circuitos > 2:
                c.positions[4] = '3'
        elif self.despliegue == 'AF':
            if self.num_circuitos == 1:
                c.positions[4] = '4'
            elif self.num_circuitos == 2:
                c.positions[4] = '5'
            elif self.num_circuitos > 2:
                c.positions[4] = '6'
        elif self.despliegue == 'S':
            if self.num_circuitos == 1:
                c.positions[4] = '7'
            elif self.num_circuitos == 2:
                c.positions[4] = '8'
            elif self.num_circuitos > 2:
                c.positions[4] = '9'
        return c
