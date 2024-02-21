from django.contrib import admin
from . models import info

# Register your models here.
class infoAdmin(admin.ModelAdmin):
    list_display = ('id', 'f_name', 'last_name', 'password', 're_password', 'email', 'batch')

admin.site.register(info,infoAdmin)