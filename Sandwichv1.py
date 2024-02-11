"""allow people to choose ingredents to  make
 a sandwich"""


# Function to see what user picked
def make_sandwich():
    bread = {
        "white": 0.80,
        "wholegrain": 1.00
    }

    meat = {
        "chicken": 2.69,
        "Beef": 3.00
    }

    others = {
        "Onion": 1.69,
        "tomato": 1.00
    }

    sandwich = []

    price = 0
    choices = [["bread", bread], ["meat", meat], ["others", others]]

    for choice in choices:
        name = choice[0]
