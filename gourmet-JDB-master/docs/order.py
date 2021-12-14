from inventory_stock import Inventory,main_food,sides,Drinks

class Order():

    def __init__(self, customer, main, sides, drinks):
        self._customer  = customer
        self._main    = main
        self._sides   = sides
        self._drinks  = drinks

    def main_fee(self):
        base = 0
        if self._main.type == 'burger':
            base = 5
        elif self._main.type == 'wrap':
            base = 7

        bun = self._main.bun.split()

        assert int(bun[0]) < 5
        assert int(bun[0]) < main_food(bun).quantity

        if bun[1] == 'seasame':
            bun_fee = 3
        elif bun[1] == 'muffin':
            bun_fee = 5

        total_bun = bun_fee * int(bun[0])

        patties = self._main.patties.split()
        if patties[1] == 'chicken':
            patties_fee = 4
        elif patties[1] == 'beef':
            patties_fee = 6
        elif patties[1] == 'vegetarian':
            patties_fee = 3

        total_patties = patties_fee * int(patties[0])
        assert int(patties[0]) < main_food(patties).quantity
        if self._main.ingredients == None:
            sum = 0
        else:
            ingredient = self._main.ingredients.split(',')
            sum = 0
            for i in range(len(ingredient)):
                c = ingredient[i].split()
                if c[1] == 'tomato':
                    price  = 2
                elif c[1] == 'lettuce':
                    price = 3
                elif c[1] == 'cheese':
                    price = 4

                total_ingredients = int(ingredient[i][0]) * price
                assert int(ingredient[i][0]) < main_food(ingredient).quantity
                sum = sum + total_ingredients
        net_price = base + total_bun + total_patties + sum
        return net_price


    def sides_fee(self):
        if self._sides == None:
            return 0

        side = self._sides.split(',')
        sum = 0
        for i in range(len(side)):
            c = side[i].split()
            assert int(side[i][0]) < sides(side).quantity
            if c[2] == 'nuggets':
                price = 5
            elif c[2] == 'fries':
                if c[1] == 'small':
                    price = 2
                elif c[1] == 'medium':
                    price = 3
                elif c[1] == 'large':
                    price = 4
            total = int(side[i][0]) * price

            sum = sum + total
        return sum

    def drinks_fee(self):
        if self._drinks == None:
            return 0
        drinks = self._drinks.split(',')
        sum = 0
        for i in range(len(drinks)):
            c = drinks[i].split()
            assert int(drinks[i][0]) < Drinks(drinks).quantity

            if c[2] == 'juice':
                price = 5
            elif c[2] == 'coke':
                price = 4

            total = int(drinks[i][0]) * price
            if c[1] == 'small':
                total = total - 1 * int(drinks[i][0])
            elif c[1] == 'medium':
                total = total
            elif c[1] == 'large':
                total = total + 1 * int(drinks[i][0])
            sum = sum + total
        return sum

    def __str__(self):
        return '11'