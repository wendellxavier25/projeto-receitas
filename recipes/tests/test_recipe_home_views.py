from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

class RecipeHomeViewsTest(TestCase):
    
    def test_recipe_home_view_fuction_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
        
    def test_recipe_home_view_loads_correct_templates(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
        
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        reponse = self.client.get(reverse('recipes:home'))
        self.assertIn('<h1>No recipes found here</h1>', reponse.content.decode('utf-8'))