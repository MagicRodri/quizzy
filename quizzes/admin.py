from django.contrib import admin

from .forms import AdminAnswerForm, AdminQuestionForm, AnswerInlineFormSet
from .models import Answer, Question, Quiz

# Register your models here.



class AnswerInline(admin.TabularInline):
    
    form = AdminAnswerForm
    formset = AnswerInlineFormSet
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):

    form = AdminQuestionForm
    inlines = [AnswerInline]

class QuestionInline(admin.TabularInline):

    model = Question
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Question,QuestionAdmin)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(Answer)