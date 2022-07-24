from ast import Return
from django.shortcuts import render
# importaciones para CRUD
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from post.models import Posts




# Create your views here.
#metodo CRUD para los datos de los post

#lista - R - read
class PostList(ListView):

    model = Posts
    tempralte_name = "post/post_list.html"
#detalle - R - read
class PostDetalle(DetailView):

    model = Posts
    template_name = "post/post_detalle.html"
#C - Create
class PostCreacion(CreateView):

    model = Posts
    template_name = "/post/post/list"
    fields = ["titulo","subtitulo"]

#U - Update
class PostUpdate(UpdateView):

    model = Posts
    template_name = "/post/post/list"
    fields = ["titulo","subtitulo"]

#D - delete
class PostDelate(DeleteView):

    model = Posts
    success_url = "/post/post/list"

