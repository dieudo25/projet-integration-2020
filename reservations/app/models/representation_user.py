from django.db import models
from django.urls import reverse


class RepresentationUser(models.Model):

    """ Representation_user model definition """
    user_id = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    representation_id = models.ForeignKey("Representation", on_delete=models.CASCADE)
    places = models.IntegerField()
    
    """ Representation_user meta definition """
    class Meta:
        verbose_name = "Representation_user"
        verbose_name_plural = "Representation_users"

    """ String Representation_user of Representation_user """
    def __str__(self):
        return f'({self.pk})'

    def get_absolute_url(self):
        return reverse("app:representation_user-detail", kwargs={"pk": self.pk})