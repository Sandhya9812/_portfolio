from django.urls import path
from . import views

urlpatterns = [
    # Your other URLs...
    path('ai/', views.ai_assistant, name='ai_assistant'),
    path('save-conversation/', views.save_conversation, name='save_conversation'),
    

]
