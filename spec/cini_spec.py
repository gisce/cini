# coding=utf-8
from cini.models import CINI

from expects import *


with context('Un objeto CINI'):
    with it('el prefijo debe ser igual a I'):
        c = CINI()
        expect(c.positions[0]).to(equal('I'))

    with it('debe tener soporte indexado'):
        c = CINI()
        expect(c[0]).to(equal('I'))
