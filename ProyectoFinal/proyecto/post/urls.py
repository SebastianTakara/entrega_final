from django.urls import path

from post import views

urlpatterns = [

    
    path("list", views.PostList.as_view(), name= "List"),
    path(r'^(?P<pk>\d+)$', views.PostDetalle.as_view(), name="Detalle"),
    path(r'^nuevo$', views.PostCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.PostUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.PostDelate.as_view(), name='Delete'),




]