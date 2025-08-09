from django.urls import path,re_path , include
from rest_framework.routers import DefaultRouter

routher = DefaultRouter()   
# routher.register()
urlpatterns = [
    re_path(r'^auth/', include('djoser.urls')),
]
       