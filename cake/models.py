from django.db import models

# Create your models here.
#class DataDiscription:
#    name : str
#    desc : str
#    #img = models.ImageField(upload_to='pics')
#    price :int

class DataDiscription(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    old_price = models.IntegerField()