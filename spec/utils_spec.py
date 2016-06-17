from expects import *
from cini import nearest


with description('Searching the nearest element'):
    with context('if only one element is passed'):
        with it('must return this element'):
            x = nearest(1, 10)
            expect(x).to(equal(10))
    with context('if more elements are passed'):
        with it('must return the nearest value'):
            x = nearest(14, 1, 2, 3, 20, 40)
            expect(x).to(equal(20))
        with context('if the element is just in the middle between to values'):
            with it('must return the greatest'):
                x = nearest(35, 0, 30, 40)
                expect(x).to(equal(40))