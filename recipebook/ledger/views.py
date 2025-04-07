from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient, RecipeImage, Ingredient
from .forms import RecipeForm, RecipeImageForm, RecipeIngredientForm, IngredientForm

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

@login_required
def add_recipe(request):
    recipe = None
    recipe_form = RecipeForm()
    ingredient_form = IngredientForm()
    recipe_ingredient_form = RecipeIngredientForm()
    if request.method == 'POST':
        if 'make_recipe' in request.POST:
            recipe_form = RecipeForm(request.POST)
            if recipe_form.is_valid():
                recipe = recipe_form.save(commit=False)
                recipe.author = request.user
                recipe.save()
        elif 'make_ingredient' in request.POST:
            ingredient_form = IngredientForm(request.POST)
            if ingredient_form.is_valid():
                ingredient_form.save()
        elif 'make_recipe_ingredient' in request.POST:
            recipe_ingredient_form = RecipeIngredientForm(request.POST)
            if recipe_ingredient_form.is_valid():
                recipe_ingredient_form.save()
        return redirect('ledger:add_recipe')
    return render(request, 'add_recipe.html', {
        'recipe_form': recipe_form,
        'ingredient_form': ingredient_form,
        'recipe_ingredient_form': recipe_ingredient_form,
        'recipe': recipe,
        'ingredients': Ingredient.objects.all(),
        'recipes': Recipe.objects.all(),
    })

@login_required
def add_recipe_image(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect('ledger:recipe_ingredients', recipe_id=recipe.id)
    else:
        form = RecipeImageForm()
    return render(request, 'add_recipe_image.html', {'form': form, 'recipe': recipe})