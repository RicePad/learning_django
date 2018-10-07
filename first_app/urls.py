from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.show_form, name='show_form'),
    url(r'^$', views.index, name='index'),
]
