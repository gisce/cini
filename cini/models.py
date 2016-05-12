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
        self.tension_p = None
        """Tension primaria en kV
        """
        self.tension_s = None
        """Tension primaria en kV
        """
        self.situacion = None
        """Situación del trado

            - En subestación = 'SE'
            - En centro de transformación = 'CT'
        """
        self.potencia = None
        """Potencia en MVA
        """
        self.estado = None
        """Estado del trafo

            - Trafo en servicio = 'S'
            - Trafo de reserva = 'R'
            - Trafo móvil = 'M'
        """

    @property
    def cini(self):
        """Obtiene el CINI del transformador
        :returns :py:class:`CINI`
        """
        c = CINI()
        c.positions[1] = '2'
        c.positions[2] = '7'

        if self.tension_p is not None:
            if self.tension_p >= 400:
                c.positions[3] = '0'
            elif 220 <= self.tension_p < 400:
                c.positions[3] = '1'
            elif 110 <= self.tension_p < 220:
                c.positions[3] = '2'
            elif 36 <= self.tension_p < 110:
                c.positions[3] = '3'
            elif 1 <= self.tension_p < 36:
                c.positions[3] = '4'
            if 1 <= self.tension_s < 36:
                c.positions[4] = '4'
            elif 36 <= self.tension_s < 110:
                c.positions[4] = '3'
            elif 110 <= self.tension_s < 220:
                c.positions[4] = '2'
            elif self.tension_s < 1:
                c.positions[4] = '5'

        if self.situacion == 'SE':
            c.positions[5] = '1'
        elif self.situacion == 'CT':
            c.positions[5] = '2'

        if self.potencia is not None:
            if self.potencia < 1:
                c.positions[6] = 'A'
            elif 1 <= self.potencia < 5:
                c.positions[6] = 'B'
            elif 5 <= self.potencia < 10:
                c.positions[6] = 'C'
            elif 10 <= self.potencia < 15:
                c.positions[6] = 'D'
            elif 15 <= self.potencia < 20:
                c.positions[6] = 'E'

        if self.estado == 'S':
            c.positions[7] = '0'
        elif self.estado == 'R':
            c.positions[7] = '1'
        elif self.estado == 'M':
            c.positions[7] = '2'

        return c


class CentroTransformador(Base):
    """
    Objeto que representa un Centro transformador
    """

    def __init__(self):
        self.tension_p = None
        """Tensión primaria en kV
        """
        self.tension_s = None
        """Tensión secundaria en kV
        """
        self.reparto = True
        """Indica si el CT es de reparto o reflexión
        """
        self.tension = None
        """Tension en kV
        """
        self.tipo = None
        """Tipo de centro transformador

            - Intemperie = ``I``
            - Caseta = ``C``
            - Local = ``L``
            - Subterráneo = ``S``
            - Móvil = ``M``
        """
        self.transformadores = []
        """Lista de transformadores del CT
        """

    @property
    def potencia_instalada(self):
        """Potencia instalada en el centro

        Suma la potencia de todos los transformadores que no esten
        en estado Reserva (R)
        """
        potencia = 0
        for t in self.transformadores:
            assert isinstance(t, Transformador)
            if t.estado != 'R':
                potencia += t.potencia
        return potencia

    @property
    def cini(self):
        """Obtiene el CINI del centro transformador
        :returns :py:class:`CINI`
        """
        c = CINI()
        c.positions[1] = '2'
        c.positions[2] = '2'

        if self.tension_p is not None and 1 <= self.tension_p < 36:
            c.positions[3] = '4'
        if self.tension_s is not None and self.tension_s < 1:
            c.positions[4] = '5'

        if self.tipo == 'I':
            c.positions[5] = '1'
        elif self.tipo == 'C':
            c.positions[5] = '2'
        elif self.tipo == 'L':
            c.positions[5] = '3'
        elif self.tipo == 'S':
            c.positions[5] = '4'
        elif self.tipo == 'M':
            c.positions[5] = '9'

        if self.tension is not None:
            if self.tension <= 1:
                c.positions[6] = 'C'
            elif self.tension == 3:
                c.positions[6] = 'D'
            elif self.tension == 5:
                c.positions[6] = 'E'
            elif self.tension == 5.5:
                c.positions[6] = 'F'
            elif self.tension == 6:
                c.positions[6] = 'G'
            elif self.tension == 6.6:
                c.positions[6] = 'H'
            elif self.tension == 10:
                c.positions[6] = 'I'
            elif self.tension == 11:
                c.positions[6] = 'J'
            elif self.tension == 12:
                c.positions[6] = 'K'
            elif self.tension == 13.2:
                c.positions[6] = 'L'
            elif self.tension == 15:
                c.positions[6] = 'M'
            elif self.tension == 16:
                c.positions[6] = 'N'
            elif self.tension == 20:
                c.positions[6] = 'O'
            elif self.tension == 22:
                c.positions[6] = 'P'
            elif self.tension == 24:
                c.positions[6] = 'Q'
            elif self.tension == 25:
                c.positions[6] = 'R'
            elif self.tension == 30:
                c.positions[6] = 'S'
            elif self.tension == 33:
                c.positions[6] = 'T'

        if self.transformadores:
            if len(self.transformadores) == 1:
                if self.potencia_instalada == 0:
                    c.positions[7] = 'A'
                elif 0 < self.potencia_instalada <= 15:
                    c.positions[7] = 'B'
                elif 15 < self.potencia_instalada <= 25:
                    c.positions[7] = 'C'
                elif 25 < self.potencia_instalada <= 50:
                    c.positions[7] = 'D'
                elif 50 < self.potencia_instalada <= 100:
                    c.positions[7] = 'E'
                elif 100 < self.potencia_instalada <= 160:
                    c.positions[7] = 'F'
                elif 160 < self.potencia_instalada <= 250:
                    c.positions[7] = 'G'
                elif 250 < self.potencia_instalada <= 400:
                    c.positions[7] = 'H'
                elif 400 < self.potencia_instalada <= 630:
                    c.positions[7] = 'I'
                elif 630 < self.potencia_instalada <= 1000:
                    c.positions[7] = 'J'
                elif 1000 < self.potencia_instalada <= 1250:
                    c.positions[7] = 'K'
            elif len(self.transformadores) == 2:
                if self.potencia_instalada <= 2 * 15:
                    c.positions[7] = 'L'
                elif 2 * 15 < self.potencia_instalada <= 2 * 25:
                    c.positions[7] = 'M'
                elif 2 * 25 < self.potencia_instalada <= 2 * 50:
                    c.positions[7] = 'N'
                elif 2 * 50 < self.potencia_instalada <= 2 * 100:
                    c.positions[7] = 'O'
                elif 2 * 100 < self.potencia_instalada <= 2 * 160:
                    c.positions[7] = 'P'
                elif 2 * 160 < self.potencia_instalada <= 2 * 250:
                    c.positions[7] = 'Q'
                elif 2 * 250 < self.potencia_instalada <= 2 * 400:
                    c.positions[7] = 'R'
                elif 2 * 400 < self.potencia_instalada <= 2 * 630:
                    c.positions[7] = 'S'
                elif 2 * 630 < self.potencia_instalada <= 2 * 1000:
                    c.positions[7] = 'T'
                elif 2 * 1000 < self.potencia_instalada <= 2 * 1250:
                    c.positions[7] = 'U'
        else:
            if self.reparto:
                c.positions[7] = 'V'
            else:
                c.positions[7] = 'Z'

        return c


class Subestacion(CentroTransformador):
    """
    Subestación
    """

    tipos_validos = {
        'C': '1',
        'B': '2',
        'M': '3'
    }

    def __init__(self):
        super(Subestacion, self).__init__()
        self.tipo = None
        """Tipo de subestación

            - Convencional = ``C``
            - Blindada = ``B``
            - Móvil = ``M``
        """

    @property
    def cini(self):
        """
        Obtiene el CINI del centro transformador
        :returns :py:class:`CINI`
        """
        c = CINI()
        c.positions[1] = '2'
        c.positions[2] = '1'

        if self.tension_p >= 400:
            c.positions[3] = '0'
        elif 220 <= self.tension_p < 400:
            c.positions[3] = '1'
        elif 110 <= self.tension_p < 220:
            c.positions[3] = '2'
        elif 36 <= self.tension_p < 110:
            c.positions[3] = '3'
        elif 1 <= self.tension_p < 36:
            c.positions[3] = '4'

        if 110 <= self.tension_s < 220:
            c.positions[4] = '2'
        elif 36 <= self.tension_s < 110:
            c.positions[4] = '3'
        elif 1 <= self.tension_s < 36:
            c.positions[4] = '4'

        if self.tipo in self.tipos_validos:
            c.positions[5] = self.tipos_validos[self.tipo]

        if not self.reparto:
            if self.potencia_instalada < 5:
                c.positions[6] = 'A'
            elif 5 <= self.potencia_instalada < 10:
                c.positions[6] = 'B'
            elif 10 <= self.potencia_instalada < 15:
                c.positions[6] = 'C'
            elif 15 <= self.potencia_instalada < 20:
                c.positions[6] = 'D'
            elif 20 <= self.potencia_instalada < 25:
                c.positions[6] = 'E'
            elif 25 <= self.potencia_instalada < 30:
                c.positions[6] = 'F'
            elif 30 <= self.potencia_instalada < 40:
                c.positions[6] = 'G'
            elif 40 <= self.potencia_instalada < 60:
                c.positions[6] = 'H'
            elif 60 <= self.potencia_instalada < 80:
                c.positions[6] = 'I'
            elif 80 <= self.potencia_instalada < 100:
                c.positions[6] = 'J'
            elif 100 <= self.potencia_instalada < 120:
                c.positions[6] = 'K'
            elif 120 <= self.potencia_instalada < 150:
                c.positions[6] = 'L'
            elif 150 <= self.potencia_instalada < 200:
                c.positions[6] = 'N'
            elif 200 <= self.potencia_instalada < 250:
                c.positions[6] = 'O'
            elif 250 <= self.potencia_instalada < 300:
                c.positions[6] = 'P'
            elif 300 <= self.potencia_instalada < 350:
                c.positions[6] = 'Q'
            elif 350 <= self.potencia_instalada < 400:
                c.positions[6] = 'R'
            elif self.potencia_instalada >= 400:
                c.positions[6] = 'S'
        else:
            c.positions[6] = 'Z'

        # Séptima posición no utilizada
        c.positions[7] = '0'

        return c
