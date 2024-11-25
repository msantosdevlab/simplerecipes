from django.contrib import admin
from .models import Category, Recipe

admin.site.site_header = "Hebrom Pneus"
admin.site.site_title = "Administração do Projeto"
admin.site.index_title = "Bem-vindo ao painel"

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...
