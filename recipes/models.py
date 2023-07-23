from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# criar tabela de categorias pra fazer relação com a tabela "Recipe" (que contém as informações de cada receita)
class Category(models.Model):
    name = models.CharField(max_length=65)
    def __str__(self) -> str:
        return self.name
        
# criar a class recipe, que vai ser minha "tabela", com informações das receitas.
class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=65)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    # na hora que criar a receita, quero que a data seja lançada automaticamente.
    created_at = models.DateTimeField(auto_now_add=True)
    # a data só vai ser colocada, quando atualizar.
    updated_at = models.DateTimeField(auto_now=True)
    # Está publicada ?  
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    # relacionar a tabela recipe com a tabela category. 
    category = models.ForeignKey(
        # on_delete: caso a pessoa apague, alguma categoria na tabela category, a coluna category aqui, também irá ser apagada
        Category, on_delete=models.SET_NULL, null=True
        )
    authors = models.ForeignKey(
        # on_delete: caso a pessoa apague, algum usuario, a coluna authors aqui também irá ser apagada.
        User, on_delete=models.SET_NULL, null=True
        )
    
    def __str__(self) -> str:
        return self.title