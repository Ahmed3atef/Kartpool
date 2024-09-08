from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'karma_points', 'is_staff', ] # new
    fieldsets = UserAdmin.fieldsets + ( # new
        (None, {'fields': ('karma_points',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ( # new
        (None, {'fields': ('karma_points',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
