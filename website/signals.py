from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

from .models import Myprofile,Project,Technologies,Services

@receiver(post_delete, sender=Myprofile)
def delete_image_on_model_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(post_delete, sender=Project)
def delete_image_on_model_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(post_delete, sender=Technologies)
def delete_image_on_model_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(post_delete, sender=Services)
def delete_image_on_model_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)