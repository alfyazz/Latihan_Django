from django.urls import path
from first_appalma import views

urlpatterns = [
    path('', views.index, name='index'),
]