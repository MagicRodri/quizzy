from django.contrib import admin

from .forms import AdminOptionForm, AdminQuestionForm, AnswerForm, OptionInlineFormSet
from .models import Answer, Option, Question, Quiz, Testing

# Register your models here.



class OptionInline(admin.TabularInline):
    
    form = AdminOptionForm
    formset = OptionInlineFormSet
    model = Option
    extra = 1

class QuestionAdmin(admin.ModelAdmin):

    form = AdminQuestionForm
    inlines = [OptionInline]

class QuestionInline(admin.TabularInline):

    model = Question
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Question,QuestionAdmin)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(Option)
admin.site.register(Answer)
admin.site.register(Testing)