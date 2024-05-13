from django.urls import path
from . import views

urlpatterns = [
    path('quizzes/', views.quiz_list_view, name='quiz_list'),
    path('quizzes/<pk>/', views.quiz_detail_view, name='quiz_detail'),
    path('quizzes/<pk>/take/', views.take_quiz_view, name='take_quiz'),
]