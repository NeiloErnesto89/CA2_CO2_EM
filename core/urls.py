from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('q1', views.q1, name='q1'),
    path('q2', views.q1, name='q2'),
    path('q3', views.q1, name='q3'),
    path('q4', views.q1, name='q4'),
    path('q5', views.q1, name='q5'),
    path('q6', views.q1, name='q6'),
    path('q7', views.q1, name='q7'),
]