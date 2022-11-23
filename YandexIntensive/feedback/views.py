from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import FeedbackForm


def feedback(request):
    template_name = 'feedback/index.html'
    form = FeedbackForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'POST' and form.is_valid():
        return send_form(request, form)
    return render(request, template_name, context)


def send_form(request, form):
    send_mail(
        'Feedback',
        form.cleaned_data['text'],
        'from@example.com',
        ['to@example.com'],
        fail_silently=True,
    )
    return redirect("feedback:feedback")
