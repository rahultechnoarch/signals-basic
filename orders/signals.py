from django.db.models.signals import pre_save, post_save, m2m_changed
from django.dispatch import receiver
from  django.contrib.auth.models import User
from orders.models import Order
from sales.models import Sale

@receiver(m2m_changed, sender=Order.cars.through)
def m2m_changed_cars_order(sender, instance, action,**kwargs):
    total = 0
    total_price = 0
    if action =='post_add' or action == 'post_remove':
        for car in instance.cars.all():
            total += 1
            total_price += car.price
        instance.total = total
        instance.total_price = total_price
        instance.save()

@receiver(post_save, sender=Order)
def post_save_create_or_update_sale(sender, instance, created, **kwargs):
    # Using 2 varialbes but the second is not used now (_)
    obj, _ = Sale.objects.get_or_create(order=instance)
    obj.amount = instance.total_price
    obj.save()