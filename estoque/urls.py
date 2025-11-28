# projeto/urls.py
# estoque/urls.py
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.tabela, name='tabela'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('editar/<int:pk>/', views.editar, name='editar'),
    path('excluir/<int:pk>/', views.excluir, name='excluir'),
]
