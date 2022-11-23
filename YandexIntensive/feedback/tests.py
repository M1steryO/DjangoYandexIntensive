from django.test import Client, TestCase
from django.urls import reverse

from .forms import FeedbackForm, FeedbackModel


class FormTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_name_label(self):
        name_label = FormTests.form.fields['text'].label
        correct_label_name = 'Текст'
        self.assertEqual(name_label, correct_label_name)

    def test_name_help_text(self):
        name_help_text = FormTests.form.fields['text'].help_text
        correct_help_text_name = 'Напишите о том, чтобы вы хотели изменить'
        self.assertEqual(name_help_text, correct_help_text_name)

    def test_correct_context(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertIn('form', response.context)

    def test_correct_post_data(self):
        form_data = {
            'text': 'Исправьте пожалуйста все!'
        }
        response = Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True
        )
        feedback_count = FeedbackModel.objects.count()
        self.assertRedirects(response, reverse('feedback:feedback'))
        self.assertEqual(feedback_count, 1)
