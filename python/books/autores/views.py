from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Autor


class AutorListView(ListView):
    model = Autor
    template_name = 'autores_list.html'


class AutorDetailView(DetailView):
    model = Autor
    template_name = 'autores_detail.html'


class AutorCreateView(CreateView):
    model = Autor
    template_name = 'autores_create.html'
    success_url = ''
    context_object_name = 'autores'


class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'autores_delete.html'
    success_url = ''
