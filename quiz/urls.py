from django.urls import path
from .views import quiz_home, quiz_view

urlpatterns = [
    path('', quiz_home),
    path('quiz_view/<int:quiz_id>/',quiz_view, name='quiz_view')
    
]
