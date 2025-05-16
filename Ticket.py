import random

def generate():
    print(random.randint(1000, 9999))

class ticket:

    def __init__(self, price):
        self.price = price
        self.number = generate()