import datetime

from django.db import models
from django.utils import timezone
        
class Client(models.Model):
    clients = [
        (0, ">_<"),
        (1, "O_O"),
        (2, ">_>"),
        (3, ";_;"),
    ]

    client_text = models.CharField(
        max_length = 3,
        choices = clients,
        default = 0,
    )
    
    def __str__(self):
        return self.client_text

    
class ProductArea(models.Model):
    areas = [
        (0, "Conquest"),
        (1, "War"),
        (2, "Famine"),
        (3, "Plague"),
    ]
    
    prod_area_text = models.CharField(
        max_length = 200,
        choices = areas,
        default = 0,
    )
    
    def __str__(self):
        return self.prod_area_text      
        
class Features(models.Model):
    title = models.CharField(max_length = 200)
    descript = models.CharField(max_length = 20000)
    client_type = models.ForeignKey('Client', on_delete=models.CASCADE)
    client_priority = models.IntegerField(default=0)
    target_date = models.CharField(max_length = 200)
    product_area = models.ForeignKey('ProductArea', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (("client_type", "client_priority"),)
    