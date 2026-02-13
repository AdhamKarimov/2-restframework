from django.db import models

# Create your models here.

class User(models.Model):
    ism = models.CharField(max_length = 100)
    familya =models.CharField(max_length = 100)
    otasinging_ismi=models.CharField(max_length = 100)
    tugilgan_kun = models.DateField()
    yashash_joyi = models.TextField()
    telefon_raqami = models.CharField(max_length = 13)
    email = models.EmailField()

    def __str__(self):
        return self.ism