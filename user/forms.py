from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserChangeForm(UserChangeForm):
    """"""
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')


class CustomUserCreationForm(UserCreationForm):
    """"""
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')
