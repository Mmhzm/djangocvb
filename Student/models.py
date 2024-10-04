from django.db import models

# Create your models here.
class studnet(models.Model):
    name=models.CharField(max_length=20)
    family=models.CharField(max_length=20)
    age=models.IntegerField()
    student_id=models.CharField(max_length=8)
    national_id=models.CharField(max_length=10)


    def __str__(self):
        return self.student_id
    