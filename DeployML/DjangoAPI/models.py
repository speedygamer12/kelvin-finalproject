from django.db import models

# Create your models here.
class Surveyor(models.Model):
    STDE = models.FloatField('Shaft Drive-end Temperature Reading')
    MTDE = models.FloatField('Motor Drive-end Temperature Reading')
    SUDEM = models.IntegerField('Shaft drive-end maximum decibel reading')
    SUDEC = models.IntegerField('Shaft drive-end carpet decibel reading')
    MVDEH = models.FloatField('Motor drive-end vertical velocity')
    MVDEV = models.FloatField('Motor drive-end horizontal velocity')
    MVDEA = models.FloatField('Motor drive-end axial velocity')
    SVDEH = models.FloatField('Shaft drive-end horizontal velocity')
    SVDEV = models.FloatField('Shaft drive-end vertical velocity')
    FD = models.IntegerField('feed capacity')

    def __str__(self):
        return self.STDE
