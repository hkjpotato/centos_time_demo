from django.db import models
from ..feeder_models import Feeder
from ..node_models import D_Bus

class D_Capacitor(models.Model):
    id = models.AutoField(primary_key=True)
    feeder = models.ForeignKey(Feeder, related_name='d_capacitors')
    name = models.CharField(max_length=200)
    phases = models.CharField(max_length=50, null=True)
    control = models.CharField(max_length=50)
    capacitor_A = models.CharField(max_length=50)
    capacitor_B = models.CharField(max_length=50)
    capacitor_C = models.CharField(max_length=50)
    time_delay = models.FloatField(null=True)
    switchA = models.CharField(max_length=10, null=True)
    switchB = models.CharField(max_length=10, null=True)
    switchC = models.CharField(max_length=10, null=True)
    control_level = models.CharField(max_length=20, null=True)
    phases_connected = models.CharField(max_length=50, null=True)
    dwell_time = models.FloatField(null=True)
    pt_phase = models.CharField(max_length=20, null=True)

    #should be complex
    nominal_voltage = models.CharField(max_length=50, null=True)
    voltage_set_high = models.CharField(max_length=50, null=True)
    voltage_set_low = models.CharField(max_length=50, null=True)

    #for gld
    gldIndex = models.IntegerField(null=True, default=0)
    object = models.CharField(max_length=50, default='capacitor')

    #foreign key
    parentLocation = models.ForeignKey(D_Bus, related_name='capacitors')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table='D_Capacitor'