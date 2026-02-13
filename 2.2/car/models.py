from django.db import models

# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rangi = models.CharField(max_length=10)
    yoqilgi_turi = models.CharField(max_length=20)
    turi = models.CharField(max_length=20)
    diska_turi = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.model
