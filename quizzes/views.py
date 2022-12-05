from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import AnswerForm
from .models import Question, Quiz, Testing


# Create your views here.
def quiz_list(request):

    quizzes = Quiz.objects.all()
    context = {
        'quizzes' : quizzes
    }
    return render(request,'quizzes/quiz_list.html',context=context)


def display_questions(request, pk):

    quiz = get_object_or_404(Quiz, pk=pk)
    testing,created = Testing.objects.get_or_create(user = request.user, quiz = quiz)
    context = {}
    remaining_questions = quiz.questions.all().difference(testing.answered_questions.all())
    print('r',remaining_questions)
    if remaining_questions.exists():
        current_question = remaining_questions.first()
        answer_form = AnswerForm(initial={'question':current_question})    
        if request.method == 'POST':
            answer_form = AnswerForm(request.POST,initial={'question':current_question})
            if answer_form.is_valid():
                answer = answer_form.save(commit=False)
                answer.user = request.user
                answer.question = current_question
                answer.save()
                answer_form.save_m2m()
                print('a:',answer.is_correct)
                testing.answered_questions.add(current_question)
                testing.save()
                return redirect(quiz.get_absolute_url())
        context['answer_form'] = answer_form
        context['question'] = current_question
        return render(request,'quizzes/answer_question.html', context=context)

    else:
        return redirect(reverse('quizzes:quiz-list'))

def answer_question(request,pk):
    question = get_object_or_404(Question,pk=pk)
    answer_form = AnswerForm(initial={'question':question})


    context = {
        'answer_form':answer_form,
        'question':question
    }

    return render(request,'quizzes/answer_question.html', context=context)