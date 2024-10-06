from django.db import models

# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.CharField(max_length=100)
    book_id=models.CharField(max_length=2)

    def __str__(self):
        return self.book_id
