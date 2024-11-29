from django.test import TestCase
from recipe_catalog.models import Recipe, Ingredient, RecipeIngredient

class TestRecipeWeight(TestCase):

    def test_calculate_weight_in_grams(self):
        # Создаем ингредиенты с разными единицами измерения
        ingredient_1 = Ingredient.objects.create(name="Сахар", unit="g", weight_per_unit=1)
        ingredient_2 = Ingredient.objects.create(name="Мука", unit="g", weight_per_unit=2)
        # Создаем рецепт
        recipe = Recipe.objects.create(name="Торт")
        # Добавляем ингредиенты в рецепт
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient_1, quantity=200)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient_2, quantity=150)
        # Проверяем расчет веса
        self.assertEqual(recipe.calculate_weight(), 200 + 150 * 2)

    def test_calculate_weight_in_tablespoons(self):
        # Создаем ингредиенты в ложках
        ingredient_1 = Ingredient.objects.create(name="Сахар", unit="tbsp", weight_per_unit=20)
        ingredient_2 = Ingredient.objects.create(name="Мука", unit="tbsp", weight_per_unit=25)
        # Создаем рецепт
        recipe = Recipe.objects.create(name="Торт")
        # Добавляем ингредиенты в рецепт
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient_1, quantity=3)
        RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient_2, quantity=4)
        # Проверяем расчет веса
        self.assertEqual(recipe.calculate_weight(), 3 * 20 + 4 * 25)
