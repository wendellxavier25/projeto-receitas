from django.test import TestCase
from django.urls import reverse
from recipes import views


class RecipeSearchViewsTest(TestCase):
    def test_recipe_search_uses_correct_view_function(self):
        resolved = reverse(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)
        
    def test_recipe_search_raises_404_if_no_search_term(self):
        reponse = self.client.get(reverse('recipes:home'))
        self.assertEqual(reponse.status_code, 404)
        
    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse('recipes:search') + '?q=teste'
        response = self.client.get(url)
        self.assertIn('Search for &quot;&lt;teste&gt;&quot;', response.content.decode('utf-8'))