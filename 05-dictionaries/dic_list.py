pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}

print(f"So you want a {pizza['crust']} pizza")
for topping in pizza["toppings"]:
    print(f"with {topping}")