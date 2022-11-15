from django.test import Client, TestCase
from django.urls import reverse


class StaticURLTests(TestCase):
    def test_catalog_main_page(self):
        response = Client().get(path='/')
        self.assertEqual(response.status_code, 200)


class TaskPagesTest(TestCase):
    fixtures = ['category.json',
                'tags.json',
                'item.json']

    def test_homepage_page_show_correct_context(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), 2)
