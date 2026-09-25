import random

def encrypt(message):
    PIZZA_TOPPINGS = ["ham", "tomatos", "spinach", "pineapple", "mushrooms"]
    encrypted = ""
    global char

    for char in message:
        encrypted += random.choice(PIZZA_TOPPINGS)

    return encrypted

print(encrypt("zef"))