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
        self.assertIs(view.func, views.recipe)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertEqual(response.status_code, 200, msg=f"O código recebido foi {response.status_code}, mas esperávamos 200.")

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:index'))
        self.assertTemplateUsed(response, 'recipes/pages/index.html')