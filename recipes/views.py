from django.shortcuts import render
from utils.recipes.factory import make_recipe
from django.templatetags.static import static
from .models import Recipe

# Create your views here.
def index(request):
    recipes = Recipe.objects.all().order_by('-id')
    for recipe in recipes:
        recipe.cover_url = recipe.cover.url if recipe.cover else static('recipes/images/default-image.png')
    return render(request, 'recipes/pages/index.html', context={'recipes': recipes})

def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.cover_url = recipe.cover.url if recipe.cover else static('recipes/images/default-image.png')
    return render(request, 'recipes/pages/recipe-view.html', context={'recipe': recipe})
