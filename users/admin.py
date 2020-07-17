from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

User = get_user_model()


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    ordering = ('email',)
    fieldsets = (("User", {"fields":
                    ('email', 'password', 'first_name', 'last_name',
                     'is_staff', 'is_active')}),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',
                       'password1', 'password2'),
        }),)
    list_display = ["email", "id"]
    search_fields = ["email"]
