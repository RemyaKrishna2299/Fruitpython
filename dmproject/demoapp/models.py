from django.db import models

# Create your models here.
class Fruit(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
class Person(models.Model):
    title=models.CharField(max_length=250)
    photo=models.ImageField(upload_to='pics')
    profile=models.TextField()
    def __str__(self):
        return self.name