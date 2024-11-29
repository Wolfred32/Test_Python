class Ingredient:
    """Класс для описания ингредиента с атрибутами: название, вес в сыром виде, вес в готовом виде, стоимость."""

    def __init__(self, name: str, raw_weight: int, weight: int, cost: int) -> None:
        if not name or raw_weight <= 0 or weight <= 0 or cost < 0:
            raise ValueError("Неверные данные для ингредиента")

        self.name = name
        self.raw_weight = raw_weight  # вес в сыром виде (граммы)
        self.weight = weight  # вес после приготовления (граммы)
        self.cost = cost  # стоимость (в рублях)

    def __str__(self) -> str:
        return f"{self.name} (сырой вес: {self.raw_weight}г, готовый вес: {self.weight}г, стоимость: {self.cost}руб)"


class Receipt:
    """Класс для работы с рецептом, включая расчеты себестоимости и веса."""

    def __init__(self, name: str, ingredients: list[tuple[str, int, int, int]]) -> None:
        self.name = name
        self.ingredients = [Ingredient(*ingredient) for ingredient in ingredients]

    def calc_cost(self, portions=1) -> int:
        """Рассчитывает себестоимость порции."""
        total_cost = sum(ingredient.cost for ingredient in self.ingredients)
        return total_cost * portions

    def calc_weight(self, portions=1, raw=True) -> int:
        """Рассчитывает общий вес ингредиентов. Можно выбрать сырой или готовый вес."""
        total_weight = sum(ingredient.raw_weight if raw else ingredient.weight for ingredient in self.ingredients)
        return total_weight * portions

    def __str__(self) -> str:
        ingredients_str = ", ".join(str(ingredient) for ingredient in self.ingredients)
        return f"Рецепт: {self.name}\nИнгредиенты: {ingredients_str}"


# Пример рецепта
if __name__ == '__main__':
    receipt_from_api = {
        "title": "Итальянская паста",
        "ingredients_list": [
            ('Мука', 100, 90, 15),
            ('Яйцо', 60, 50, 10),
            ('Оливковое масло', 20, 20, 30),
            ('Соль', 5, 5, 1),
            ('Перец', 2, 2, 2),
        ],
    }

    receipt = Receipt(receipt_from_api['title'], receipt_from_api['ingredients_list'])

    # Проверка методов
    print(receipt)  # Вывод рецепта и ингредиентов
    print("Себестоимость (на 1 порцию):", receipt.calc_cost())
    print("Себестоимость (на 3 порции):", receipt.calc_cost(3))
    print("Вес сырого продукта:", receipt.calc_weight(raw=True))
    print("Вес готового продукта:", receipt.calc_weight(raw=False))

    # Второе блюдо: Спагетти карбонара

    receipt_from_api_2 = {
        "title": "Спагетти карбонара",
        "ingredients_list": [
            ('Спагетти', 200, 180, 50),
            ('Бекон', 100, 80, 60),
            ('Яйцо', 50, 45, 10),
            ('Пармезан', 30, 30, 40),
            ('Сливки', 50, 50, 20),
            ('Соль', 5, 5, 1),
            ('Черный перец', 2, 2, 2),
        ],
    }

    receipt_2 = Receipt(receipt_from_api_2['title'], receipt_from_api_2['ingredients_list'])

    # Проверка методов
    print(receipt_2)  # Вывод рецепта и ингредиентов
    print("Себестоимость (на 1 порцию):", receipt_2.calc_cost())
    print("Себестоимость (на 3 порции):", receipt_2.calc_cost(3))
    print("Вес сырого продукта:", receipt_2.calc_weight(raw=True))
    print("Вес готового продукта:", receipt_2.calc_weight(raw=False))