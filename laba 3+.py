milky = {"Cow milk": 35, "Cheese": 77, "Yogurt": 40}
bread = {"Buns": 25, "Bread": 32.5, "Baguette": 35.5}
meat = {"Beef": 125.35, "Chicken": 75, "Turkey": 105.45}
quantity = {
    'Cow milk': 2, 'Cheese': 3, 'Yogurt': 5,
    'Buns': 10, 'Bread': 15, 'Baguette': 12,
    'Beef': 4, 'Chicken': 10, 'Turkey': 3
}

products = {}
products.update(milky)
products.update(bread)
products.update(meat)

bag = []
bag_price = 0
wallet = 200


def greet_user():
    username = input("Введіть ваш логін аккаунта: ")
    print(f"{username}, ласкаво просимо у наш магазин! ")


def admin_login():
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")
    if login == "admin" and password == "1234":
        print("Ласкаво просимо!")
        print(quantity)
    else:
        print("невірний логін або пароль")


def buy_product_from_section(section):
    global bag_price
    print(section)
    print("Виберіть продукт в кошик: ")
    try:
        user_choice_product = int(input("> "))
    except ValueError:
        print("Введено невірну цифру/символ")
        return

    items = list(section.items())
    if 1 <= user_choice_product <= len(items):
        item_name, item_price = items[user_choice_product - 1]
        if quantity.get(item_name, 0) > 0:
            bag.append(item_name)
            bag_price += item_price
            quantity[item_name] = quantity.get(item_name, 0) - 1
            print("Додано товар", item_name, "в кошик")
        else:
            print("Не вистачає товару")
    else:
        print("Введено невірний номер товару")


def buy_product():
    print("Виберіть секцію:\n 1 - milky\n 2 - bread\n 3 - meat")
    try:
        user_choice = int(input("> "))
    except ValueError:
        print("Введено невірну цифру/символ")
        return

    sections = {1: milky, 2: bread, 3: meat}
    if user_choice in sections:
        buy_product_from_section(sections[user_choice])
    else:
        print("Невірна секція")


def view_products():
    print(products)


def view_cart():
    print(bag)
    print(bag_price)


def remove_product():
    global bag_price
    print("Впишіть в термінал продукт який ви хочете видалити з кошика", bag)
    while True:
        product_name = input("> ")
        if product_name == "exit":
            break
        elif product_name in bag:
            bag.remove(product_name)
            bag_price -= products.get(product_name, 0)
            quantity[product_name] = quantity.get(product_name, 0) + 1
            print("Видалено товар", product_name)
            break
        else:
            print("Введено невірний товар")


def checkout():
    global wallet
    print("...")
    wallet -= bag_price
    if wallet >= 0:
        print("Покупка завершена! Гарного дня")
        return True
    else:
        print("Недостатньо коштів")
        wallet += bag_price
        return False


def main():
    greet_user()

    menu = (
        "Будь ласка, виберіть опцію:\n"
        " 1 - Увійти\n"
        " 2 - Переглянути продукти\n"
        " 3 - Онлайн покупка\n"
        " 4 - Переглянути кошик\n"
        " 5 - Видалити товар\n"
        " 6 - Закінчити операцію\n"
        "Введіть опцію: "
    )

    while True:
        try:
            user_input = int(input(menu))
        except ValueError:
            print("Введено невірну цифру/символ")
            continue

        if user_input == 1:
            admin_login()
        elif user_input == 2:
            view_products()
        elif user_input == 3:
            buy_product()
        elif user_input == 4:
            view_cart()
        elif user_input == 5:
            remove_product()
        elif user_input == 6:
            if checkout():
                break
        else:
            print("Введено невірну цифру/символ")


if __name__ == "__main__":
    main()