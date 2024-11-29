from django.contrib import admin

# Register your models here.

from .models import Ingredient, Recipe, RecipeIngredient
"""Image, Time,"""
# admin.site.register(Image)
# admin.site.register(Time)


class IngredientInline(admin.StackedInline):
    """В рецепте есть ингредиенты."""
    model = RecipeIngredient
    extra = 5


class RecipeAdmin(admin.ModelAdmin):
    """Настройка формы админки для рецепта."""
    inlines = [IngredientInline]
    list_display = ('name', 'total_weight_display')

    def total_weight_display(self, obj):
        """Отображение общего веса ингредиентов в админке."""
        return f"{obj.total_weight()} г"

    total_weight_display.short_description = "Общий вес"


admin.site.register(Recipe, RecipeAdmin)


class IngredientAdmin(admin.ModelAdmin):
    """Настройка формы админки для рецепта."""
    list_display = ('name', 'unit', 'weight_per_unit')
    search_fields = ('name',)


admin.site.register(Ingredient, IngredientAdmin)
