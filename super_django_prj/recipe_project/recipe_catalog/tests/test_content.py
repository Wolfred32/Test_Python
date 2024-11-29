from django.test import TestCase
from recipe_catalog.models import Recipe, Ingredient, RecipeIngredient

class TestModels(TestCase):

    def test_create_ingredient(self):
        ingredient = Ingredient.objects.create(name="Сахар", unit="g", weight_per_unit=1)
        self.assertEqual(ingredient.name, "Сахар")
        self.assertEqual(ingredient.unit, "g")
        self.assertEqual(ingredient.weight_per_unit, 1)

    def test_create_recipe(self):
        recipe = Recipe.objects.create(name="Торт")
        self.assertEqual(recipe.name, "Торт")

    def test_create_recipe_ingredient(self):
        ingredient = Ingredient.objects.create(name="Сахар", unit="g", weight_per_unit=1)
        recipe = Recipe.objects.create(name="Торт")
        recipe_ingredient = RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient, quantity=200)
        self.assertEqual(recipe_ingredient.recipe, recipe)
        self.assertEqual(recipe_ingredient.ingredient, ingredient)
        self.assertEqual(recipe_ingredient.quantity, 200)
