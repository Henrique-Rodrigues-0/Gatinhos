from django.urls import path
from galeria_gatos.views import index

urlpatterns = [
    path('', index)
]