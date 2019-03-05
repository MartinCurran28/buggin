from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=250, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='image')
    
    def __str__(self):
        return self.name
