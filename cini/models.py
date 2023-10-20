# coding=utf-8
"""
Modelos de datos básicos para calcular los CINIS.
"""
TG_TECHNOLOGIES = ['prime', 'plc800', 'smmweb']

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
        self._tension = None
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
    def tension(self):
        return self._tension

    @tension.setter
    def tension(self, value):
        if 3000 >= value >= 4000:
            value = int(round(value / 1000.0) * 1000)
        self._tension = value

    @property
    def cini(self):
        """Obtiene el CINI de la linea
        :returns :py:class:`CINI`
        """
        c = CINI()
        c.positions[1] = '2'
        c.positions[2] = '0'
        if self.tension is not None:
            if 110000 <= self.tension < 220000:
                c.positions[3] = '2'
            elif 36000 <= self.tension < 110000:
                c.positions[3] = '3'
            elif 1000 <= self.tension < 36000:
                c.positions[3] = '4'
            elif self.tension < 1000:
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
            if self.seccion is not None:
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

            if self.tension <= 230:
                c.positions[7] = 'A'
            elif 0.230 < self.tension <= 400:
                c.positions[7] = 'B'
            elif 0.4 < self.tension <= 1000:
                c.positions[7] = 'C'
            elif 1000 < self.tension <= 3000:
                c.positions[7] = 'D'
            elif 3000 < self.tension <= 5000:
                c.positions[7] = 'E'
            elif 5000 <= self.tension <= 5500:
                c.positions[7] = 'F'
            elif 5500 < self.tension <= 6000:
                c.positions[7] = 'G'
            elif 6000 < self.tension <= 6600:
                c.positions[7] = 'H'
            elif 6600 < self.tension <= 10000:
                c.positions[7] = 'I'
            elif 10000 < self.tension <= 11000:
                c.positions[7] = 'J'
            elif 11000 < self.tension <= 12000:
                c.positions[7] = 'K'
            elif 12000 < self.tension <= 13200:
                c.positions[7] = 'L'
            elif 13200 < self.tension <= 15000:
                c.positions[7] = 'M'
            elif 15000 < self.tension <= 16000:
                c.positions[7] = 'N'
            elif 16000 < self.tension <= 20000:
                c.positions[7] = 'O'
            elif 20000 < self.tension <= 22000:
                c.positions[7] = 'P'
            elif 22000 < self.tension <= 24000:
                c.positions[7] = 'Q'
            elif 24000 < self.tension <= 25000:
                c.positions[7] = 'R'
            elif 25000 < self.tension <= 30000:
                c.positions[7] = 'S'
            elif 30000 < self.tension <= 33000:
                c.positions[7] = 'T'
            elif 33000 < self.tension <= 45000:
                c.positions[7] = 'U'
            elif 45000 < self.tension <= 50000:
                c.positions[7] = 'V'
            elif 50000 < self.tension <= 55000:
                c.positions[7] = 'W'
            elif 55000 < self.tension <= 66000:
                c.positions[7] = 'X'
            elif 66000 < self.tension <= 110000:
                c.positions[7] = 'Y'
            elif 110000 < self.tension <= 130000:
                c.positions[7] = 'Z'
            elif 130000 < self.tension <= 132000:
                c.positions[7] = '1'
            elif 133000 < self.tension <= 150000:
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

        if self.tension_s is not None:
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
            elif 20 <= self.potencia < 25:
                c.positions[6] = 'F'
            elif 25 <= self.potencia < 30:
                c.positions[6] = 'G'
            elif 30 <= self.potencia < 40:
                c.positions[6] = 'H'
            elif 40 <= self.potencia < 60:
                c.positions[6] = 'I'
            elif 60 <= self.potencia < 80:
                c.positions[6] = 'J'
            elif 80 <= self.potencia < 100:
                c.positions[6] = 'K'
            elif 100 <= self.potencia < 120:
                c.positions[6] = 'L'
            elif 120 <= self.potencia < 150:
                c.positions[6] = 'M'
            elif 150 <= self.potencia:
                c.positions[6] = 'N'

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
        from cini import nearest
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
            elif 1 < self.tension <= 3:
                c.positions[6] = 'D'
            elif 3 < self.tension <= 5:
                c.positions[6] = 'E'
            elif 5 < self.tension <= 5.5:
                c.positions[6] = 'F'
            elif 5.5 < self.tension <= 6:
                c.positions[6] = 'G'
            elif 6 < self.tension <= 6.6:
                c.positions[6] = 'H'
            elif 6.6 < self.tension <= 10:
                c.positions[6] = 'I'
            elif 10 < self.tension <= 11:
                c.positions[6] = 'J'
            elif 11 < self.tension <= 12:
                c.positions[6] = 'K'
            elif 12 < self.tension <= 13.2:
                c.positions[6] = 'L'
            elif 13.2 < self.tension <= 15:
                c.positions[6] = 'M'
            elif 15 < self.tension <= 16:
                c.positions[6] = 'N'
            elif 16 < self.tension <= 20:
                c.positions[6] = 'O'
            elif 20 < self.tension <= 22:
                c.positions[6] = 'P'
            elif 22 < self.tension <= 24:
                c.positions[6] = 'Q'
            elif 24 < self.tension <= 25:
                c.positions[6] = 'R'
            elif 25 < self.tension <= 30:
                c.positions[6] = 'S'
            elif 30 < self.tension <= 33:
                c.positions[6] = 'T'

        if self.transformadores:
            if len(self.transformadores) == 1:
                pos_7 = {
                    0: 'A',
                    15: 'B',
                    25: 'C',
                    50: 'D',
                    100: 'E',
                    160: 'F',
                    250: 'G',
                    400: 'H',
                    630: 'I',
                    1000: 'J',
                    1250: 'K'
                }
                idx = nearest(self.potencia_instalada, *pos_7.keys())
                c.positions[7] = pos_7[idx]
            elif len(self.transformadores) == 2:
                pos_7 = {
                    30: 'L',
                    50: 'M',
                    100: 'N',
                    200: 'O',
                    320: 'P',
                    500: 'Q',
                    800: 'R',
                    1260: 'S',
                    2000: 'T',
                    2500: 'U'
                }
                idx = nearest(self.potencia_instalada, *pos_7.keys())
                c.positions[7] = pos_7[idx]
        else:
            if self.reparto:
                c.positions[7] = 'Z'
            else:
                c.positions[7] = 'V'

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

        if self.tension_s is not None:
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


class Posicion(Base):
    """Posición de una subestación
    """

    actuaciones_validas = {
        'L': '1',
        'T': '2',
        'A': '3',
        'M': '4',
        'R': '5'
    }

    def __init__(self):
        super(Posicion, self).__init__()
        self.tension = None
        self.interruptor = None
        self.situacion = None
        """
        Ubicación de la posición:
          - Interior: ``I``
          - Intemperie: ``E``
          - Móvil: ``M``
        """
        self.tipo = None
        """
        Tipo de posición:
          - Blindada ``B``
          - Convencional ``C``
          - Hibrida ``H``
        """
        self.actuacion = None
        """
        Actuación de la posición:
          - Linea ``L``
          - Transformación ``T``
          - Acoplamiento ``A``
          - Medida ``M``
          - Reserva ``R``
        """

    @property
    def cini(self):
        """
        Obtiene el CINI del centro transformador
        :returns :py:class:`CINI`
        """

        c = CINI()
        c.positions[1] = '2'
        c.positions[2] = '8'

        if self.tension is not None:
            if self.tension >= 110:
                c.positions[3] = 'A'
            elif 110 > self.tension >= 36:
                c.positions[3] = 'B'
            elif 36 > self.tension >= 1:
                c.positions[3] = 'C'

        if self.interruptor is not None:
            if self.interruptor:
                c.positions[4] = '2'
            else:
                c.positions[4] = '3'

        if self.tipo and self.situacion:
            if self.situacion == 'I':
                if self.tipo == 'B':
                    c.positions[5] = 'A'
                elif self.tipo == 'C':
                    c.positions[5] = 'C'
                elif self.tipo == 'H':
                    c.positions[5] = 'E'
            elif self.situacion == 'E':
                if self.tipo == 'B':
                    c.positions[5] = 'B'
                elif self.tipo == 'C':
                    c.positions[5] = 'D'
                elif self.tipo == 'H':
                    c.positions[5] = 'F'
            elif self.situacion == 'M' and self.tipo == 'B':
                c.positions[5] = 'G'

        if self.actuacion and self.actuacion in self.actuaciones_validas:
            c.positions[6] = self.actuaciones_validas[self.actuacion]

        if self.tension is not None:
            tension_v = int(round(self.tension, 1) * 1000)
            if 0 < tension_v <= 1000:
                c.positions[7] = 'C'
            elif 1000 < tension_v <= 3000:
                c.positions[7] = 'D'
            elif 3000 < tension_v <= 5000:
                c.positions[7] = 'E'
            elif 5000 < tension_v <= 5500:
                c.positions[7] = 'F'
            elif 5500 < tension_v <= 6000:
                c.positions[7] = 'G'
            elif 6000 < tension_v <= 6600:
                c.positions[7] = 'H'
            elif 6600 < tension_v <= 10000:
                c.positions[7] = 'I'
            elif 10000 < tension_v <= 11000:
                c.positions[7] = 'J'
            elif 11000 < tension_v <= 12000:
                c.positions[7] = 'K'
            elif 12000 < tension_v <= 13200:
                c.positions[7] = 'L'
            elif 13200 < tension_v <= 15000:
                c.positions[7] = 'M'
            elif 15000 < tension_v <= 16000:
                c.positions[7] = 'N'
            elif 16000 < tension_v <= 20000:
                c.positions[7] = 'O'
            elif 20000 < tension_v <= 22000:
                c.positions[7] = 'P'
            elif 22000 < tension_v <= 24000:
                c.positions[7] = 'Q'
            elif 24000 < tension_v <= 25000:
                c.positions[7] = 'R'
            elif 25000 < tension_v <= 30000:
                c.positions[7] = 'S'
            elif 30000 < tension_v <= 33000:
                c.positions[7] = 'T'
            elif 33000 < tension_v <= 45000:
                c.positions[7] = 'U'
            elif 45000 < tension_v <= 50000:
                c.positions[7] = 'V'
            elif 50000 < tension_v <= 55000:
                c.positions[7] = 'W'
            elif 55000 < tension_v <= 66000:
                c.positions[7] = 'X'
            elif 66000 < tension_v <= 110000:
                c.positions[7] = 'Y'
            elif 110000 < tension_v <= 130000:
                c.positions[7] = 'Z'
            elif 130000 < tension_v <= 132000:
                c.positions[7] = '1'
            elif 132000 < tension_v <= 150000:
                c.positions[7] = '2'
            else:
                c.positions[7] = '5'

        return c


class Parque(Posicion):
    """
    Parque
    """
    def __init__(self):
        super(Parque, self).__init__()
        self.barras = None
    
    @property
    def cini(self):
        """
        Obtiene el CINI del centro transformador
        :returns :py:class:`CINI`
        """
        c = super(Parque, self).cini

        if self.tension is not None:
            if 110 <= self.tension < 220:
                c.positions[3] = '2'
            elif 36 <= self.tension < 110:
                c.positions[3] = '3'
            elif 1 <= self.tension < 36:
                c.positions[3] = '4'

        c.positions[4] = '1'

        if self.tipo is not None:
            if self.tipo == 'C':
                c.positions[5] = '1'
            elif self.tipo == 'B':
                c.positions[5] = '2'
            elif self.tipo == 'H':
                c.positions[5] = '3'

        if self.barras is not None:
            c.positions[6] = self.barras

        return c


class Fiabilidad(Base):
    """
    Elemento de fiabilidad
    """

    TIPOS = {
        'S': '1',
        'R': '2',
        'T': '3',
        'F': '4',
        'SA': '5',
        'I': '6',
        'IS': '7'
    }

    TIPO_POSICIONES = {
        'L': '1',
        'P': '2'
    }

    SITUACIONES = {
        'SE': '1',
        'CT': '2',
        'LAT': '3'
    }

    TENSIONES = {
        'LAT': ['2', '3', '4'],
        'CT': ['A', 'B', 'C'],
        'SE': ['A', 'B', 'C'],
    }

    def __init__(self):
        self.tension = None
        self.tipo = None
        self.tipo_posicion = None
        self.telemando = None
        self.situacion = None
        self.aislante = None

    @property
    def cini(self):
        """
        Obtiene el CINI del centro transformador
        :returns :py:class:`CINI`
        """
        c = CINI()
        c.positions[1] = '2'
        if self.situacion in ('CT', 'SE'):
            c.positions[2] = '8'
        else:
            c.positions[2] = '6'
        if self.tension is not None:
            if 110 <= self.tension < 220:
                c.positions[3] = self.TENSIONES[self.situacion][0]
            elif 36 <= self.tension < 110:
                c.positions[3] = self.TENSIONES[self.situacion][1]
            elif 1 <= self.tension < 36:
                c.positions[3] = self.TENSIONES[self.situacion][2]
        if self.situacion in ('CT', 'SE'):
            c.positions[4] = '2'
        else:
            c.positions[4] = '0'
        if self.situacion == 'LAT' and self.tipo:
            c.positions[5] = self.TIPOS.get(self.tipo, ' ')
        elif self.situacion in ('CT', 'SE') and self.aislante:
            if self.aislante.upper() == 'AIRE':
                c.positions[5] = 'C'
            else:
                c.positions[5] = 'A'
        if self.situacion == 'LAT' and self.telemando is not None:
            if self.telemando:
                c.positions[6] = '2'
            else:
                c.positions[6] = '1'
        elif self.situacion in ('CT', 'SE') and self.tipo_posicion:
            c.positions[6] = self.TIPO_POSICIONES.get(self.tipo_posicion, ' ')
        if self.situacion:
            if self.situacion == 'LAT':
                c.positions[7] = self.SITUACIONES.get(self.situacion, ' ')
            elif self.situacion in ('CT', 'SE') and self.tension:
                tension_v = int(round(self.tension, 1) * 1000)
                if 0 < tension_v <= 1000:
                    c.positions[7] = 'C'
                elif 1000 < tension_v <= 3000:
                    c.positions[7] = 'D'
                elif 3000 < tension_v <= 5000:
                    c.positions[7] = 'E'
                elif 5000 < tension_v <= 5500:
                    c.positions[7] = 'F'
                elif 5500 < tension_v <= 6000:
                    c.positions[7] = 'G'
                elif 6000 < tension_v <= 6600:
                    c.positions[7] = 'H'
                elif 6600 < tension_v <= 10000:
                    c.positions[7] = 'I'
                elif 10000 < tension_v <= 11000:
                    c.positions[7] = 'J'
                elif 11000 < tension_v <= 12000:
                    c.positions[7] = 'K'
                elif 12000 < tension_v <= 13200:
                    c.positions[7] = 'L'
                elif 13200 < tension_v <= 15000:
                    c.positions[7] = 'M'
                elif 15000 < tension_v <= 16000:
                    c.positions[7] = 'N'
                elif 16000 < tension_v <= 20000:
                    c.positions[7] = 'O'
                elif 20000 < tension_v <= 22000:
                    c.positions[7] = 'P'
                elif 22000 < tension_v <= 24000:
                    c.positions[7] = 'Q'
                elif 24000 < tension_v <= 25000:
                    c.positions[7] = 'R'
                elif 25000 < tension_v <= 30000:
                    c.positions[7] = 'S'
                elif 30000 < tension_v <= 33000:
                    c.positions[7] = 'T'
                elif 33000 < tension_v <= 45000:
                    c.positions[7] = 'U'
                elif 45000 < tension_v <= 50000:
                    c.positions[7] = 'V'
                elif 50000 < tension_v <= 55000:
                    c.positions[7] = 'W'
                elif 55000 < tension_v <= 66000:
                    c.positions[7] = 'X'
                elif 66000 < tension_v <= 110000:
                    c.positions[7] = 'Y'
                elif 110000 < tension_v <= 130000:
                    c.positions[7] = 'Z'
                elif 130000 < tension_v <= 132000:
                    c.positions[7] = '1'
                elif 132000 < tension_v <= 150000:
                    c.positions[7] = '2'
                else:
                    c.positions[7] = '5'

        return c


class Contador(Base):
    """
    Objeto que representa una Contador.

    Podemos obtener el CINI de una Contador creando un objeto Contador,
    asignando los valores correspondientes y accediendo a la propiedada `cini`:
        c = Contador()
        c.fases = 1
        c.tecnologia = 'prime'
        c.telegestionado = True
        c.tipo_agree = '5'
        c.tipo_tarifa = 'BT'
        c.propiedad_cliente = True
        str(c.cini)
    """

    def __init__(self):
        self.fases = None               # INT
        self.tecnologia = None          # STR
        self.telegestionado = None      # BOOLEAN
        self.tipo_agree = None          # STR
        self.tipo_tarifa = None         # STR
        self.propiedad_cliente = None   # BOOLEAN

    @property
    def cini(self):
        """
        Obtiene el CINI del Contador
        :returns :py:class:`CINI`
        """
        cini = CINI()
        cini.positions[1] = '3'
        cini.positions[2] = '1'
        cini.positions[3] = '0'
        cini.positions[7] = '0'

        # Posicio 4
        if self.propiedad_cliente:
            cini.positions[4] = '2'
        else:
            cini.positions[4] = '1'

        # Posicio 5
        if self.tecnologia in TG_TECHNOLOGIES:
            cini.positions[5] = '3'
        elif self.tecnologia == 'telemeasure':
            cini.positions[5] = '2'
        elif self.tecnologia not in TG_TECHNOLOGIES and self.tecnologia != 'telemeasure':
            cini.positions[5] = '1'
        else:
            cini.positions[5] = '1'

        # Posicio 6
        if self.tipo_agree == '2':
            cini.positions[6] = 'L'
        elif self.tipo_agree == '3' and self.tipo_tarifa == 'BT':
            cini.positions[6] = 'M'
        elif self.tipo_agree == '3' and self.tipo_tarifa == 'AT':
            cini.positions[6] = 'N'
        elif self.tipo_agree == '4':
            cini.positions[6] = 'O'
        elif self.tipo_agree == '5' and self.fases == 1:
            cini.positions[6] = 'P'
        elif self.tipo_agree == '5' and self.fases == 3:
            cini.positions[6] = 'Q'
        else:
            cini.positions[6] = 'U'

        return cini

class Generador(Base):
    """
    Objeto que representa una instalación de generación conectada a distribución
    """

    def __init__(self):
        self.tension = None
        """Tensión de conexión en kV
        """
        self.tecnologia = None
        """Tecnologia de generación
        """
        self.potencia = None
        """Potencia en MVA
        """

    @property
    def cini(self):
        """
        Obtiene el CINI del generador
        :returns :py:class:`CINI`
        """
        c = CINI()
        c.positions[1] = '4'
        c.positions[2] = '3'
        c.positions[5] = '0'
        c.positions[7] = '0'
        tecnologias = {
                'a11': '2',
                'a12': '2',
                'a13': '2',
                'a20': '4',
                'b11': '5',
                'b12': '9',
                'b21': '7',
                'b22': '8',
                'b30': '9',
                'b41': '1',
                'b42': '1',
                'b51': '1',
                'b52': '1',
                'b60': '3',
                'b71': '9',
                'b72': '9',
                'b80': '3',
                'c10': '4',
                'c20': '4',
                'c30': '9'
        }

        if self.tension is not None:
            if 110000 <= self.tension < 220000:
                c.positions[3] = '2'
            elif 36000 <= self.tension < 110000:
                c.positions[3] = '3'
            elif 1000 <= self.tension < 36000:
                c.positions[3] = '4'
            elif self.tension < 1000:
                c.positions[3] = '5'

        if self.tecnologia is not None:
            if self.tecnologia in tecnologias:
                c.positions[4] = tecnologias[self.tecnologia]

        if self.potencia is not None:
            if self.potencia <= 1000:
                c.positions[6] = 'A'
            elif 1000 < self.potencia <= 2000:
                c.positions[6] = 'B'
            elif 2000 < self.potencia <= 5000:
                c.positions[6] = 'C'
            elif 5000 < self.potencia <= 10000:
                c.positions[6] = 'D'
            elif 10000 < self.potencia < 15000:
                c.positions[6] = 'E'
            elif 15000 <= self.potencia < 20000:
                c.positions[6] = 'F'
            elif 20000 <= self.potencia < 25000:
                c.positions[6] = 'G'
            elif 25000 <= self.potencia < 30000:
                c.positions[6] = 'H'
            elif 30000 <= self.potencia < 40000:
                c.positions[6] = 'I'
            elif self.potencia >= 40000:
                c.positions[6] = 'J'

        return c
