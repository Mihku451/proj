from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_exercise', views.create_exercise, name='create_exercise'),


    path('register', views.register, name='register'),
    path('login', views.login, name="login")

]
