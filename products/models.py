from django.db import models

# Create your models here.




class Product(models.Model):
    '''
        manage the products
    '''
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=500)
    pricce = models.FloatField()
