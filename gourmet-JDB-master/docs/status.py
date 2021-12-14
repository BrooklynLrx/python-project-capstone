class Status():

    def __init__(self, customer, main, sides, drinks, order_id,order_state = 'not ready'):
        self._customer = customer
        self._main = main
        self._sides = sides
        self._drinks = drinks
        self._order_id = order_id
        self._order_state = order_state

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self,order_id):
        self._order_id = order_id

    @property
    def order_state(self):
        return self._order_state


    def order_state_change(self,order_state):
        self._order_state = order_state



