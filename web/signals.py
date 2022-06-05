from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from web.models import Profile

@receiver(post_save,sender=User)
def create_profile_handler(sender,instance,created,**kwargs):
    if not created :
        return 
    profile = Profile.objects.create(user = instance)