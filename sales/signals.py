from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from orders.models import Order
from sales.models import Sale

@receiver(pre_delete, sender=Sale)
def create_delete_change_order(sender, instance, **kwargs):
    obj = instance.order
    obj.active = False
    obj.save()

