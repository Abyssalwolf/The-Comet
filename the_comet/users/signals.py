from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomerUser, CustomerProfile

@receiver(post_save, sender=CustomerUser)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        CustomerProfile.objects.create(user=instance)