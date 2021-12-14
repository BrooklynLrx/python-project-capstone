from abc import ABC

class Inventory(ABC):

    def __init__(self,name,quantity):
        self._name = name
        self._quantity = quantity

    def refill(self,incre):
        pass

    @property
    def quantity(self):
        return self._quantity

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f'Inventory <{self.name} has {self.quantity} >'


class main_food(Inventory):

    def __init__(self, name):
        super().__init__(name,500)

    def __str__(self):
        return 'main_food' + super().__str__()


class ingredient(Inventory):

    def __init__(self, name):
        super().__init__(name,1000)

    def __str__(self):
        return 'ingredient' + super().__str__()

class sides(Inventory):

    def __init__(self, name):
        super().__init__(name, 1000)

    def __str__(self):
        return 'sides' + super().__str__()

class Drinks(Inventory):

    def __init__(self, name):
        super().__init__(name, 2000)

    def __str__(self):
        return 'drinks' + super().__str__()