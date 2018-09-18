

from django.db import models
from django.contrib.auth.models import User

class MarklynUser(models.Model):
    marklyn_user = models.OneToOneField(User, on_delete = models.CASCADE)
        #if user created from registration was deleted from AA section on admin panel, this marklyn user is also deleted
        #if set_null and user is deleted from AA section, the def __str__ will have problem display because marky_user is nonobject now
    # user_pic = models.ImageField(upload_to = 'marklyn_pics', blank = True)

    def __str__(self):
        return self.marklyn_user.username
# Create your models here.
