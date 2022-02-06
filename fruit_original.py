import csv


class fruit_original:
    payrate = 0.8  # this is the class attribute
    all = []

    def __init__(self, fruit: str, price: float, quantity=0):
        # run validation to the received arguments:
        assert price >= 0, f"Price {price} should greater than zero"
        assert quantity >= 0, f"Quantity {quantity} should greater than zero"

        # assign to self object,
        self.__fruit = fruit  # they are the instance attributes
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        fruit_original.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.payrate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property  # Property Decorator = Read-Only Attribute
    def fruit(self):
        return self.__fruit

    @fruit.setter
    # allow the editable rights to the attribute
    def fruit(self, value):
        if len(value) > 5:
            raise Exception("The name is too long!")
        else:
            self.__fruit = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod  # a decorator is to quick the behaviour of function, indicate before the function line
    def instantiate_from_csv(cls):  # class object itself is passed as first argument
        with open('fruits.csv', 'r') as f:
            reader = csv.DictReader(f)
            fruits = list(reader)

        for i in fruits:
            fruit_original(
                fruit=i.get('fruit'),
                price=int(i.get('price')),
                quantity=int(i.get('quantity')),
            )

    @staticmethod  # this is a regular function, not passing the object to the first argument
    def is_integer(num):
        # we will count out the floats that are point zero.
        # for i.e. 5.0, 10.0
        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__} are ('{self.fruit}', {self.__price}, {self.quantity})"

    def __connect_smpt(self, smpt_server):
        pass

    def __email_body(self):
        return f"""
        Hello, we have {self.__fruit} and total {self.quantity}.
        Regards, ChowChow
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect_smpt('')
        self.__send()
        self.__email_body()
