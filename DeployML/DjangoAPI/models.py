from django.db import models

# Create your models here.
class Surveyor(models.Model):
    STDE = models.FloatField(' Shaft drive-end temperature reading (degrees Celsius)')
    MTDE = models.FloatField('Motor drive-end temperature reading (degrees Celsius)')
    SUDEM = models.IntegerField('Shaft drive-end maximum decibel reading (decibels)')
    SUDEC = models.IntegerField('Shaft drive-end carpet decibel reading (decibels)')
    MVDEH = models.FloatField('Motor drive-end vertical velocity (metre per second)')
    MVDEV = models.FloatField('Motor drive-end horizontal velocity (metre per second)')
    MVDEA = models.FloatField('Motor drive-end axial velocity (metre per second)')
    SVDEH = models.FloatField('Shaft drive-end horizontal velocity (metre per second)')
    SVDEV = models.FloatField('Shaft drive-end vertical velocity (metre per second)')
    FD = models.IntegerField('feed capacity (kilogram)')

    def __str__(self):
        return self.STDE
