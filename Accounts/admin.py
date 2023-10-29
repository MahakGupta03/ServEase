from django.contrib import admin

from .models import CustomUser

# admin.site.register(CustomUser)

# # Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .forms import CustomUserForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    # add_form = CustomUserForm

    model = CustomUser

    list_display = ('name', 'email', 'is_active',
                    'is_staff', 'is_superuser', 'last_login','phone_number')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('phone_number',)
    ordering = ('phone_number',)

admin.site.register(CustomUser, CustomUserAdmin)
