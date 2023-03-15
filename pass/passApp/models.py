from django.db import models

# Create your models here.


class Pass(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    travelpt = models.IntegerField()

    def __str__(self):
        return self.fname+self.lname+self.travelpt
