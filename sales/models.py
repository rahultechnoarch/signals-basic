from django.db import models
from django.db.models.deletion import CASCADE
from orders.models import Order
# Create your models here.

class Sales(models.Model):
    order = models.ForeignKey(Order, on_delete=CASCADE)
    amount = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self)
