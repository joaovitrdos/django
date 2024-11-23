from django.urls import path
from app_portifolio import views

urlpatterns = [
    #totas, view resposnavel, nome de referencia
    path('',views.home,name='home'),
    path('usuarios/',views.usuarios,name='listagem_usuario')
]
