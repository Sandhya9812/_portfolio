from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('test-email/', views.send_test_email, name='test_email'),
]
