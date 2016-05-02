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
        raise NotImplementedError


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
        """Obtiene el CINI de la linea
        :returns :py:class:`CINI`
        """
        c = CINI()
        c.positions[1] = '2'
        c.positions[2] = '0'
        if self.tension is not None:
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

        if self.tension is not None:
            if self.tension < 1000:
                if self.seccion <= 16:
                    c.positions[6] = 'A'
                elif 16 < self.seccion <= 25:
                    c.positions[6] = 'B'
                elif 25 < self.seccion <= 50:
                    c.positions[6] = 'C'
                elif 50 < self.seccion <= 95:
                    c.positions[6] = 'D'
                elif 95 < self.seccion <= 150:
                    c.positions[6] = 'E'
                elif 150 < self.seccion <= 240:
                    c.positions[6] = 'F'
                elif 240 < self.seccion <= 400:
                    c.positions[6] = 'G'
                elif self.seccion > 400:
                    c.positions[6] = 'H'
            elif self.tension >= 1000:
                if round(self.seccion, 1) <= 32.4:
                    c.positions[6] = 'I'
                elif 32.4 < round(self.seccion, 1) <= 56.2:
                    c.positions[6] = 'J'
                elif 56.2 < round(self.seccion, 1) <= 78.6:
                    c.positions[6] = 'K'
                elif 78.6 < round(self.seccion, 1) <= 95.1:
                    c.positions[6] = 'L'
                elif 95.1 < round(self.seccion, 1) <= 116.7:
                    c.positions[6] = 'M'
                elif 116.7 < round(self.seccion, 1) <= 152.7:
                    c.positions[6] = 'N'
                elif 152.7 < round(self.seccion, 1) <= 181.6:
                    c.positions[6] = 'O'
                elif 181.6 < round(self.seccion, 1) <= 242.0:
                    c.positions[6] = 'P'
                elif 242 < self.seccion <= 290:
                    c.positions[6] = 'Q'
                elif 290 < self.seccion <= 400:
                    c.positions[6] = 'R'
                elif 400 < self.seccion <= 500:
                    c.positions[6] = 'S'
                elif self.seccion > 500:
                    c.positions[6] = 'T'

            if round(self.tension, 3) <= 0.230:
                c.positions[7] = 'A'
            elif 0.230 < round(self.tension, 3) <= 0.4:
                c.positions[7] = 'B'
            elif 0.4 < round(self.tension, 3) <= 1.0:
                c.positions[7] = 'C'
            elif 1 < self.tension <= 3:
                c.positions[7] = 'D'
            elif 3 < self.tension <= 5:
                c.positions[7] = 'E'
            elif 5 <= round(self.tension, 1) <= 5.5:
                c.positions[7] = 'F'
            elif 5.5 < round(self.tension, 1) <= 6.0:
                c.positions[7] = 'G'
            elif 6.0 < round(self.tension, 1) <= 6.6:
                c.positions[7] = 'H'
            elif 6.6 < round(self.tension, 1) <= 10:
                c.positions[7] = 'I'
            elif 10 < round(self.tension, 1) <= 11:
                c.positions[7] = 'J'
            elif 11 < round(self.tension, 1) <= 12:
                c.positions[7] = 'K'
            elif 12 < round(self.tension, 1) <= 13.2:
                c.positions[7] = 'L'
            elif self.tension == 15:
                c.positions[7] = 'M'
            elif 15 < round(self.tension, 1) <= 16:
                c.positions[7] = 'N'
            elif 16 < self.tension <= 20:
                c.positions[7] = 'O'
            elif 20 < self.tension <= 22:
                c.positions[7] = 'P'
            elif 22 < self.tension <= 24:
                c.positions[7] = 'Q'
            elif 24 < round(self.tension, 1) <= 25:
                c.positions[7] = 'R'
            elif 25 < self.tension <= 30:
                c.positions[7] = 'S'
            elif 30 < self.tension <= 33:
                c.positions[7] = 'T'
            elif 33 < self.tension <= 45:
                c.positions[7] = 'U'
            elif 45 < self.tension <= 50:
                c.positions[7] = 'V'
            elif 50 < self.tension <= 55:
                c.positions[7] = 'W'
            elif 55 < self.tension <= 66:
                c.positions[7] = 'X'
            elif 66 < self.tension <= 110:
                c.positions[7] = 'Y'
            elif 110 < self.tension <= 130:
                c.positions[7] = 'Z'
            elif 130 < self.tension <= 132:
                c.positions[7] = '1'
            elif 133 < self.tension <= 150:
                c.positions[7] = '2'
            else:
                c.positions[7] = '5'

        return c


class Transformador(Base):
    """
    Objeto que representa un transformador.
    """
    def __init__(self):
        pass