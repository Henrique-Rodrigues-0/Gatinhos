from django.urls import path
from galeria_gatos.views import index

# este arquivo foi criado por mim e não pelo django, é um URLconf separado, no setup/urls tem a explicação
# aqui definimos as rotas para as paginas do site, ao acessar o endereço principal representado pela string vazia
# é retornado a função index que contem uma página html

urlpatterns = [
    path('', index)
]