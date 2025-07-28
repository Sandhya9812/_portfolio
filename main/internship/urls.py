from django.urls import path
from .views import internship_list

urlpatterns = [
    path('internships/', internship_list, name='internship_list'),
]
