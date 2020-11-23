from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
   

    def __str__(self):
        return 'Message from ' + self.author + ' - ' + self.title 