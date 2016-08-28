from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.HomeListView.as_view(), name = 'home'),
    url(r'^create/$', views.create_function, name = 'createFunction'),
    url(r'^add/$', views.add_function, name = 'addFunction'),
    url(r'^list/(?P<pk>\d+)/$', views.FunctionListView.as_view(), name = 'listFunction'),
    url(r'^detail/(?P<pk>\d+)/$', views.FunctionDetailView.as_view(), name = 'functionDetails'),
]
