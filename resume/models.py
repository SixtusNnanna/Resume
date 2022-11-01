from email.policy import default
from django.db import models


class Expertise(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()


    def __str__(self):
        return self.title

        
class Education(models.Model):
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)
    qulification = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    school = models.CharField(max_length=200)

    def __str__(self):
        return self.qulification

class Skills(models.Model):
    title = models.CharField(max_length=100)
    level = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Language(models.Model):
    title = models.CharField(max_length=100)
    level = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    


    
class Profile(models.Model):
    dp = models.ImageField(upload_to='pic/')
    title = models.CharField(max_length=100, default="Chemical Engineer/ Fullstack Developer")
    about = models.TextField(default= 'sixtus')