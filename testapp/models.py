from django.db import models

# Create your models here.

class Project_model(models.Model):

    title=models.CharField(max_length=50)
    desc=models.TextField()
   
class userpro(models.Model):

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)