from django.db import models
from django.contrib.auth import get_user_model

class Person(models.Model):
    profile = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    bio = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
