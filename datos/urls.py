from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('usuario/', views.lista_usuarios, name='lista_usuario'),
    path('productos/', views.productos_en_stock, name='lista_productos')
  
]

