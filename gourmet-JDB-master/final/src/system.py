class OrderSystem(object):

    def __init__(self):
        self._mains = []
        self._orders = []
        self._inventory = []

    def add_mains(self, mains):
        self._mains.append(mains)

    @property
    def mains(self):
        return self._mains

    @property
    def orders(self):
        return self._orders

    @property
    def inventory(self):
        return self._inventory