from django.urls import path
from .views import Allperson,Detailperson,Createperson,Updateperson,Deleteperson,Createuser,Authuser,LOGOUT
urlpatterns = [
    path('Allperson/',Allperson.as_view(),name="all"),
    path('Detailperson/<int:pk>/',Detailperson.as_view(),name="detail"),
    path('Createperson/',Createperson.as_view()),
    path('Updateperson/<int:pk>/',Updateperson.as_view()),
    path('Deleteperson/<int:pk>/',Deleteperson.as_view()),
    path('Createuser/',Createuser.as_view()),
    path('Authuser/',Authuser.as_view()),
    path('Logout/',LOGOUT.as_view())
    

]
