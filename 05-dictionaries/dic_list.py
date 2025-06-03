pizza = {
'crust': 'thin',
'toppings': ['mushrooms', 'extra cheese', 'pineapple'],
}

print(f"So you want a {pizza['crust']} pizza")
for topping in pizza["toppings"]:
    print(f"with {topping}")