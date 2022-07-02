class Car:
    """Official car dealer"""
    def __init__(self, maker, model, colour, price):
        """Details and feature of car"""
        self.maker = maker
        self.model = model
        self.colour = colour
        self.price = price
        self.__secret_cog = "tshhhh"

    def get_price(self):
        """Discounted price"""
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        """Possible discount"""
        self._discount = amount

car1 = Car("BMW", "i8", "white", 50000)
car2 = Car("Mercedes", "c-class", "black", 28500)

print(car1.get_price())
car2.set_discount(0.25)
print(car2.get_price())
print(car2._Car__secret_cog)