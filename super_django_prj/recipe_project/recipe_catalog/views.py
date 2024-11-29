from django.shortcuts import render

# Файл приложения views.py
from django.http import HttpResponse

from .models import Recipe


def about(request):
    template_name = 'recipe_catalog/about.html'

    # return HttpResponse('О проекте')
    return render(request, template_name)


def index(request):
    template_name = 'recipe_catalog/index.html'

    recipes = Recipe.objects.all().order_by('name')
    context = {
        'recipes': recipes,
    }

    # return HttpResponse('Главная страница')
    return render(request, template_name, context)


def recipe_detail(request, pk):
    template_name = 'recipe_catalog/recipe.html'

    recipe = Recipe.objects.get(pk=pk)
    context = {
        'title': recipe.name,
        'recipe_id': pk,
        'ingredients': recipe.ingredients.order_by('name')
    }

    # title = 'Блинчики с мясом!'
    # context = {
    #     'title': title,
    #     'recipe_id': pk,
    # }

    # return HttpResponse(f'А тут будет описание рецепта id = {pk}')
    return render(request, template_name, context)

