from django.http import HttpResponse
from django.shortcuts import render


def item_detail(request, pk: int):
    return HttpResponse("Подробно элемент")


def item_list(request):
    template_name = 'catalog/index.html'
    context = {'active': 'catalog'}
    return render(request, template_name, context)
