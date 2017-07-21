from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Question(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    added_at = models.DateTimeField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)


class Answer(models.Model):
    text = models.CharField(max_length=200)
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User)
