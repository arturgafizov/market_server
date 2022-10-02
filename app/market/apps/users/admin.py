from django.contrib import admin
from django.conf import settings
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from .models import IdentificationCode

User = get_user_model()


class IdentificationCodeInline(admin.TabularInline):
    model = IdentificationCode
    extra = 0


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ('-id',)
    list_display = ('email', 'full_name', 'is_active', 'username', 'role', 'phone', 'position')
    search_fields = ('first_name', 'last_name', 'email', 'role', 'phone', )
    list_display_links = ('email', 'username', )
    list_filter = ('is_active', 'is_staff', 'role', 'position')
    list_editable = ('is_active', )
    list_per_page = 20
    inlines = [IdentificationCodeInline, ]
    fieldsets = (
        (_('Personal info'), {'fields': ('id', 'first_name', 'last_name', 'email', 'username', 'role', 'phone',
                                         )}),
        (_('Secrets'), {'fields': ('password',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('id',)


class CustomOutstandingTokenAdmin(OutstandingTokenAdmin):
    def has_delete_permission(self, *args, **kwargs):
        return True  # or whatever logic you want


title = settings.MICROSERVICE_TITLE

admin.site.site_title = title
admin.site.site_header = title
admin.site.site_url = '/'
admin.site.index_title = title

# admin.site.unregister(Group)
admin.site.unregister(OutstandingToken)
admin.site.register(OutstandingToken, CustomOutstandingTokenAdmin)
