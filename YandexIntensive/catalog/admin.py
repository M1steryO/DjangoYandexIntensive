from django.contrib import admin
from .models import Item, Category, Tag, Gallery, Photo


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published",)
    list_editable = ("is_published",)
    list_display_links = ("name",)
    filter_horizontal = ('tags',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
