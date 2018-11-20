from django.db import models
from django.conf import settings
from ilan.models import Ilan

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def user_ilanlar(self):
        return Ilan.objects.filter(user=self.user)
        
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)