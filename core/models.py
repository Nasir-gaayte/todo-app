
from django.db import models
from django.contrib.auth.models import User
from helper.models import TrackerModel
from django.urls import reverse

# Create your models here.



class TodoModel(TrackerModel):
    title = models.CharField(max_length=225)
    description = models.TextField()
    is_completed = models.BooleanField(default= False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    



    def __str__(self):
        return self.title


    def get_absolute_url(self):
            
            return reverse('todo_detail', kwargs={'pk': self.pk})