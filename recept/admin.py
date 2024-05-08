from django.contrib import admin
from recept.models import Categories,SubCategories,Recepts
# Register your models here.

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

@admin.register(Recepts)
class ReceptsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}