from django.test import TestCase
from django.urls import reverse
from recipe_catalog.models import Recipe, Ingredient

class TestRoutes(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('recipe_catalog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Главная страница')

    def test_recipe_detail_page(self):
        # Создаем тестовый рецепт и ингредиент
        ingredient = Ingredient.objects.create(name="Сахар", unit="g", weight_per_unit=1)
        recipe = Recipe.objects.create(name="Торт")
        recipe.ingredients.add(ingredient)
        response = self.client.get(reverse('recipe_catalog:recipe_detail', args=[recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, recipe.name)
        self.assertContains(response, 'Общий вес')

    def test_about_page(self):
        response = self.client.get(reverse('recipe_catalog:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'О проекте')
