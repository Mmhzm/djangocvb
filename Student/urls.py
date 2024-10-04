from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import showallstudent,logoutToken,liststudent,createstudent,updatestudent,deletestudent
urlpatterns = [
    path('loginapi/',ObtainAuthToken.as_view()),
    path('showall/',showallstudent.as_view()),
    path('out/',logoutToken.as_view()),
    path('Liststu/',liststudent.as_view()),
    path('Createstu/',createstudent.as_view()),
    path('Deletestu/<int:pk>/',deletestudent.as_view()),
    path('Updatestu/<int:pk>/',updatestudent.as_view())



]
