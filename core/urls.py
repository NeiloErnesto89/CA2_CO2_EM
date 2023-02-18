from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('q1', views.q1, name='q1'),
]