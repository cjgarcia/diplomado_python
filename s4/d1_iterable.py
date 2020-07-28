def pizzas():
    yield "Pizza 1"
    yield "Pizza 2"
    yield "Pizza 3"
    yield "Pizza 4"
    yield "Pizza 5"

mis_pizzas = pizzas()

for pizza in mis_pizzas:
    print(pizza)

