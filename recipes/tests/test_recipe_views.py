from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

# Create your tests here.
class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function(self):
        view = resolve(reverse('recipes:index'))
        self.assertIs(view.func, views.index)

    def test_recipe_category_view_function(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id' : 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_view_function(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id' : 1}))
        self.assertIs(view.func, views.recipe, msg="corretinho")