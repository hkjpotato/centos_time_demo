from django.db import models
from ..feeder_models import Feeder
from ..node_models import D_Bus

class D_Generator(models.Model):
    id = models.AutoField(primary_key=True)
    feeder = models.ForeignKey(Feeder, related_name='d_generators')
    name = models.CharField(max_length=200)
    capacity = models.FloatField(null=True)
    cost = models.FloatField(null=True)

    #for gld
    gldIndex = models.IntegerField(null=True, default=0)
    object = models.CharField(max_length=50, default='generator')

    #foreign key
    parentLocation = models.ForeignKey(D_Bus, related_name='generators')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table='D_Generator'