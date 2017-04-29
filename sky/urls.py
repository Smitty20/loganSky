from django.conf.urls import url

from . import views

app_name = 'sky'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^purchase/$', views.purchase, name='purchase'),
    url(r'^submit/$', views.submit, name='submit'),
]