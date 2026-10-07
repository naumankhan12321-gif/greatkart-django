from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):

    list_display = (
        'email',
        'first_name',
        'last_name',
        'username',
        'last_login',
        'date_joined',
        'is_active',
    )

    list_display_links = (
        'email',
        'first_name',
        'last_name',
    )

    readonly_fields = (
        'password',
        'last_login',
        'date_joined',
    )

    ordering = ('date_joined',)

    list_filter = ()
    search_fields = ('email', 'username')


admin.site.register(Account, AccountAdmin)