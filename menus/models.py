from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.urls import reverse

from tuits.models import TuitLocation


# Create your models here.

class Item(models.Model):
    # associations
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(TuitLocation, on_delete=models.CASCADE)
    # real item stuff
    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='Separe cada ingrediente por coma')
    excludes = models.TextField(blank=True, null=True, help_text='Separe cada ingrediente por coma')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #        return f'/tuits/{self.slug}'
        # return reverse('menus:create', kwargs={'create': 'create'})
        return reverse('menus:detail', kwargs={'pk': self.pk})

        # return reverse({'menus:detail','menus:create'}, kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_contents(self):
        return self.contents.split(',')
    def get_excludes(self):
        return self.excludes.split(',')
