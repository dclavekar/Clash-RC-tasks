from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phoneno=models.IntegerField()
    gender=models.CharField(max_length=100)


    def __str__(self):
        return f'{self.user.username}'


