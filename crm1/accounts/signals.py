from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.dispatch import receiver
from .models import Customer


@receiver(post_save, sender=User)
def customer_profile(sender,instance,created, **kwargs):
    if created:
        group=Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(user=instance,
                                name=instance.username
                                )
        print(instance,instance.username)


# @receiver(post_save, sender=User)
# def update_profile(sender, instance, created, **kwargs):
#     if created == False:
#         instance.profile.save()
#         print("profile updated for",instance)