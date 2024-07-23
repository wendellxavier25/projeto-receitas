from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.http import Http404

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request,'recipes/pages/home.html', {'recipes': recipes})

def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    
    if not recipes:
        raise Http404('Not found')
    
    return render(request,'recipes/pages/category.html', {'recipes': recipes, 'title': f'{recipes.first().category.name}'})


def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)
    
    return render(request,'recipes/pages/recipe-view.html', {'is_detail_page': True, 'recipe': recipe,})
