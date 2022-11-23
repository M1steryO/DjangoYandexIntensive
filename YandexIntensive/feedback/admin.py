from django.contrib import admin
from .forms import FeedbackModel


@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin):
    pass
