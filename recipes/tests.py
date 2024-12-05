from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:index')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id' : 1})
        self.assertEqual(url, '/category/1/')

    def test_recipe_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id' : 1})
        self.assertEqual(url, '/1/')
