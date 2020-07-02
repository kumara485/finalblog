from django.db.models.signals import post_save, pre_delete 
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import Profile

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('Profile Created')
post_save.connect(create_profile,sender=User)


def save_profile(sender, instance, **kwargs):
    instance.profile.save()
post_save.connect(create_profile,sender=User)
    