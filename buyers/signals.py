from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from  django.contrib.auth.models import User
from buyers.models import Buyer

@receiver(post_save, sender=User)
def post_save_create_user(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance', instance)
    print('created', created)
    if created:
        Buyer.objects.create(user=instance)