from inventory_stock import Inventory
from order import Order
from Main import Main
from customer import Customer

class OrderSystem():

    def __init__(self):
        self._customers = []
        self._orders = []
        self._inventory = []

    def get_customer(self, Id):

        for customer in self._customers:
            if customer.Id is Id:
                return customer
        return None

    def make_order(self,customer,main,sides,drinks):

        order = Order(customer,main,sides,drinks)
        self.add_customer(customer)
        self._orders.append(order)
        return order

    def inventory1(self,item,quantity):

        inventory_item = Inventory(item,quantity)
        self._inventory.append(inventory_item)
        return inventory_item

    def add_customer(self,customer):
        self._customers.append(customer)



    '''
    Properties
    '''

    @property
    def customers(self):
        return self._customers

    @property
    def orders(self):
        return self._orders

    @property
    def inventory(self):
        return self._inventory