import datetime
from django.db import models
from django.utils import timezone 

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField("date plublished")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >=timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0) #Variable contador.

    def __str__(self):
        return self.choice_text   