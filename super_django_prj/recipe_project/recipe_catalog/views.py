from django.shortcuts import render, get_object_or_404

# Файл приложения views.py
from django.http import HttpResponse

from .models import Recipe


def about(request):
    template_name = 'recipe_catalog/about.html'

    # return HttpResponse('О проекте')
    return render(request, template_name)


def index(request):
    template_name = 'recipe_catalog/index.html'

    recipes = Recipe.objects.prefetch_related('recipeingredient_set__ingredient').order_by('name')
    context = {
        'recipes': recipes,
    }

    # return HttpResponse('Главная страница')
    return render(request, template_name, context)


def recipe_detail(request, pk):
    template_name = 'recipe_catalog/recipe.html'

    # Получаем рецепт с его ингредиентами
    recipe = get_object_or_404(Recipe.objects.prefetch_related('recipeingredient_set__ingredient'), pk=pk)
    # Формируем список ингредиентов с деталями
    ingredients = recipe.recipeingredient_set.all()
    # Генерация данных для шаблона
    context = {
        'title': recipe.name,
        'recipe_id': pk,
        'recipe': recipe,
        'ingredients': ingredients,
        'total_weight': recipe.total_weight(),
    }

    # title = 'Блинчики с мясом!'
    # context = {
    #     'title': title,
    #     'recipe_id': pk,
    # }

    # return HttpResponse(f'А тут будет описание рецепта id = {pk}')
    return render(request, template_name, context)

