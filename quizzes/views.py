from django.shortcuts import get_object_or_404, render

from .forms import AnswerForm
from .models import Question, Quiz


# Create your views here.
def quiz_list(request):

    quizzes = Quiz.objects.all()
    context = {
        'quizzes' : quizzes
    }
    return render(request,'quizzes/quiz_list.html',context=context)


def quiz_detail(request, pk):
    ...

def answer_question(request,pk):
    question = get_object_or_404(Question,pk=pk)
    answer_form = AnswerForm(initial={'question':question})


    context = {
        'answer_form':answer_form,
        'question':question
    }

    return render(request,'quizzes/answer_question.html', context=context)