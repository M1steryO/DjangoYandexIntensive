from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_main_page(self):
        response = Client().get(path='/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_item_int_endpoint(self):
        response = Client().get(path="/catalog/123/")
        self.assertEqual(response.status_code, 200)

    # Digit = 0
    def test_catalog_item_zero_endpoint(self):
        response = Client().get(path="/catalog/0/")
        self.assertEqual(response.status_code, 404)

    # Digit < 0
    def test_catalog_item_negative_int_endpoint(self):
        response = Client().get(path="/catalog/-123/")
        self.assertEqual(response.status_code, 404)

    # Digit with dot
    def test_catalog_item_float_endpoint(self):
        response = Client().get(path="/catalog/1.23/")
        self.assertEqual(response.status_code, 404)

    # Str
    def test_catalog_item_str_endpoint(self):
        response = Client().get(path="/catalog/str/")
        self.assertEqual(response.status_code, 404)
