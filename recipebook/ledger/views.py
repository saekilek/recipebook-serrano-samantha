from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {"recipes": recipes})

@login_required
def recipe_ingredients(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_ingredients.html', {"recipe": recipe})

def home(request):
    return render(request, 'homepage.html')