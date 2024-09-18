from django.db import models
import datetime


# Create your models here.
from django.db import models
from django.utils import timezone


"""
    Each question has a question and a publication date.
    It will be associated with a choice object.
"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text
"""
    Each choice has a choice text and a vote tally
    It will be associated with a question object.
"""
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text