from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.recipe, name="recipe"),
    path('category/<int:category_id>/', views.category, name="category"),
]