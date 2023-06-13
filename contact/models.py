from django.db import models

# Create your models here.
class ContactPerson(models.Model):
    name     = models.CharField(max_length=50)
    image    = models.ImageField(upload_to='contact-list')
    facebook = models.CharField(max_length=300)
    whatsapp = models.CharField(max_length=300)