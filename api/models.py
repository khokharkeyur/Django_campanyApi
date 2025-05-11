from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    about = models.TextField()
    type = models.CharField(max_length=50, choices=(('IT', 'IT'), ('Finance', 'Finance'), ('Healthcare', 'Healthcare')))
    add_date = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.name
