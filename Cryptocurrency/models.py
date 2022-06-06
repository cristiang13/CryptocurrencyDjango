from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    percent_change_24h=models.DecimalField(max_digits=10, decimal_places=2)
    favorite=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)