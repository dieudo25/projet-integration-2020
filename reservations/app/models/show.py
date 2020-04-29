from django.db import models
from django.utils import timezone
from django.urls import reverse

class Show(models.Model):

    # Show model definition 
    slug = models.SlugField(max_length=60, unique=True)
    title = models.CharField(max_length=255)
    poster_url = models.URLField(max_length=200, null=True)
    bookable = models.BooleanField()
    price = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now, null=True)

    # Show meta definition 
    class Meta:
        verbose_name = "Show"
        verbose_name_plural = "Shows"

    # String representation of Show 
    def __str__(self):
        return f'({self.pk}) {self.title}'

    def get_absolute_url(self):
        return reverse("Show_detail", kwargs={"pk": self.pk})