from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/',default='default_pic.png')
    country = models.CharField(default='',max_length=100)
    state = models.CharField(default='',max_length=100)
    city = models.CharField(default='',max_length=100)
    fullAddress = models.CharField(default='',max_length=100)
    pin = models.CharField(default='',max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()