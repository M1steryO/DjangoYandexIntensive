from django.shortcuts import render, get_object_or_404

from .models import Item, Category, Photo


def item_detail(request, pk: int):
    template_name = 'catalog/item_detail.html'
    item = get_object_or_404(Item, pk=pk)
    photo = get_object_or_404(Photo, item=item.id)
    context = {
        'item': item,
        'photo': photo
    }
    return render(request, template_name, context)


def item_list(request):
    template_name = 'catalog/index.html'
    items = Item.objects.item_list_published()
    categories = Category.objects.only('name')
    photos = Photo.objects.select_related('item')
    context = {
        'active': 'catalog',
        'items': items,
        'categories': categories,
        'photos': photos
    }

    return render(request, template_name, context)
