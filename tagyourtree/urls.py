from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from tagyourtree.views import *

urlpatterns = [
    path('', Home,name='home'),
    path('login/',Login,name='login'),
    path('user/',UserPage, name='userpage'),
    path('addPlantName/',addPlantName,name='addPlantName'),
    path('addImageAndExtract/<str:weekno>/',addImageAndExtract,name='addImageAndExtract'),
    path('deploy/',Deploy,name='deploy')


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
