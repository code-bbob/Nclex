from django.db import models
# Create your models here.
class Question(models.Model):
    ques= models.CharField(max_length=1000)
    option1= models.TextField(max_length=100)
    option2= models.TextField(max_length=100)
    option3= models.TextField(max_length=100)
    option4= models.TextField(max_length=100)
    ans= models.TextField(max_length=100)

    def __str__(self):
        return self.ques

