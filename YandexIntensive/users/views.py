from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import UpdateProfileForm,\
    UpdateUserForm,\
    CustomUserCreationForm
from .models import Profile, CustomUser


@login_required
def profile(request):
    template_name = "users/profile.html"

    Profile.objects.get_or_create(user_id=request.user.id)

    if request.method == 'POST':
        user_form = UpdateUserForm(
            request.POST,
            instance=request.user
        )
        profile_form = UpdateProfileForm(
            request.POST,
            instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Твой профиль успешно обновлен')
            return redirect(reverse('users:profile'))

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    context = {
        'user': request.user,
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, template_name, context)


def user_detail(request, pk):
    template_name = "users/user_detail.html"
    user = CustomUser.objects.get(pk=pk)
    context = {
        'user': user,
    }
    return render(request, template_name, context)


def user_list(request):
    template_name = "users/user_list.html"
    users = CustomUser.objects.filter(is_superuser=False)
    context = {
        'users': users,
        'active': True
    }

    return render(request, template_name, context)


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:login")
    template_name = "users/sign_up.html"
