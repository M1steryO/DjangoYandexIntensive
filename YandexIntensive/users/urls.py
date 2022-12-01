from django.contrib.auth.views import LoginView, \
    LogoutView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetView, PasswordChangeView, \
    PasswordResetCompleteView, PasswordChangeDoneView
from django.urls import path, re_path

from . import views
from YandexIntensive.settings import EMAIL_SENDER

from .forms import LoginUserForm
from .views import RegisterView

app_name = 'users'

urlpatterns = [
    path('login/',
         LoginView.as_view(
             template_name="users/login.html",
             form_class=LoginUserForm
         ),
         name="login"),
    path('logout/',
         LogoutView.as_view(
             template_name="users/logged_out.html"
         ),
         name="logout"),
    path('password_change/',
         PasswordChangeView.as_view(
             template_name="users/password_change_form.html"),

         name="password_change"),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(
             template_name="users/password_change_done.html"
         ),
         name="password_change_done"),
    path('password_reset/',
         PasswordResetView.as_view(
             template_name="users/password_reset_form.html",
             email_template_name="users/password_reset_email.html",
             from_email=EMAIL_SENDER
         ),
         name="password_reset"),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(
             template_name="users/password_reset_done.html",
         ),
         name="password_reset_done"),
    path('password_reset/confirm/',
         PasswordResetConfirmView.as_view(
             template_name="users/password_reset_confirm.html"
         ),
         name="password_reset_confirm"),
    path('password_reset/complete/',
         PasswordResetCompleteView.as_view(
             template_name="users/password_reset_complete.html"
         ),
         name="password_reset_complete"),

    path('profile/', views.profile, name="profile"),
    re_path(
        r'user_detail/(?<![-.])\b(?P<pk>[1-9][0-9]*)\b(?!\.[0-9])',
        views.user_detail,
        name="user_detail"
    ),
    path('user_list/', views.user_list, name="user_list"),
    path('register', RegisterView.as_view(), name="register")

]
