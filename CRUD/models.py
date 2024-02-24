from django.db import models

# Create your models here.
class ToDo(models.Model):
    team_name=models.CharField(max_length=20)
    captain=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    t_mem=models.IntegerField()





