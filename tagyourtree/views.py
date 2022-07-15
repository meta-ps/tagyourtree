from django.shortcuts import render,redirect
from tagyourtree.models import *
from API_KEYS.keys import keys
from pathlib import Path
from utility.nftstorage import NftStorage
import json
import shutil
from pathlib2 import Path as Path2_
import requests
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

        print(WalletAddress)
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

# def imageUpload(request):
#     global img_file_list
#     files = request.FILES.getlist('allimages')
#     WalletAddress = request.session['WalletAddress']
#     meta_file_list = []
#     user = User.objects.get(WalletAddress=WalletAddress)

#     path =Path(os.path.normpath( str(BASE_DIR) + '/'+ str(user.id) +'/metadata/'))
#     print(path)
#     path_images =Path(os.path.normpath( str(BASE_DIR) + '/'+ str(user.id) + '/'+str(usercollection_obj.collection_name)+'/images/'))


#     try:
#         Path(path).mkdir(parents=True, exist_ok=True)
#     except Exception as e:
#         print(e)
    
#     count_image=0
#     images = {}
#     image_count = 0
#     for f in files:
#         a = UserCollectionImage.objects.get_or_create(usercollection=usercollection_obj,image=f,user=user)

#     i=1
#     for filename in os.listdir(path_images):
#         os.rename(os.path.join(path_images,filename),os.path.join(path_images,str(i)+'.jpg'))
#         i+=1
    
#     for filename in os.listdir(path_images):
#         img_file_list.append(str(Path(os.path.normpath(str(path_images)+'\\'+str(filename)))))
    
#     for k in img_file_list:
#         image_count +=1
#         token = {
#             "name": str(usercollection_obj.collection_name) + ' ' + str(image_count),
#             "image": base_uri + str(image_count),
#             "desc": "Hello World"
#         }
#         meta_file =   Path(str(path)+'/' + str(image_count) + '.json')
#         meta_file_list.append(meta_file)
#         print(meta_file)
    
#         with open(meta_file, 'w') as outfile:
#             json.dump(token, outfile, indent=4)
    
#     nstorage = {}
#     c = NftStorage(NFTSTORAGE_API_KEY)
#     print('LISTSTSTST----------------------------------------------------------------------')
#     print(img_file_list)
 
#     cid = c.upload(img_file_list, 'image/png')
#     usercollection_obj = UserCollection.objects.get(id=pkk)
#     usercollection_obj.collection_hash=cid
#     usercollection_obj.is_active=False
#     usercollection_obj.collection_count=image_count
#     usercollection_obj.save()
#     print(cid)
#     img_file_list.clear()
#     user_id = str(user.id)
#     try:
#         shutil.rmtree(user_id)
#     except OSError as e:
#         print ("Error: %s - %s." % (e.filename, e.strerror))


#     return redirect('userpage')
