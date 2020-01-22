from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):
    
    STATUS = (
        ('fazendo', 'Fazendo'),
        ('feito', 'Feito'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=7,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Note(models.Model):
    description_text = models.CharField(max_length=200)
    fk_task = models.ForeignKey(Task, on_delete=models.CASCADE)   
    def __str__(self):
        return self.description_text