from django.db import models

# Create your models here.
class Employes(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    semester = models.CharField(max_length=20,null=True)
    batch = models.CharField(max_length=20,null=True)
    phone= models.IntegerField()
    address= models.TextField()

    def __str__(self):
        return self.name
    