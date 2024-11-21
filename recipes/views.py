from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Create your views here.
def index(request):
    return render(request, 'recipes/pages/index.html', context={'recipes': [make_recipe() for _ in range(10)], 'categories':[make_recipe() for _ in range(6)]})

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={'recipe': make_recipe()})