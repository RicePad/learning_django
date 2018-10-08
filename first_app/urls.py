from django.conf.urls import url
from first_app import views

app_name = "firstapp"

urlpatterns = [
    url(r'^$', views.show_form, name='show_form'),
    url(r'^index/$', views.index, name='index'),
    url(r'^form/$', views.show_form, name='show_form'),
]
