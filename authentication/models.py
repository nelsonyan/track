

from django.db import models
from django.contrib.auth.models import User

class MarklynUser(models.Model):
    marklyn_user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.marklyn_user.username
# Create your models here.
