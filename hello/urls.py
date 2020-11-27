from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Abdo', views.Abdo, name='Abdo'),
    path('<str:name>', views.greet, name="greet"),
]
