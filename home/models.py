from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.TextField(max_length=120, null=True, blank=True )
    message = models.TextField(max_length=500)
    contact = models.TextField(max_length=12, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

