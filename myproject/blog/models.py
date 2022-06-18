from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.

# Create a new model in the blog app called Post. It should have the following fields:


#Title : A string of maxlength 200, use Django’s models.CharField
#Text : Any amount of text, use Django’s TextField
#Author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.
#Created_date : A date-time column, use Django’s models.DateTimeField. 
#Published_date : A date-time column, use Django’s models.DateTimeField. 

user = get_user_model()
class Post(models.Model):
    tittle = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(user, on_delete= models.CASCADE)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.tittle