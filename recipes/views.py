from django.shortcuts import render

def home(request):
    recipes = recipes
    return render(request,'recipes/pages/home.html', {'recipes': recipes})


def recipes(request, id):
    return render(request,'recipes/pages/recipe-view.html', {'is_detail_page': True,})
