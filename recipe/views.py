from django.shortcuts import render
from .models import Recipe, Category
from django.db import models

def main(request):
    latest_recipes = Recipe.objects.order_by('-created_at')[:5]
    context = {'latest_recipes': latest_recipes}
    return render(request, 'main.html', context)

def category_list(request):
    categories = Category.objects.all()
    category_recipe_counts = {}

    for category in categories:
        recipe_count = Recipe.objects.filter(category=category).count()
        category_recipe_counts[category] = recipe_count

    return render(request, 'category_list.html', {'category_recipe_counts': category_recipe_counts})