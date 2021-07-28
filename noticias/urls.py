from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('noticias/g1/', views.exibe_noticia_g1, name='noticias_g1'),
    path('noticias/bbc/', views.exibe_noticia_bbc, name='noticias_bbc'),
    path('ofertas/', views.exibe_ofertas, name='ofertas'),
]
