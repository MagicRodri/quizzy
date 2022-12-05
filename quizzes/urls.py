from django.urls import path

from .views import answer_question, display_questions, quiz_list

app_name = 'quizzes'
urlpatterns = [
    path('',quiz_list,name='quiz-list'),
    path('quiz/<int:pk>/',display_questions, name='display-question'),
    path('<int:pk>/',answer_question,name='answer-question')
]
