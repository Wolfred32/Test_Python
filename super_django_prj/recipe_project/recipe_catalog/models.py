from django.db import models


# Create your models here.

class Ingredient(models.Model):
    """Составная часть рецепта."""
    UNIT_CHOICES = [
        ('g', 'Граммы'),
        ('pcs', 'Штуки'),
        ('tbsp', 'Ложки (столовые)'),
        ('cup', 'Стаканы'),
    ]
    name = models.CharField(max_length=255, verbose_name="Название")
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, verbose_name="Единица измерения", default='g')
    weight_per_unit = models.FloatField(
        verbose_name="Вес одной единицы в граммах",
        help_text="Для граммов оставьте 1, для других укажите эквивалент в граммах."
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Вкусное делается по рецепту."""
    name = models.CharField(max_length=300, verbose_name="Название")
    ingredients = models.ManyToManyField(
        Ingredient, through="RecipeIngredient", verbose_name="Ингредиенты")

    def __str__(self):
        return self.name

    def total_weight(self):
        """Рассчитать общий вес всех ингредиентов в рецепте в граммах."""
        return sum(ri.total_weight() for ri in self.recipeingredient_set.all())

    def get_ingredients_list(self):
        """Список ингредиентов с количеством для отображения."""
        return [
            f"{ri.ingredient.name} - {ri.quantity} {ri.ingredient.get_unit_display()} ({ri.total_weight()} г)"
            for ri in self.recipeingredient_set.all()
        ]


class RecipeIngredient(models.Model):
    """Один ингредиент может быть
    в нескольких рецептах,
    как и в одном рецепте может быть
    несколько ингредиентов."""
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name="Рецепт")
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, verbose_name="Ингредиент")
    quantity = models.FloatField(
        verbose_name="Количество",
        help_text="Количество ингредиента в выбранной единице измерения."
    )

    def __str__(self):
        return f'{self.recipe.name} - {self.ingredient.name} ({self.quantity} {self.ingredient.get_unit_display()})'

    def total_weight(self):
        """Рассчитать вес ингредиента в граммах."""
        return self.quantity * self.ingredient.weight_per_unit

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_recipes_ingredients'
            )
        ]

# class Image(models.Model):
#     """Картинка готового блюда."""
#     name = models.ImageField(width_field=500, height_field=500)
#
#
# class Time(models.Model):
#     """Время приготовления."""
#     name = models.TimeField(max_length=255)
