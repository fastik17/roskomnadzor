from django.contrib import admin
from sites.models import UserRequest, BlockedSites


class BlockedSitesAdmin(admin.ModelAdmin):
    list_display = ['site', 'is_blocked', 'email_was_sent']


class UserRequestAdmin(admin.ModelAdmin):
    list_display = ['domain_name', 'id']


admin.site.register(UserRequest, UserRequestAdmin)
admin.site.register(BlockedSites, BlockedSitesAdmin)

