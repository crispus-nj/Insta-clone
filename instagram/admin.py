from django.contrib import admin
from .models import UserAccount
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class StyleUserAccount(UserAdmin):
    list_display = ('username', 'email', 'fullname', 'date_joined', 'last_login', 'is_admin', 'is_active')
    list_display_links = ('username','email',)
    list_filter = ()
    filter_horizontal = ()
    fieldsets = ()
    

admin.site.register(UserAccount, StyleUserAccount)
