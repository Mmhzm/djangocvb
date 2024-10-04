from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import showallstudent,logoutToken
urlpatterns = [
    path('loginapi/',ObtainAuthToken.as_view()),
    path('showall/',showallstudent.as_view()),
    path('out/',logoutToken.as_view())

]
