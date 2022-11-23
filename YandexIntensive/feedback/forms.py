from django import forms
from django.db import models
import datetime


class FeedbackModel(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(default=datetime.datetime.now())


class FeedbackForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = FeedbackModel
        fields = (
            FeedbackModel.text.field.name,
        )
        labels = {
            FeedbackModel.text.field.name: 'Текст',
        }
        help_texts = {
            FeedbackModel.text.field.name: "Напишите о том,"
                                           " чтобы вы хотели изменить"
        }
