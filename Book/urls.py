from django.urls import path
from .views import listbook,Publicpostuser,Privatepostuser,AdminAdminuser,Readorlogin
urlpatterns = [
    path('allbook/',listbook.as_view()),
    path('AllowAny/',Publicpostuser.as_view()),
    path('Just/',Privatepostuser.as_view()),
    path('JustReador/',Readorlogin.as_view()),
    path('AdAd/',AdminAdminuser.as_view())


]
