from django.test import TestCase
from recipe_catalog.models import Recipe


class TestRecipeOrder(TestCase):

    def test_recipe_order_alphabetical(self):
        # Создаем несколько рецептов
        recipe_1 = Recipe.objects.create(name="Торт")
        recipe_2 = Recipe.objects.create(name="Кекс")
        recipe_3 = Recipe.objects.create(name="Пирог")

        # Получаем рецепты, отсортированные по имени
        recipes = Recipe.objects.all().order_by('name')

        # Проверяем, что рецепты идут в алфавитном порядке
        self.assertEqual([recipe.name for recipe in recipes], ['Кекс', 'Пирог', 'Торт'])
