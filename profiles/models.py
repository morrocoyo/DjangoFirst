from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from django.core.mail import send_mail

from .utilidades import code_generator
# Create your models here.
User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='is_following', blank=True)
#    following = models.ManyToManyField(User, related_name='following', blank=True)
    activation_key = models.CharField(max_length=120, blank=True, null=True)
    activated = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        if not self.activated:
            self.activation_key = code_generator()
            self.save()
            path_ = reverse('activate', kwargs={'code': self.activation_key})
            subject = 'Activación de cuenta'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = f'Active su cuenta aquí {path_}'
            recipient_list = [self.user.email]
            html_message = f'<p>Active su cuenta aquí {path_}</p>'
            print (html_message)
            # send_mail(
            #     subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
            sent_mail = False   #send_mail()
            return sent_mail



def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        default_user_profile = Profile.objects.get_or_create(user__id=1)[0]  #user_username,...
        default_user_profile.followers.add(instance)
        profile.followers.add(default_user_profile.user)
        profile.followers.add(2)

post_save.connect(post_save_user_receiver, sender=User)