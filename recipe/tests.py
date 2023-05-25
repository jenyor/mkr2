from django.test import TestCase
from django.urls import reverse
from .models import Category, Recipe


class MainViewTest(TestCase):
    def test_main_view_returns_last_5_recipes(self):
        # Створюємо тестові об'єкти рецептів
        category1 = Category.objects.create(name='Category 1')
        Recipe.objects.create(title='Recipe 1', description='Description 1', instructions='Instructions 1', ingredients='Ingredients 1', category=category1)
        Recipe.objects.create(title='Recipe 2', description='Description 2', instructions='Instructions 2', ingredients='Ingredients 2', category=category1)
        Recipe.objects.create(title='Recipe 3', description='Description 3', instructions='Instructions 3', ingredients='Ingredients 3', category=category1)
        Recipe.objects.create(title='Recipe 4', description='Description 4', instructions='Instructions 4', ingredients='Ingredients 4', category=category1)
        Recipe.objects.create(title='Recipe 5', description='Description 5', instructions='Instructions 5', ingredients='Ingredients 5', category=category1)
        Recipe.objects.create(title='Recipe 6', description='Description 6', instructions='Instructions 6', ingredients='Ingredients 6', category=category1)

        # Отримуємо URL для view 'main'
        url = reverse('main')

        # Виконуємо GET-запит на URL
        response = self.client.get(url)

        # Перевіряємо, що сторінка завантажена успішно
        self.assertEqual(response.status_code, 200)

        # Перевіряємо, що на сторінці відображаються останні 5 рецептів
        self.assertContains(response, 'Recipe 2')
        self.assertContains(response, 'Recipe 3')
        self.assertContains(response, 'Recipe 4')
        self.assertContains(response, 'Recipe 5')
        self.assertContains(response, 'Recipe 6')


class CategoryListViewTest(TestCase):
    def test_category_list_view_displays_categories_with_recipe_counts(self):
        # Створюємо тестові об'єкти категорій і рецептів
        category1 = Category.objects.create(name='Category 1')
        category2 = Category.objects.create(name='Category 2')
        category3 = Category.objects.create(name='Category 3')

        Recipe.objects.create(title='Recipe 1', description='Description 1', instructions='Instructions 1', ingredients='Ingredients 1', category=category1)
        Recipe.objects.create(title='Recipe 2', description='Description 2', instructions='Instructions 2', ingredients='Ingredients 2', category=category1)
        Recipe.objects.create(title='Recipe 3', description='Description 3', instructions='Instructions 3', ingredients='Ingredients 3', category=category2)

        # Отримуємо URL для view 'category_list'
        url = reverse('category_list')

        # Виконуємо GET-запит на URL
        response = self.client.get(url)

        # Перевіряємо, що сторінка завантажена успішно
        self.assertEqual(response.status_code, 200)

        # Перевіряємо, що на сторінці відображаються категорії з кількістю рецептів
        self.assertContains(response, 'Category 1 - 2')
        self.assertContains(response, 'Category 2 - 1')
        self.assertContains(response, 'Category 3 - 0')

