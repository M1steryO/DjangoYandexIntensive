from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse

from .models import Category, Tag, Item


class StaticURLTests(TestCase):
    fixtures = ['category.json',
                'tags.json',
                'item.json']
    endpoint_status = {
        '/catalog/': 200,
        '/catalog/0/': 404,
        '/catalog/-1/': 404,
        '/catalog/1str/': 404,
    }

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_catalog_pages(self):
        for url, status in self.endpoint_status.items():
            with self.subTest(url=url):
                response = Client().get(path=url)
                self.assertEqual(status, response.status_code)


class ModelsTest(TestCase):
    item_text_checking = {
        "text": False,
        "превосходно": True,
        "роскошно": True
    }
    category_weight = {
        0: False,
        100: True,
        32769: False,
    }

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            is_published=True,
            name='Тестовая категория',
            slug="test-category-slug",
            weight=150)
        cls.tag = Tag.objects.create(
            is_published=True,
            name="Тестовый тег",
            slug="test-tag-slug")

    def test_create_one_letter(self):
        item_count = Item.objects.count()

        for text, is_correct in self.item_text_checking.items():
            with self.subTest(text=text):
                if is_correct:
                    self.item = Item(
                        name="Тестовый item",
                        category=self.category,
                        text=text)
                    self.item.full_clean()
                    self.item.save()
                    self.item.tags.add(self.tag)
                    self.assertEqual(Item.objects.count(), item_count + 1)
                    item_count += 1
                else:
                    with self.assertRaises(ValidationError):
                        self.item = Item(name="Тестовый item",
                                         category=self.category,
                                         text=text)
                        self.item.full_clean()
                        self.item.save()
                        self.item.tags.add(self.tag)
                    self.assertEqual(Item.objects.count(), item_count)

    def test_create_category_weight(self):
        category_count = Category.objects.count()

        for weight, is_correct in self.category_weight.items():
            with self.subTest(weight=weight):
                if is_correct:
                    self.category = Category(is_published=True,
                                             name='Тестовая категория',
                                             slug="category-slug",
                                             weight=weight)
                    self.category.full_clean()
                    self.category.save()
                    self.assertEqual(Category.objects.count(),
                                     category_count + 1)
                    category_count += 1
                else:
                    with self.assertRaises(ValidationError):
                        self.category = Category(is_published=True,
                                                 name='Тестовая категория',
                                                 slug="category-slug",
                                                 weight=weight)
                        self.category.full_clean()
                        self.category.save()
                    self.assertEqual(Category.objects.count(),
                                     category_count)


class TaskPagesTest(TestCase):
    fixtures = ['category.json',
                'tags.json',
                'item.json']

    def test_catalog_page_show_correct_context(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), 2)
