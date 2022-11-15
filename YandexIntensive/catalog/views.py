from django.shortcuts import render, get_object_or_404
from django import template

from .models import Item, Category


def item_detail(request, pk: int):
    template_name = 'catalog/item_detail.html'
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item,
    }
    return render(request, template_name, context)


def item_list(request):
    template_name = 'catalog/index.html'
    items = Item.objects.item_list_published()
    categories = Category.objects.all()
    context = {
        'active': 'catalog',
        'items': items,
        'categories': categories
    }

    return render(request, template_name, context)



