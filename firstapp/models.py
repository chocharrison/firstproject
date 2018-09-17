from django.db import models


class Register(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=10)
    email=models.EmailField()
    
    def __str__(self):
        return self.first_name+'  -  '+self.last_name+'  -  '+self.email

# Create your models here.
