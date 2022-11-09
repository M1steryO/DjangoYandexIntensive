from django.shortcuts import render


def home(request):
    template_name = 'homepage/index.html'
    context = {'active': 'home'}
    return render(request, template_name, context)
