from django.db import models
from django_currentuser.middleware import get_current_authenticated_user
# Create your models here.
class Records(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    country = models.CharField(max_length=50)
    dol = models.DateField()
    last_seen = models.TextField(max_length=300)
    dob = models.DateField()
    mobileno = models.CharField(max_length=10)
    image = models.ImageField(upload_to = 'images')
    current_user = models.CharField(max_length=30, default=get_current_authenticated_user, blank=True, null=True)
    status = models.BooleanField()

    def __str__(self):
        return self.name