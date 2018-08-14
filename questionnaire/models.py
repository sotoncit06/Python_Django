from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Questionnaire(models.Model):
    question=models.CharField(max_length=200)
    answar=models.CharField(max_length=100)

    def __str__(self):
        return self.question