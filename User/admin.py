from django.contrib import admin

from .models import UserDetail

# Register your models here.

class JoinUserDetails(admin.ModelAdmin):
    list_display = ['name', 'username', 'email', 'telephone']

    class Meta:
        mode = UserDetail


admin.site.register(UserDetail, JoinUserDetails)