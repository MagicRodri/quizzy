from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q
from django.urls import reverse

from core.models import BaseModel

# Create your models here.
User = get_user_model()

class Quiz(BaseModel):

    name = models.CharField(max_length=64)
    subject = models.CharField(max_length=128)
    pass_score = models.FloatField(
        default=100,
        validators=[
            MinValueValidator(0, message='Pass score must be greater than 0'),
            MaxValueValidator(100,message='Pass score must be less than 100')
        ])
    
                                 

    class Meta:
        verbose_name_plural = 'Quizzes'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("quizzes:display-question", kwargs={"pk": self.pk})

    @property
    def total_questions(self):
        return self.questions.count()
    

class Question(BaseModel):


    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE) 
    content = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.content

class Option(BaseModel):


    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.content

class Answer(BaseModel):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    options = models.ManyToManyField(
        Option,
    )

    @property
    def is_correct(self):
        correct_answered = self.options.filter(correct = True).count()
        correct_set = self.question.options.filter( correct = True).count()
        return (correct_answered == correct_set) and (correct_set != self.question.options.count())

class Testing(BaseModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answered_questions = models.ManyToManyField(Question, blank=True)
    answers = models.ManyToManyField(Answer, blank=True)
    finished = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Quiz:{self.quiz} User:{self.user} time:{self.created_at.ctime()}'
    
    @property
    def total_correct(self):
        
        count = 0
        for ans in self.answers.all():
            if ans.is_correct:
                count+=1
        return count

    @property
    def total_questions(self):
        return self.quiz.total_questions

    @property
    def score(self):
        return '%.2f' % ((self.total_correct/self.total_questions) * 100)

    @property
    def passed(self):
        return float(self.score) >= self.quiz.pass_score

    # def result(self):
    #     correct = 0
    #     incorrect = 0
    #     quiz_questions = self.quiz.questions.all()
    #     for answer in Answer.objects.filter(user = self.user, quiz = )