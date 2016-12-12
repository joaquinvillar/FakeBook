from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

app_name = 'fb'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^all/$', views.All.as_view(), name='all'),
    url(r'^add/(?P<pk>[0-9]+)/$', views.add_friend, name='add'),
    url(r'^register/$', views.register_login, name='register'),
    url(r'^register_out/$', views.register_logout, name='register_out'),
    url(r'^is_online/$', views.is_online, name='is_online'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^movie/(?P<pk>[0-9]+)/$', views.DetailViewMovie.as_view(), name='detailmovie'),
    # url(r'^cinema/(?P<pk>[0-9]+)/$', views.DetailViewCinema.as_view(), name='detailcinema'),
    # url(r'^sign/', views.sig_in, name='sign'),
    # url(r'^logout/', views.logout_view, name='logout'),
    # url(r'^upload/$', views.model_form_upload, name='upload'),
]