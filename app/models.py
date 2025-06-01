from django.db import models

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)
    discount = models.IntegerField()
    active = models.BooleanField()

    def __str__(self):
        return self.code