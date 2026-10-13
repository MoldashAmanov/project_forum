from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """
    Наследуемся, чтобы получить бесплатно: проверку сложности пароля,
    совпадение паролей, хэширование пароля при сохранении
    """
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')