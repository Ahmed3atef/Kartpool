from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Removing password-based authentication
        if 'usable_password' in self.fields:
            del self.fields['usable_password']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields