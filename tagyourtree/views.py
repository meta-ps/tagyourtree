from django.shortcuts import render,redirect
from tagyourtree.models import *
from API_KEYS.keys import keys
from pathlib import Path
from utility.nftstorage import NftStorage
import json
import shutil
from pathlib2 import Path as Path2_
import requests
import exifread

base_uri = "ipfs://"
NFTSTORAGE_API_KEY = keys['NFTSTORAGE']
PINATA_JWT = keys['PINATA']

img_file_list = [] 

# Create your views here.
def Home(request):
    return render(request,'home.html')

def Login(request):
    request.session['WalletAddress'] = "xxx"
    if request.POST:
        WalletAddress = request.POST.get('WalletAddress')
        request.session['WalletAddress'] = WalletAddress
        obj = User.objects.get_or_create(WalletAddress=WalletAddress)


        return redirect('userpage')
    else:
        return redirect('home')



def UserPage(request):
    WalletAddress = request.session['WalletAddress']
    user = User.objects.get(WalletAddress=WalletAddress)

    
    context=dict()
    context['user']=user

    return render(request,'userpage.html',context)


def addPlantName(request):
    WalletAddress = request.session['WalletAddress']
    plantname=request.POST.get('plantname')
    
    user = User.objects.filter(WalletAddress=WalletAddress).update(plantName=plantname,is_plant_name_is_active=False)

    return redirect('userpage')


def addImageAndExtract(request,weekno):
    WalletAddress = request.session['WalletAddress']
    user = User.objects.get(WalletAddress=WalletAddress)

    file = request.FILES.getlist('Aimage')
    file=file[0]

    print(type(weekno))
    print(weekno)
    

    ##save
    ImageMetaData.objects.create(user=user,image=file,weekno=weekno  )

    ##fetch meta data from image
    fetchMetaDataAndSave(request,weekno)

    #validate
    validatePlantData(request,weekno)


    ##upload to IPFS
    


    
   

 




    return redirect('userpage')

def validatePlantData(request,weekno):
    WalletAddress = request.session['WalletAddress']
    user = User.objects.filter(WalletAddress=WalletAddress)
    print('ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    weekno=int(weekno)
    if weekno==1:
        user.update(week1=True,week2=False)
    elif weekno ==2:
        user.update(week2=True,week3=False)
    elif weekno ==3:
        user.update(week3=True,week4=False)
        user.week3=True
        user.week4=False
    else:
        user.update(week4=True)


    #validate previous coordinate data





def fetchMetaDataAndSave(request,weekno):
    WalletAddress = request.session['WalletAddress']
    user = User.objects.get(WalletAddress=WalletAddress)


    xx=ImageMetaData.objects.get(user=user)
    xy=ImageMetaData.objects.filter(user=user,weekno=weekno)
    exif_dict = exifread.process_file(xx.image)

    lon_ref = exif_dict["GPS GPSLongitudeRef"].printable
    lon = exif_dict["GPS GPSLongitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
    lon = float(lon[0]) + float(lon[1]) / 60 + float(lon[2]) / float(lon[3]) / 3600
    if lon_ref != "E":
        lon = lon * (-1)


    lat_ref = exif_dict["GPS GPSLatitudeRef"].printable
    lat = exif_dict["GPS GPSLatitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
    lat = float(lat[0]) + float(lat[1]) / 60 + float(lat[2]) / float(lat[3]) / 3600
    if lat_ref != "N":
        lat = lat * (-1)

    date_ = str(exif_dict['EXIF DateTimeOriginal'])
    date_ = date_.split(' ')[0]

    date_ = date_.split(':')
    d = datetime.date(int(date_[0]), int(date_[1]), int(date_[2]))    
    xy.update(lati=lat,long=lon,metadata_date=d)
    
