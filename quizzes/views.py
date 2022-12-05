from django.contrib.auth.decorators import login_required
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

@login_required
def display_questions(request, pk):

    quiz = get_object_or_404(Quiz, pk=pk)
    # Create or grab ongoing testing for the given quiz
    testing,created = Testing.objects.get_or_create(user = request.user, quiz = quiz, finished = False)
    context = {
        'total':quiz.total_questions,
        'current': testing.answered_questions.count() + 1
    }
    # Remove answered questions from the quiz's questions set
    remaining_questions = quiz.questions.all().difference(testing.answered_questions.all())

    if remaining_questions.exists():
        current_question = remaining_questions.first()
        answer_form = AnswerForm(initial={'question':current_question})    
        
        if request.method == 'POST':

            # If request is post, feed answer form and save answer if it's valid then redirect to this same view
            answer_form = AnswerForm(request.POST,initial={'question':current_question})
            if answer_form.is_valid():
                answer = answer_form.save(commit=False)
                answer.user = request.user
                answer.question = current_question
                answer.save()
                answer_form.save_m2m()
                testing.answered_questions.add(current_question)
                testing.answers.add(answer)
                testing.save()
                return redirect(quiz.get_absolute_url())
        context['answer_form'] = answer_form
        context['question'] = current_question
        return render(request,'quizzes/display_questions.html', context=context)

    else:
        # If no question remaining then redirect to
        testing.finished = True
        testing.save()
        return redirect(reverse('quizzes:results'))
        
@login_required
def results(request):
    testings = Testing.objects.filter(user = request.user)

    return render(request, 'quizzes/results.html', context={'testings': testings})