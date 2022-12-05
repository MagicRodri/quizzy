from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q

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

class Question(BaseModel):


    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE) 
    content = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.content

class Option(BaseModel):


    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.content

class Answer(BaseModel):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    options = models.ManyToManyField(
        Option,
        blank=True
    )