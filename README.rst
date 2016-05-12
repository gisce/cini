CINI
====

.. image:: https://travis-ci.org/gisce/cini.svg?branch=master
    :target: https://travis-ci.org/gisce/cini
.. image:: https://readthedocs.org/projects/cini/badge/?version=latest
    :target: http://cini.readthedocs.io/es/latest/?badge=latest
    :alt: Documentation Status

Libreria para calcular de forma automática el código de identificación normalizado
de instalaciones (CINI)

Instalaciones soportadas
-------------------------

- Lineas
- Transformadores
- CT’s
- Subestacions
- Posicions y parques de distribución
- Celdas y elementos de corte
- Aparatos de medidas

Para desarrollar
----------------

Para cualquier cambio en el comportamiento **debe haber** un test que implemente este
comportamiento **antes** de desarrollar el cambio (metodología `TDD <https://en.wikipedia.org/wiki/Test-driven_development>`_)

- Crear un virtualenv

.. code-block:: shell

    $ mkvirtualenv cini
    $ workon cini


- Clonar el repositorio

.. code-block:: shell

    $ git clone https://github.com/gisce/cini.git


- Instalar dependencias desarrollo

.. code-block:: shell

    $ cd cini
    $ pip install -r requirements-dev.txt
    $ pip install -e .
    
Ejecutar tests
--------------
Utilizamos el sistema de tests `Mamba <http://nestorsalceda.github.io/mamba/>`_

Con el virtualenv activado y situados en la raíz del repositorio ejecutamos:

.. code-block:: shell

    $ mamba --format=documentation

