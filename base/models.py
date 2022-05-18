from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = category = models.ForeignKey(User, on_delete = models.SET_NULL, null= True)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null= True)
    name = models.CharField(max_length=200)
    payout = models.CharField(max_length = 200, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    updated =  models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self):
        return self.name



class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    body = models.TextField()
    updated =  models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.body[0:50]

