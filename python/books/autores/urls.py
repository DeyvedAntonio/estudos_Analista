from django.urls import path
from .views import (
    AutorCreateView,
    AutorDeleteView,
    AutorDetailView,
    AutorListView,
)


urlspatterns = [
    path('criar/', AutorCreateView.as_view(), name='autores_list'),
    path('<int:pk>/deletar/', AutorDeleteView.as_view(), name='autores_delete'),
    path('<int:pk>/detalhe/', AutorDetailView.as_view(), name='autores_detail'),
    path('lista/', AutorListView.as_view(), name='autores_list'),
]
