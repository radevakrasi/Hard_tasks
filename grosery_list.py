def shop_from_grocery_list(budget, grocery_list, *args):
    purchased_products = set()
    total = 0

    for item in args:
        name, price = item
        if name not in grocery_list:
            continue
        if name in purchased_products:
            continue
        if price > budget - total:
            break
        purchased_products.add(name)
        total += price

    if len(purchased_products) == len(grocery_list):
        budget_left = '{:.2f}'.format(budget - total)
        return f"Shopping is successful. Remaining budget: {budget_left}."
    else:
        searched_item = set(grocery_list) - purchased_products
        return "You did not buy all the products. Missing products: " + ', '.join(searched_item) + "."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),

    ("tomato", 10.0),
    ("tomato", 20.45),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))