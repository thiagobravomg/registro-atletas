from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Atleta
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

class ListaAtletas(LoginRequiredMixin,ListView):
    model = Atleta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atletas'] = Atleta.objects.filter(user=self.request.user)
        busca_filtro = self.request.GET.get("area_busca")
        if busca_filtro:
            x = Atleta.objects.filter(user=self.request.user)
            context['atletas'] = x.filter(Q(equipe__icontains = busca_filtro)|Q(nome__icontains = busca_filtro))
        return context
    

class InfoAtleta(LoginRequiredMixin,DetailView):
    model = Atleta

class RegistrarAtleta(LoginRequiredMixin,CreateView):
    model = Atleta
    fields = ['nome','equipe','idade','graduacao','peso','genero']
    success_url = reverse_lazy('lista_atletas')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RegistrarAtleta,self).form_valid(form)

class AlterarAtleta(LoginRequiredMixin,UpdateView):
    model = Atleta
    fields = ['nome','equipe','idade','graduacao','peso','genero']
    success_url = reverse_lazy('lista_atletas')

class RemoverAtleta(LoginRequiredMixin,DeleteView):
    model = Atleta
    success_url = reverse_lazy('lista_atletas')

class FazerLogin(LoginView):
    template_name = 'crudauth/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self) -> str:
        return reverse_lazy('lista_atletas')

class RegistrarUsuario(FormView):
    form_class = UserCreationForm
    template_name = 'crudauth/user_form.html'
    success_url = reverse_lazy('fazer_login')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('lista_atletas')
        return super(RegistrarUsuario,self).get(*args, **kwargs)