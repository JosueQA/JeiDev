from django.contrib import admin
from .models import AppModel

class AppModelAdmin(admin.ModelAdmin):
    model = AppModel
    list_display = ('name', 'description', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(AppModel, AppModelAdmin)