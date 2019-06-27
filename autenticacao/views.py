from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autenticacao.models import AuthUser


class AuthUserListView(ListView):
    model = AuthUser
    context_object_name = 'user'


class AuthUserCreateView(CreateView):
    model = AuthUser
    fields = ('password', 'last_login', 'is_superuser', 'username', 'first_name', 'email', 'is_staff',
              'is_active', 'date_joined', 'last_name')
    success_url = reverse_lazy('user_list')


class AuthUserUpdateView(UpdateView):
    model = AuthUser
    fields = ('password', 'last_login', 'is_superuser', 'username', 'first_name', 'email', 'is_staff',
              'is_active', 'date_joined', 'last_name')
    template_name = 'autenticacao/authuser_update_form.html'
    success_url = reverse_lazy('user_list')


class AuthUserDeleteView(DeleteView):
    model = AuthUser
    template_name = 'autenticacao/authuser_delete_form.html'
    success_url = reverse_lazy('user_list')
