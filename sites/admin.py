from django.contrib import admin
from . models import (
    Category,
    Site,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'description', 'updated', 'timestamp', )
