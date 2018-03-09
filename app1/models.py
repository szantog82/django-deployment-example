from django.contrib.auth.models import User

from django.db import models


# Create your models here.
class Clients(models.Model):
    FIRST_NAME = models.CharField(max_length=254)
    LAST_NAME = models.CharField(max_length=254)
    E_MAIL = models.CharField(max_length=254)
    
    def __str__(self):
        return "name: {} {}, e-mail: {}".format(self.FIRST_NAME, self.LAST_NAME, self.E_MAIL)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    
    portfolio_site = models.URLField(blank=True)

    def __str__(self):
        return self.user.username