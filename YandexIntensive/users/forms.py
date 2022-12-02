from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile, CustomUser


class UpdateProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ['birthday']
        labels = {
            Profile.birthday.field.name: 'День рождения',
        }
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class UpdateUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CustomUser
        fields = ['email']


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CustomUser
        fields = '__all__'
