from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import UserProfile,Account


@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance,
                                   profile_picture='media/profile/avatar.png'
                                  )


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.edit_profile.save()
