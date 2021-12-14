class Main(object):

    def __init__(self,seasame,qty,muffin,qty1,chicken,qty2,beef,qty3,vegeterian,qty4,tomato,qty5,lettuce,qty6,cheese,qty7):
        self._seasame = seasame
        self._qty = qty
        self._muffin = muffin
        self._qty1 = qty1
        self._chicken = chicken
        self._qty2 = qty2
        self._beef = beef
        self._qty3 = qty3
        self._vegeterian = vegeterian
        self._qty4 = qty4
        self._tomato= tomato
        self._qty5 = qty5
        self._lettuce = lettuce
        self._qty6 = qty6
        self._cheese = cheese
        self._qty7 = qty7
    
    def main_fee(self):
        fee = self._qty * 1 + self._qty1 * 2 + self._qty2 * 2 + self._qty3 * 2 + self._qty4 * 1 + self._qty5 * 1 + self._qty6 * 1 + self._qty7 * 2 + 4
        return fee

    @property
    def qty(self):
        return self._qty

    @property
    def qty1(self):
        return self._qty1

    @property
    def qty2(self):
        return self._qty2

    @property
    def qty3(self):
        return self._qty3

    @property
    def qty4(self):
        return self._qty4

    @property
    def qty5(self):
        return self._qty5

    @property
    def qty6(self):
        return self._qty6

    @property
    def qty7(self):
        return self._qty7


    def __str__(self):
        return f'123'