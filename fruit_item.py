from fruit_original import fruit_original

class fruit_item(fruit_original):
    def __init__(self, fruit: str, price: float, quantity=0, riped_fruit=0):
        #call to super function to have access to all attributes/methods
        super().__init__(fruit, price, quantity)
        #run validation to the received arguments:
        assert riped_fruit >= 0, f"Riped fruit {riped_fruit} should greater than zero"

        # assign to self object,
        self.riped_fruit = riped_fruit