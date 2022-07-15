from statistics import mode
from django.db import models
from requests import request
import datetime
from config.settings import BASE_DIR
from pathlib import Path
import os
# Create your models here.

def get_file_path(instance, filename):
    extension = filename.split('.')[-1]
    str_path = '/static/images/' + str(instance.user.id)+'/data/'
    layerPath = Path(str(BASE_DIR) + str_path)
    filename_start = filename.replace('.'+extension,'')

    filename = "%s.%s" % (filename_start, extension)
    return os.path.join(layerPath, filename)


class User(models.Model):
    WalletAddress = models.CharField(max_length=255, null=True, blank=True)
    plantName = models.CharField(max_length=200,null=True,blank=True)
    is_plant_name_is_active = models.BooleanField(default=True)
    week1 = models.BooleanField(default=False)
    week2 = models.BooleanField(default=True)
    week3 = models.BooleanField(default=True)
    week4 = models.BooleanField(default=True)
    weekPercentage = models.IntegerField(default=0);

    
    def __str__(self):
        return self.WalletAddress


class ImageMetaData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images', verbose_name=(u'File'))
    weekno = models.CharField(max_length=10, null=True, blank=True)
    lati= models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    long=models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    metadata_date=models.DateField(blank=True,null=True)
    present_date=models.DateField(default=datetime.date.today)
    ipfs_hash = models.CharField(max_length=200, null=True, blank=True)
    


    def __str__(self):
        return self.weekno
