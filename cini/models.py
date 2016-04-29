# coding=utf-8
"""
Modelos de datos básicos para calcular los CINIS.
"""


class CINI(object):
    """
    Objeto CINI

    Tiene ocho posiciones y longitud de ocho, la posición 0 siempre es el
    prefijo ``I``.

    Se puede acceder a las posiciones como si se tratara de una lista y la
    representación de string es la concatenación de las ocho posiciones.::

        cini = CINI()
        cini[0]   # El valor es 'I'
        len(cini)  # El valor es 8
        str(cini)  # 'IXXXXXXX'
    """
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
        """
        Obtención del CINI del objeto

        :return: :py:class:`CINI`
        """
        raise NotImplemented


class Linea(Base):
    """
    Objeto que representa una linea.

    Podemos obtener el CINI de una linea creando un objeto linea, asignando
    los valores correspondientes y accediendo a la propiedada `cini`.::

        linea = Linea()
        linea.tension = 110
        linea.num_circuitos = 2
        linea.num_conductores = 1
        linea.seccion = 80
        linea.despliegue = 'AP'
        str(linea.cini)  # 'I20221LY'
    """
    def __init__(self):
        self.tension = None
        """Tension en kV
        """
        self.num_circuitos = None
        """Número de circuitos
        """
        self.num_conductores = None
        """Número de conductores
        """
        self.seccion = None
        """Sección del cable en mm²
        """
        self.despliegue = None
        """Despliegue de la linea:

            - Tensada sobre postes: ``AP``
            - Apoyada sobre fachada: ``AF``
            - Subterránea: ``S``
        """

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

        if self.num_conductores == 1:
            c.positions[5] = '1'
        elif self.num_conductores == 2:
            c.positions[5] = '2'
        elif self.num_conductores == 3:
            c.positions[5] = '3'

        if self.tension < 1000:
            if self.seccion <= 16:
                c.positions[6] = 'A'

        return c
