from django.contrib import admin
from .models import Item, Category, Tag


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published")
    fields = ("is_published", "name", "category", "tags", "text")
    list_editable = ("is_published",)
    list_display_links = ("name",)
    filter_horizontal = ('tags',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
