from django.db.models.signals import pre_save, post_save, m2m_changed
from django.dispatch import receiver
from  django.contrib.auth.models import User
from cars.models import Car
from buyers.models import Buyer
from orders.models import Order
from sales.models import Sales

