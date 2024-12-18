import json
from itertools import product
from operator import index

# Файл для хранения данных
DATA_FILE = "store_data.json"

# Функция для загрузки данных из файла
def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"products": [], "cart": []}


# Функция для сохранения данных в файл
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Функция для отображения каталога продуктов
def show_products(products):
    print("\nКаталог продуктов:")
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product['name']} - {product['price']} руб. ({product['quantity']} шт. в наличии)")

# Функция для добавления продукта в корзину
def add_to_cart(data, product_index, quantity):
    product = data["products"][product_index]
    if product["quantity"] >= quantity:
        product["quantity"] -= quantity
        data["cart"].append({"name": product["name"], "price": product["price"], "quantity": quantity})
        print(f"Добавлено в корзину: {product['name']} - {quantity} шт.")
    else:
        print("Недостаточно товара на складе.")

# Функция для отображения корзины
def show_cart(cart):
    print("\nВаша корзина:")
    if not cart:
        print("Корзина пуста.")
    else:
        total = 0
        for item in cart:
            cost = item["price"] * item["quantity"]
            total += cost
            print(f"{item['name']} - {item['quantity']} шт. x {item['price']} руб. = {cost} руб.")
        print(f"Итого: {total} руб.")

# Основной цикл работы магазина
def main():
    data = load_data()

    while True:
        print("\n1. Показать каталог продуктов")
        print("2. Добавить продукт в корзину")
        print("3. Показать корзину")
        print("4. Купить")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_products(data["products"])
        elif choice == "2":
            show_products(data["products"])
            try:
                product_index = int(input("Введите номер продукта: ")) - 1
                quantity = int(input("Введите количество: "))
                if 0 <= product_index < len(data["products"]):
                    add_to_cart(data, product_index, quantity)
                    save_data(data)
                else:
                    print("Неверный номер продукта.")
            except ValueError:
                print("Ошибка ввода. Попробуйте снова.")
        elif choice == "3":
            show_cart(data["cart"])
        elif choice == "4":
            show_cart(data["cart"])
            if not data["cart"]:
                print("Ваша корзина пуста. Добавьте товары перед покупкой.")
        else:
                buy = input("Вы хотите купить эти товары? (Да/Нет): ")
                if buy.lower() == "да":
                    print("Спасибо за покупку! Товары будут доставлены.")
                    # Очистка корзины после покупки
                    data["cart"] = []
                    save_data(data)
                else:
                    print("Вы можете продолжить покупки.")


if __name__ == "__main__":
    main()
