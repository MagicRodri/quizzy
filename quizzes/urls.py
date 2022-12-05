from django.urls import path

from .views import answer_question, quiz_list

app_name = 'quizzes'
urlpatterns = [
    path('',quiz_list,name='quiz-list'),
    path('<int:pk>/',answer_question,name='answer-question')
]
