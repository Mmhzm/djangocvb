from django.db import models

# Create your models here.

class person(models.Model):
    name=models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    age=models.IntegerField()
    national_id=models.CharField(max_length=10)


    def __str__(self):
        return self.national_id
