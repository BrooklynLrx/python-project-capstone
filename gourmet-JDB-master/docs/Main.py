

class Main():

    def __init__(self,type,bun,patties,ingredients=None):
        self._type = type
        self._bun = bun
        self._patties = patties
        self._ingredients = ingredients

    @property
    def type(self):
        return self._type

    @property
    def bun(self):
        return self._bun

    @property
    def patties(self):
        return self._patties

    @property
    def ingredients(self):
        return self._ingredients

    def __str__(self):
        return f'Main <{self.type}, {self.bun},{self.patties},{self.ingredients}>'

