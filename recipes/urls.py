from django.urls import path
from recipes.views import sobre,contatos,home


urlpatterns = [
    path('',home),
    path('sobre/', sobre),
    path('contatos/', contatos)
]