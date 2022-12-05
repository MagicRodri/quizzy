
from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, SignUpForm

# Create your views here.

User = get_user_model()

def login_view(request):

    form = LoginForm(request)
    message = ""
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect(reverse('quizzes:quiz-list'))

        else:
            message = "Login failed"
            
    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'accounts/login.html',context = context)


def logout_view(request):

    if request.method == 'POST':
        logout(request)
        return redirect(reverse('accounts:login'))

    return render(request,'accounts/logout.html',context={})


def signup_view(request):

    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect(reverse('quizzes:quiz-list'))

    return render(request,'accounts/signup.html',context={'form':form})
