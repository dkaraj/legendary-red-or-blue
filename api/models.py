# Create your models here
from django.db import models


class Property(models.Model):
    property_address = models.CharField(max_length=255,null=False)
    listing_price = models.FloatField(null=False)

    class Meta:
        db_table = 'property'
