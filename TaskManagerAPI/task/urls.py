from django.urls import path,re_path , include
from rest_framework.routers import DefaultRouter
from task import views
router = DefaultRouter()   
router.register('tasks' , views.TaskViewSet , basename='taks')
urlpatterns = [
    re_path(r'^auth/', include('djoser.urls')),
    path('', include(router.urls)),
    
    ]
       