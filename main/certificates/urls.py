from django.urls import path
from . import views

urlpatterns = [
     path('', views.certificates_list, name='certificates'),
]
