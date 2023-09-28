class Bikes:
    sold = False

    def __init__(self, description, cost, sale_price, condition):
        self.description = description
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition

    def update_sale_price(self, sale_price):
        if self.sold:
            print('Action not allowed, bike has already been sold')
        else:
            self.sale_price = sale_price

    def sell(self):
        self.sold = True


bike1 = Bikes('Univega Alpina, orange', 100, 500, 0.5)
bike1.update_sale_price(350)
bike1.sell()
