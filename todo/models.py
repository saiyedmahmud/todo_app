from operator import truediv
from pydoc import describe
from unicodedata import name
from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    choose = (('','Select One'),
            ('High','High'),
            ('Medium','Medium'),
            ('Low', 'Low'))
    priority = models.CharField(choices=choose, max_length=15)
    description = models.TextField(max_length=500)
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)