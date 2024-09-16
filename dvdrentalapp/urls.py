from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.customer, name='mycustomer'),
    path('detalhes/<int:id>', views.detalhes, name='myDetalhe'),
    path('edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),

    # CATEGORIAS
    path('add_category/', views.add_category, name='add_category'),
    path('categories/', views.list_categories, name='list_categories'),

    # DESAFIO DE LISTAR E EDITAR ELEMENTOS
    path('cidade/', views.cidade, name='minhaCidade'),
    path('edit_cidade/<int:city_id>/', views.edit_cidade, name='edit_cidade'),

    # DESAFIO DE ADICIONAR ELEMENTOS
    path('desafio_adicionar/', views.adicionar_linguagem, name='desafio_adicionar'),
    path('linguagens/', views.listar_linguagens, name='desafio_listar_linguagem'),

    # ATIVIDADE
    path('home/', views.home),
    path('clientes/', views.clientes, name='meusClientes'),
    path('endereco/<int:id>', views.endereco, name='meuEndereco'),
    path('pagamentos/<int:id>', views.pagamento, name='meuPagamento'),

    # AULA 27 (11/09) - QUERYSET
    path('listacustomer/', views.listacustomer, name='listacustomer'),
]
