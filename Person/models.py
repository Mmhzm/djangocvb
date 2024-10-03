from django.db import models
from django.urls import reverse

# Create your models here.

class person(models.Model):
    name=models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    age=models.IntegerField()
    national_id=models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.national_id
