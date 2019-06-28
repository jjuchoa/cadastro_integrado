from django.urls import path, include

from django.contrib import admin

from pais.views import PaisListView, PaisCreateView, PaisUpdateView, PaisDeleteView
from estado.views import EstadoListView, EstadoCreateView, EstadoUpdateView, EstadoDeleteView
from cidade.views import CidadeListView, CidadeCreateView, CidadeUpdateView, CidadeDeleteView
from bairro.views import BairroListView, BairroCreateView, BairroUpdateView, BairroDeleteView
from tipo_logradouro.views import TipoLogradouroListView, TipoLogradouroCreateView,\
    TipoLogradouroUpdateView, TipoLogradouroDeleteView
from nome_logradouro.views import NomeLogradouroListView, NomeLogradouroCreateView,\
    NomeLogradouroUpdateView, NomeLogradouroDeleteView
from logradouro.views import LogradouroListView, LogradouroCreateView, LogradouroUpdateView, LogradouroDeleteView
from endereco.views import EnderecooListView, EnderecoCreateView, EnderecoUpdateView, EnderecoDeleteView
from autenticacao.views import AuthUserListView, AuthUserCreateView, AuthUserUpdateView, AuthUserDeleteView, HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('', HomeView.as_view(), name='home'),

    path('paislist/', PaisListView.as_view(), name='pais_list'),
    path('paisadd/', PaisCreateView.as_view(), name='pais_add'),
    path('<int:pk>/paisedit/', PaisUpdateView.as_view(), name='pais_edit'),
    path('<int:pk>/paisdelete/', PaisDeleteView.as_view(), name='pais_delete'),

    path('estadolist/', EstadoListView.as_view(), name='estado_list'),
    path('estadoadd/', EstadoCreateView.as_view(), name='estado_add'),
    path('<int:pk>/estadoedit/', EstadoUpdateView.as_view(), name='estado_edit'),
    path('<int:pk>/estadodelete/', EstadoDeleteView.as_view(), name='estado_delete'),

    path('cidadelist/', CidadeListView.as_view(), name='cidade_list'),
    path('cidadeadd/', CidadeCreateView.as_view(), name='cidade_add'),
    path('<int:pk>/cidadeedit/', CidadeUpdateView.as_view(), name='cidade_edit'),
    path('<int:pk>/cidadedelete/', CidadeDeleteView.as_view(), name='cidade_delete'),

    path('bairrolist/', BairroListView.as_view(), name='bairro_list'),
    path('bairroadd/', BairroCreateView.as_view(), name='bairro_add'),
    path('<int:pk>/bairroedit/', BairroUpdateView.as_view(), name='bairro_edit'),
    path('<int:pk>/bairrodelete/', BairroDeleteView.as_view(), name='bairro_delete'),

    path('tipologradourolist/', TipoLogradouroListView.as_view(), name='tipologradouro_list'),
    path('tipologradouroadd/', TipoLogradouroCreateView.as_view(), name='tipologradouro_add'),
    path('<int:pk>/tipologradouroedit/', TipoLogradouroUpdateView.as_view(), name='tipologradouro_edit'),
    path('<int:pk>/tipologradourodelete/', TipoLogradouroDeleteView.as_view(), name='tipologradouro_delete'),

    path('nomelogradourolist/', NomeLogradouroListView.as_view(), name='nomelogradouro_list'),
    path('nomelogradouroadd/', NomeLogradouroCreateView.as_view(), name='nomelogradouro_add'),
    path('<int:pk>/nomelogradouroedit/', NomeLogradouroUpdateView.as_view(), name='nomelogradouro_edit'),
    path('<int:pk>/nomelogradourodelete/', NomeLogradouroDeleteView.as_view(), name='nomelogradouro_delete'),

    path('logradourolist/', LogradouroListView.as_view(), name='logradouro_list'),
    path('logradouroadd/', LogradouroCreateView.as_view(), name='logradouro_add'),
    path('<int:pk>/logradouroedit/', LogradouroUpdateView.as_view(), name='logradouro_edit'),
    path('<int:pk>/logradourodelete/', LogradouroDeleteView.as_view(), name='logradouro_delete'),

    path('enderecolist/', EnderecooListView.as_view(), name='endereco_list'),
    path('enderecoadd/', EnderecoCreateView.as_view(), name='endereco_add'),
    path('<int:pk>/enderecoedit/', EnderecoUpdateView.as_view(), name='endereco_edit'),
    path('<int:pk>/enderecodelete/', EnderecoDeleteView.as_view(), name='endereco_delete'),

    path('userlist/', AuthUserListView.as_view(), name='user_list'),
    path('useradd/', AuthUserCreateView.as_view(), name='user_add'),
    path('<int:pk>/useredit/', AuthUserUpdateView.as_view(), name='user_edit'),
    path('<int:pk>/userdelete/', AuthUserDeleteView.as_view(), name='user_delete'),

]
