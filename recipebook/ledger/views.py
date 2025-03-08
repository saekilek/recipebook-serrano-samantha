from django.shortcuts import render
from .models import Recipe, RecipeIngredient

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {"recipes": recipes})

def recipe_ingredients(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_ingredients.html', {"recipe": recipe})