class Human:
    default_name = 'Ivan'
    default_age = 19

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Name: {self.name}"
              f"\nAge: {self.age}\nMoney: {self.__money}"
              f"\nHouse: {self.__house}")

    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}"
              f"\nDefault age: {Human.default_age}")

    def __make_deal(self, house, price):
        if self.__money >= price:
            self.__money -= price
            self.__house = house
            print(f"Поздравляю, {self.name}! Вы купили дом!")
        else:
            print(f"Извините, {self.name}. У вас "
                  f"недостаточно денег, чтобы купить этот дом.")

    def earn_money(self):
        self.__money += 100000

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        self.__make_deal(house, final_price)


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount=0):
        return self._price * (1 - discount)


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)


Human.default_info()
person = Human(name="Alice", age=25)
person.info()
small_house = SmallHouse(price=10000)
person.buy_house(small_house, discount=0.1)
person.earn_money()
person.buy_house(small_house, discount=0.1)
person.info()
