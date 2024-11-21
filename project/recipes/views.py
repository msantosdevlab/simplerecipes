from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'recipes/pages/index.html')

def recipe(request, id):
    return render(request, 'recipes/pages/recipe.html')