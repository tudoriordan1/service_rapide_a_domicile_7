from django.db import models
from django.contrib.auth.models import User
from geopy.geocoders import Nominatim

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Service(models.Model):

    host = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete = models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True)
    address = models.TextField(null=True, blank = True)
    updated = models.DateTimeField(auto_now=True)
    montant = models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='base/files/images',default="base\files\images\Logo_SRAD.png")


    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete = models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


    def __str__(self):
        return f"{self.address}, {self.city}, {self.zip_code}"