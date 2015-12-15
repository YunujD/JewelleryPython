from django.db import models


# Create your models here.
class UserDetail(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=50)
    added_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name