from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_main_page(self):
        response = Client().get(path='/about/')
        self.assertEqual(response.status_code, 200)
