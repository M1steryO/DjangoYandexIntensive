from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_main_page(self):
        response = Client().get(path='/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_item_endpoint(self):
        correct_item_examples = ["123", "3131", "1"]
        for c_item in correct_item_examples:
            correct_response = Client().get(path=f"/catalog/{c_item}/")
            self.assertEqual(correct_response.status_code, 200)

        incorrect_item_examples = ["0", "-123", "1.23", "abc", "1str"]
        for inc_item in incorrect_item_examples:
            incorrect_response = Client().get(path=f"/catalog/{inc_item}/")
            self.assertEqual(incorrect_response.status_code, 404)
