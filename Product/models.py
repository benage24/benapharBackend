from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=255,blank=True)
    quantity=models.IntegerField(default=0)
    unit=models.IntegerField(default=0)
    price=models.DecimalField(default=0.0,decimal_places=2,max_digits=10)
    exp_date=models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.name