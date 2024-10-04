from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import showallstudent
urlpatterns = [
    path('loginapi/',ObtainAuthToken.as_view()),
    path('showall/',showallstudent.as_view()),
    


]
