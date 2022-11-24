from django.db import models
from django.utils import timezone


class FeedbackModel(models.Model):
    text = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Фидбэки"
        verbose_name_plural = "Фидбэк"

    def __str__(self):
        return str(self.created_on)
