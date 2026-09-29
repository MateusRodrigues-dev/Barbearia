from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path(
        'clientes/novo/',
        views.criar_cliente,
        name='cliente_criar'
    ),

    path(
        'clientes/',
        views.lista_clientes,
        name='clientes'
    ),

    path(
        'clientes/<int:id>/',
        views.detalhe_cliente,
        name='cliente_detalhes'
    ),
    path(
    'clientes/<int:id>/editar/',
    views.editar_cliente,
    name='cliente_editar'
),
path(
    'clientes/<int:id>/excluir/',
    views.excluir_cliente,
    name='cliente_excluir'
),
path('accounts/', include('django.contrib.auth.urls')),
]