from django.contrib import admin
from .models import Category, Recipe
# Register your models here.
# criar uma classe pra área administrativa do meu model 

# registrar as categorias no meu admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


# registrar as receitas no admin
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...