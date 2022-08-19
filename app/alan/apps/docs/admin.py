from django.contrib import admin
from .models import Speciality, Category, Information, Document


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_per_page = 20
    readonly_fields = ('id',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code',)
    list_per_page = 20
    readonly_fields = ('id',)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'file', )
    search_fields = ('speciality__name', 'category_name')
    list_per_page = 20
    readonly_fields = ('id',)
