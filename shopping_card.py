def shopping_cart(*args):
    shopping_list = {'Pizza': [], 'Soup': [], 'Dessert': []}
    result = ''
    for element in args:
        if element == "Stop":
            break

        else:
            if (element[0] == "Pizza" and len(shopping_list["Pizza"]) == 4) or \
                    (element[0] == "Soup" and len(shopping_list["Soup"]) == 3) or \
                    (element[0] == "Dessert" and len(shopping_list["Dessert"]) == 2):
                continue
        if element[1] not in shopping_list[element[0]]:
            shopping_list[element[0]].append(element[1])

    if not shopping_list:
        return "No products in the cart!"
    else:
        sorted_shopping_list= sorted(shopping_list.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))


        for k, value in sorted_shopping_list:
            sorted_products = sorted(value)
            result += k + ":" + "\n"
            for el in sorted_products:
                result += " - " + el + "\n"
        return result


print(shopping_cart(
            ('Pizza', 'ham'),
            ('Dessert', 'milk'),
            ('Pizza', 'ham'),
            'Stop',
        ))

