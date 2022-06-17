from django.urls import path
from . import views


urlpatterns = [
    path('', views.chatrooms, name='chatrooms'),

]
