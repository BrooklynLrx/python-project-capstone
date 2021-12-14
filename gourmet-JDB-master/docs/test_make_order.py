from inventory_stock import Inventory,main_food,ingredient,sides,Drinks
from order import Order
from Main import Main
from customer import Customer
from system import OrderSystem
from status import Status
from staff import Staff

import pytest

@pytest.fixture
def sys():
    return OrderSystem()




def test_order_with_burger(sys):

    main = Main('burger','2 seasame buns', '2 chicken patties','5 tomato')
    c = Customer('Dennis','123')
    sys.add_customer(c)
    order = sys.make_order(c,main,'1 pack nuggets','2 small coke')
    print(order.drinks_fee())
    total = order.drinks_fee() + order.main_fee() + order.sides_fee()

    assert total == 40
    assert len(sys.orders) == 1
    assert order is not None

def test_order_with_wrap(sys):

    main = Main('wrap','2 seasame buns', '2 chicken patties','5 tomato')
    c = Customer('Dennis','123')
    sys.add_customer(c)
    order = sys.make_order(c,main,'1 pack nuggets','2 small coke')
    print(order.drinks_fee())
    total = order.drinks_fee() + order.main_fee() + order.sides_fee()

    assert total == 42
    assert len(sys.orders) == 1
    assert order is not None

def test_order_without_ingredients(sys):

    main = Main('wrap','2 seasame buns', '2 chicken patties',None)
    c = Customer('Dennis','123')
    sys.add_customer(c)
    order = sys.make_order(c,main,'1 pack nuggets','2 small coke')
    print(order.drinks_fee())
    total = order.drinks_fee() + order.main_fee() + order.sides_fee()

    assert total == 32
    assert len(sys.orders) == 1
    assert order is not None

def test_order_with_mutiple_sides(sys):

    main = Main('wrap','2 seasame buns', '2 chicken patties',None)
    c = Customer('Dennis','123')
    sys.add_customer(c)
    order = sys.make_order(c,main,'1 pack nuggets,2 small fries','2 small coke')
    print(order.drinks_fee())
    total = order.drinks_fee() + order.main_fee() + order.sides_fee()

    assert total == 36
    assert len(sys.orders) == 1
    assert order is not None

def test_order_without_sides_and_drinks(sys):

    main = Main('wrap','2 seasame buns', '2 beef patties',None)
    c = Customer('Dennis','123')
    sys.add_customer(c)
    order = sys.make_order(c,main,None,None)
    print(order.drinks_fee())
    total = order.drinks_fee() + order.main_fee() + order.sides_fee()

    assert total == 25
    assert len(sys.orders) == 1
    assert order is not None

def test_order_with_state_changed_by_staff(sys):

    main = Main('wrap','2 seasame buns', '2 beef patties',None)
    c = Customer('Dennis','123')

    status = Status(c,main,'1 pack nuggets','2 small coke',c.id,'not ready')
    staff = Staff(status,'ken')
    staff.change_status('ready')
    sys.add_customer(c)
    order = sys.make_order(c,main,None,None)
    print(order.drinks_fee())
    total = order.drinks_fee() + order.main_fee() + order.sides_fee()

    assert status.order_state == 'ready'
    assert total == 25
    assert len(sys.orders) == 1
    assert order is not None