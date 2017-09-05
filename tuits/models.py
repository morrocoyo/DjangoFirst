from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.db.models import Q
from .validators import validate_category
from .utilidades import unique_slug_generator
# from django.core.urlresolvers import reverse    #dpara django 1.11
from django.urls import reverse

# Create your models here.


User = settings.AUTH_USER_MODEL


class TuitLocationQuerySet(models.query.QuerySet):
    def search(self, query):
        if query:
            query=query.strip()
            return self.filter(
                    Q(name__icontains=query) |
                    Q(location__icontains=query) |
                    Q(category__icontains=query) |
                    Q(item__name__icontains=query) |
                    Q(item__contents__icontains=query)
                    ).distinct()
        return self


class TuitLocationManager(models.Manager):
    def get_queryset(self):
        return TuitLocationQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class TuitLocation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Django Models Unleash JOINCFE.com
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)
    # my_date_field   = models.DateField(auto_now=False, auto_now_add=True)

    objects = TuitLocationManager()  # add Models.objects.all()

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

    def get_absolute_url(self):
        #        return f'/tuits/{self.slug}'
        return reverse('tuits:detail', kwargs={'slug': self.slug})


def tl_pre_save_receiver(sender, instance, *args, **kwargs):
    print("saving...")
    print(instance.timestamp)
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# def tl_post_save_receiver(sender, instance,  created, *args, **kwargs):
#    print("saved")
#    print(instance.timestamp)


pre_save.connect(tl_pre_save_receiver, sender=TuitLocation)

# post_save.connect(tl_post_save_receiver, sender=TuitLocation)
