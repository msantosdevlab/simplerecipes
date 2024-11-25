from django.shortcuts import render
from utils.recipes.factory import make_recipe
from django.templatetags.static import static
from .models import Recipe, Category

# Create your views here.
def index(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    categories = Category.objects.all().order_by('-id')
    for recipe in recipes:
        recipe.cover_url = recipe.cover.url if recipe.cover else static('recipes/images/default-image.png')
    return render(request, 'recipes/pages/index.html', context={'recipes': recipes, 'categories': categories})

def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.cover_url = recipe.cover.url if recipe.cover else static('recipes/images/default-image.png')
    return render(request, 'recipes/pages/recipe-view.html', context={'recipe': recipe})

def category(request, category_id):
    category_name = Category.objects.get(id=category_id).name
    recipes = Recipe.objects.filter(category_id=category_id , is_published=True).order_by('-id')
    for recipe in recipes:
        recipe.cover_url = recipe.cover.url if recipe.cover else static('recipes/images/default-image.png')
    return render(request, 'recipes/pages/list_category.html', context={'recipes': recipes, 'category_name': category_name})