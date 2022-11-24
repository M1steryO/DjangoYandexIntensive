from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from dotenv import load_dotenv

from .forms import FeedbackForm, FeedbackModel
from YandexIntensive.settings import EMAIL_SENDER

load_dotenv()


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
        EMAIL_SENDER,
        ['to@example.com'],
        fail_silently=True,
    )
    messages.success(request, "Спасибо, ваш отзыв принят")
    fb = FeedbackModel.objects.create(
        text=form.cleaned_data['text']
    )
    fb.save()
    return redirect("feedback:feedback")
