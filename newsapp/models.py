from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name

class user(models.Model):
    name= models.CharField(max_length=70)
    email= models.EmailField(max_length=100)
    message= models.CharField(max_length=100)

class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article_url = models.URLField()
    count = models.IntegerField(default=0)


# class User(models.Model):
#     Username= models.CharField(max_length=30)
#     email =models.EmailField(max_length=100)
#     password =models.CharField(max_length=50)
 

# class signin(AbstractBaseUser):
#     username= models.CharField(max_length=30)
#     email =models.EmailField(max_length=100)
#     password =models.CharField(max_length=50)
#     objects =  UserManager()