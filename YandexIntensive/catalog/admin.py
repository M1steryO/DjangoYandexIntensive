from django.contrib import admin
from .models import Item, Category, Tag, Gallery, Photo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class GalleryInLine(admin.StackedInline):
    model = Gallery


class PhotoInLine(admin.StackedInline):
    model = Photo


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published", "is_on_main")
    list_editable = ("is_published", "is_on_main")
    list_display_links = ("name",)
    filter_horizontal = ('tags',)
    inlines = [GalleryInLine, PhotoInLine, ]
