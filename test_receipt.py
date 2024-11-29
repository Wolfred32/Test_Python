import unittest
from dish import Ingredient, Receipt

class TestIngredientAndReceipt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Запуск общего setup для класса TestIngredientAndReceipt")

    @classmethod
    def tearDownClass(cls):
        print("Очистка после всех тестов TestIngredientAndReceipt")

    def setUp(self):
        """Инициализация ингредиентов и рецепта для тестов"""
        self.ingredients_list_1 = [
            ('Мука', 100, 90, 15),
            ('Яйцо', 60, 50, 10),
            ('Оливковое масло', 20, 20, 30),
            ('Соль', 5, 5, 1),
            ('Перец', 2, 2, 2),
        ]
        self.ingredients_list_2 = [
            ('Спагетти', 200, 180, 50),
            ('Бекон', 100, 80, 60),
            ('Яйцо', 50, 45, 10),
            ('Пармезан', 30, 30, 40),
            ('Сливки', 50, 50, 20),
            ('Соль', 5, 5, 1),
            ('Черный перец', 2, 2, 2),
        ]
        self.receipt_1 = Receipt("Итальянская паста", self.ingredients_list_1)
        self.receipt_2 = Receipt("Спагетти карбонара", self.ingredients_list_2)

    def tearDown(self):
        print("Завершение теста")

    def test_calc_cost_receipt_1(self):
        """Тест расчета себестоимости Итальянской пасты на одну и несколько порций."""
        self.assertEqual(self.receipt_1.calc_cost(), 58)  # 15+10+30+1+2 = 58
        self.assertEqual(self.receipt_1.calc_cost(3), 174)

    def test_calc_cost_receipt_2(self):
        """Тест расчета себестоимости Спагетти карбонара на одну и несколько порций."""
        self.assertEqual(self.receipt_2.calc_cost(), 183)  # Проверка расчета
        self.assertEqual(self.receipt_2.calc_cost(2), 366)

    def test_calc_weight_raw_receipt_1(self):
        """Тест расчета общего сырого веса Итальянской пасты."""
        self.assertEqual(self.receipt_1.calc_weight(raw=True), 187)  # 100+60+20+5+2 = 187

    def test_calc_weight_raw_receipt_2(self):
        """Тест расчета общего сырого веса Спагетти карбонара."""
        self.assertEqual(self.receipt_2.calc_weight(raw=True), 437)  # Проверка веса

    def test_calc_weight_cooked_receipt_1(self):
        """Тест расчета общего веса готового продукта Итальянской пасты."""
        self.assertEqual(self.receipt_1.calc_weight(raw=False), 167)  # 90+50+20+5+2 = 167

    def test_calc_weight_cooked_receipt_2(self):
        """Тест расчета общего веса готового продукта Спагетти карбонара."""
        self.assertEqual(self.receipt_2.calc_weight(raw=False), 392)  # Проверка веса

    def test_invalid_ingredient(self):
        """Тест обработки неверных данных ингредиента."""
        with self.assertRaises(ValueError):
            Ingredient("", -100, -90, -10)

if __name__ == '__main__':
    unittest.main()