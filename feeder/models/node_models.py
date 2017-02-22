from django.db import models
from .feeder_models import Feeder

class D_Bus(models.Model):
    id = models.AutoField(primary_key=True)
    feeder = models.ForeignKey(Feeder, related_name='d_buses')
    name = models.CharField(max_length=200)
    phases = models.CharField(max_length=50, null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    busType = models.CharField(max_length=20, null = True)

    #should be complex
    voltA = models.CharField(max_length=50, null=True)
    voltB = models.CharField(max_length=50, null=True)
    voltC = models.CharField(max_length=50, null=True)
    nominalVolt = models.CharField(max_length=50, null=True)
    
    #for gld
    gldIndex = models.IntegerField(null=True, default=0)
    object = models.CharField(max_length=50, default='node')

    #foreign key
    parentLocation = models.ForeignKey("D_Bus", related_name='child_bus', null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table='D_Bus'
