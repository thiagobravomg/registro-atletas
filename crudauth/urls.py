from django.urls import path
from .views import ListaAtletas, InfoAtleta, RegistrarAtleta, AlterarAtleta, RemoverAtleta, FazerLogin, RegistrarUsuario
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('lista/', ListaAtletas.as_view(), name='lista_atletas'),
    path('lista/<int:pk>', InfoAtleta.as_view(), name='info_atleta'),
    path('registrar/', RegistrarAtleta.as_view(), name='registrar_atleta'),
    path('alterar/<int:pk>', AlterarAtleta.as_view(), name='alterar_atleta'),
    path('remover/<int:pk>',RemoverAtleta.as_view(), name='remover_atleta'),
    path('login/',FazerLogin.as_view(), name='fazer_login'),
    path('logout/',LogoutView.as_view(next_page = 'fazer_login'), name='fazer_logout'),
    path('registrarusuario/',RegistrarUsuario.as_view(), name='registrar_usuario')
] 