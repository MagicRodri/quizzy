from django.urls import path

from .views import display_questions, quiz_list, results

app_name = 'quizzes'
urlpatterns = [
    path('',quiz_list,name='quiz-list'),
    path('quiz/<int:pk>/',display_questions, name='display-question'),
    path('quiz/results/',results,name='results')
]
