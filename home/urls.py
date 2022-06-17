''' URL Configuration for the home app '''

from django.urls import path
from . import views

# empty path to indicate the root url of the app
urlpatterns = [
    path('', views.index, name='home'),
]
